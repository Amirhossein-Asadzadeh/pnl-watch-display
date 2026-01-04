# PNL Watch Display

Real-time crypto unrealized PNL display on Android and Galaxy Watch using Bitunix API.

## How it works
- Python script fetches unrealized PNL from Bitunix Futures
- Bash script runs via Termux/Tasker
- Output is written to a text file and shown as notification / watch sync

## Tech
Python · Bash · Termux · Tasker · REST API

## Security
API keys are read from environment variables and are not stored in the code.
