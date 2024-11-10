# 10. Exponential Backoff
# Problem: 
# Implement an exponential backoff strategy that doubles the wait time between retries,
# starting from 1 second, but stops after 5 retries.

import time

# Set initial wait time and maximum number of retries
wait_time = 1  # in seconds
max_retries = 5
attempt = 1

# Loop for the backoff strategy
while attempt <= max_retries:
    print(f"Attempt {attempt}: Waiting for {wait_time} second(s)...")
    
    # Simulate the wait time (backoff)
    time.sleep(wait_time)
    
    # Double the wait time for the next retry
    wait_time *= 2
    attempt += 1

print("Max retries reached. Stopping.")
