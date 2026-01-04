#!/data/data/com.termux/files/usr/bin/bash

OUT=$(/data/data/com.termux/files/usr/bin/python \
/data/data/com.termux/files/home/.termux/tasker/pnl.py)

NUM=$(echo "$OUT" | sed -n 's/.*PNL:[[:space:]]*\([-0-9.]\+\).*/\1/p')

echo "$NUM" > /sdcard/Download/pnl.txt
