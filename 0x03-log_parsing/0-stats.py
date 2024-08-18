#!/usr/bin/python3
import sys
import signal

# Global variables to store total file size and counts of each status code
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

def print_stats():
    """
    Prints the accumulated metrics.
    """
    print(f"File size: {total_size}")
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def signal_handler(sig, frame):
    """
    Handles the SIGINT (CTRL+C) signal and prints the metrics before exiting.
    """
    print_stats()
    sys.exit(0)

# Register the signal handler for SIGINT
signal.signal(signal.SIGINT, signal_handler)

# Process the input lines from stdin
try:
    line_count = 0
    for line in sys.stdin:
        line_count += 1
        parts = line.split()
        if len(parts) > 6:
            try:
                file_size = int(parts[-1])
                status_code = int(parts[-2])
                total_size += file_size
                if status_code in status_codes:
                    status_codes[status_code] += 1
            except ValueError:
                continue

        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    raise

