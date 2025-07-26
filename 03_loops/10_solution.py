# Exponential Backoff Strategy
import time

wait_time = 1  # Initial wait time in seconds
max_retries = 5
attempts = 0

while attempts < max_retries:
    print(f"Attempt {attempts + 1}, Wait Time {wait_time}")
    time.sleep(wait_time)
    wait_time *= 2  # Double the wait time for the next attempt
    attempts += 1
