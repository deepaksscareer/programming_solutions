import time
import functools
import time


def timeit(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Start operator
        start_time = time.time()

        # Perform main function
        result = func(*args, **kwargs)

        # Get the end time
        end_time = time.time()

        # Print result
        print(f"The time taken to execute {func.__name__} is {end_time - start_time:.4f} seconds to run")

        # Getting result
        return result

    return wrapper


# Decorator to log the start and end timing and print the difference

@timeit
def sleep_machine(no_seconds: int):
    print("Started to sleep")
    time.sleep(no_seconds)
    print(f"Slept for {no_seconds} seconds.")

# Decorator to check the numbers entered are all positive

if __name__ == "__main__":

    sleep_machine(2)