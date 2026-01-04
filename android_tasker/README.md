# Android Tasker & Termux Setup

This document explains how the PNL Watch Display is executed on Android using
Termux and Tasker.

## Overview
- Tasker triggers a shell script
- Shell script runs the Python PNL fetcher via Termux
- Output is written to a text file
- Tasker displays the value as a global popup overlay
- Notification is mirrored to Galaxy Watch automatically

## File locations
- Python script:
/data/data/com.termux/files/home/.termux/tasker/pnl.py

diff
Copy code

- Shell script:
/data/data/com.termux/files/home/.termux/tasker/pnl.sh

csharp
Copy code

- Output file:
/sdcard/Download/pnl.txt

markdown
Copy code

## Tasker configuration (high level)
- Action: Run Shell
- Command: `bash pnl.sh`
- Working directory: `.termux/tasker`
- Run via Termux environment

## Notes
- Popup overlay is system-wide (visible on top of any app)
- No API keys are stored in the repository