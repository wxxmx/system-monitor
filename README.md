# System Monitor & Log Analyzer

A Python-based system monitoring and log analysis tool for macOS.

## Features
- Monitors CPU, memory, and disk usage
- Lists top running processes by CPU usage
- Analyzes macOS system logs for errors, warnings, and authentication-related events
- Generates persistent system reports with timestamps

## Technologies
- Python 3
- psutil
- macOS `log` command

## Usage
```bash
pip install -r requirements.txt
python3 monitor.py
