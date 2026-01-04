import os
import time
import json
import hashlib
import secrets
import requests


BASE_URL = "https://fapi.bitunix.com"
PATH = "/api/v1/futures/account"


def sha256_hex(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def make_sign(api_key: str, api_secret: str, nonce: str, timestamp_ms: str, query_params_str: str, body_str: str) -> str:
    # digest = SHA256(nonce + timestamp + api-key + queryParams + body)
    digest = sha256_hex(nonce + timestamp_ms + api_key + query_params_str + body_str)
    # sign = SHA256(digest + secretKey)
    sign = sha256_hex(digest + api_secret)
    return sign


def get_futures_account(margin_coin: str = "USDT") -> float:
    api_key = os.environ.get("BITUNIX_API_KEY", "").strip()
    api_secret = os.environ.get("BITUNIX_API_SECRET", "").strip()

    if not api_key or not api_secret:
        raise RuntimeError("Set env vars: BITUNIX_API_KEY and BITUNIX_API_SECRET")

    nonce = secrets.token_hex(16)  # 32 chars
    timestamp_ms = str(int(time.time() * 1000))

    # queryParams must be "key + value" concatenated, sorted by ASCII key
    # only one param here:
    query_params_str = f"marginCoin{margin_coin}"
    body_str = ""  # GET has no body

    sign = make_sign(api_key, api_secret, nonce, timestamp_ms, query_params_str, body_str)

    url = BASE_URL + PATH
    headers = {
        "api-key": api_key,
        "nonce": nonce,
        "timestamp": timestamp_ms,
        "sign": sign,
        "Content-Type": "application/json",
        "language": "en-US",
    }

    r = requests.get(url, params={"marginCoin": margin_coin}, headers=headers, timeout=10)
    r.raise_for_status()
    j = r.json()

    if j.get("code") != 0:
        raise RuntimeError(f"API error: {j}")

    data = j.get("data")
    # docs show array sometimes; your earlier response was object. handle both.
    if isinstance(data, list) and data:
        data = data[0]

    pnl = float(data.get("crossUnrealizedPNL", "0") or "0")
    return pnl


if __name__ == "__main__":
    pnl = get_futures_account("USDT")
    print(f"PNL: {pnl:.2f} USDT")
