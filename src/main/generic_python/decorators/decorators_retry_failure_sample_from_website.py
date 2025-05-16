import functools
import logging
import time
import requests

def retry(max_attempts=3, delay_seconds=1, backoff_factor=2, exceptions=(Exception,)):
    """Retry a function if it raises specified exceptions."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            current_delay = delay_seconds

            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempts += 1
                    if attempts == max_attempts:
                        logging.error(f"Failed after {attempts} attempts. Last error: {e}")
                        raise

                    logging.warning(
                        f"Attempt {attempts} failed with error: {e}. "
                        f"Retrying in {current_delay} seconds..."
                    )

                    time.sleep(current_delay)
                    current_delay *= backoff_factor

        return wrapper
    return decorator

@retry(max_attempts=5, delay_seconds=1, exceptions=(requests.RequestException,))
def fetch_data(url):
    """Fetch data from an API with retry logic."""
    response = requests.get(url, timeout=2)
    response.raise_for_status()  # Raise exception for 4XX/5XX responses
    return response.json()

# This will retry up to 5 times if the request fails
try:
    data = fetch_data('https://api.example.com/data')
    print("Successfully fetched data!")
except Exception as e:
    print(f"All retry attempts failed: {e}")
