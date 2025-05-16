import functools
import logging
import time

import requests

logging.basicConfig(level=logging.INFO)

def retry_job(no_retry=3, exponential_backoff=2, delay=1, exception=(Exception)):
    # No edge conditions here
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):

            # Perform the operation, wait till the retries are done
            attempts = 0
            attempted_delay = delay

            while attempts < no_retry:
                # Try
                try:

                    logging.info("Starting to download")

                    result = func(*args, **kwargs)

                    print(f"Result obtained success: {result}")
                    return result

                except exception as e:

                    attempts += 1
                    attempted_delay = attempted_delay ** exponential_backoff

                    logging.info("Beginning to retry")

                    if attempts == no_retry:
                        logging.warning("Reached the maximum retry and thus exiting!!")
                        raise

                    logging.warning(f"Got the error : {e}")
                    logging.warning(f"Retrying now: {attempts}")

                    logging.warning(f"Retying the operation after : {attempted_delay} seconds!!")

                    time.sleep(attempted_delay)

        return wrapper

    return decorator


@retry_job(no_retry=2, exponential_backoff=2, delay=1, exception=(requests.RequestException))
def get_data(url: str, timeout: int):
    # Get response
    response = requests.get(url, timeout=timeout)

    # Raise error if there is 400 / 500 response issue
    response.raise_for_status()

    # Return response
    return response.json()


try:
    # Getting dummy data from API call
    # Bad case
    # https://api.example.com/data
    # Good API
    #
    data = get_data(url='https://jsonplaceholder.typicode.com/todos/1', timeout=2)
    print(f"Received data successfully {data}")

except Exception as e:
    print(e)