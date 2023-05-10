from time import perf_counter
import threading
import requests
import os

# CPU-bound task (heavy computation)
def encrypt_file(path: str):
    start = perf_counter()
    print(f"Processing image from {path} in process {os.getpid()}")
    # Simulate heavy computation by sleeping for a while
    _ = [i for i in range(100_000_000)]
    encryption_counter = perf_counter() - start
    print(f"Time taken for encryption task: {encryption_counter}.")

# I/O-bound task (downloading image from URL)
def download_image(image_url):
    start = perf_counter()
    print(f"Downloading image from {image_url} in thread {threading.current_thread().name}")
    response = requests.get(image_url)
    with open("image.jpg", "wb") as f:
        f.write(response.content)
    download_counter = perf_counter() - start
    print(f"Time taken for I/O-bound task: {download_counter}.")

