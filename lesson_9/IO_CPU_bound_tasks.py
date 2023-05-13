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
    print(
        f"Downloading image from {image_url} in thread {threading.current_thread().name}"
    )
    response = requests.get(image_url)
    with open("image.jpg", "wb") as f:
        f.write(response.content)
    download_counter = perf_counter() - start
    print(f"Time taken for I/O-bound task: {download_counter}.")


from time import perf_counter
import threading
import requests
import os


# CPU-bound task (heavy computation)
def encrypt_file(path: str):
    # start = perf_counter()
    print(f"Processing image from {path} in process {os.getpid()}")
    # Simulate heavy computation by sleeping for a while
    _ = [i for i in range(100_000_000)]
    # encryption_counter = perf_counter() - start
    # print(f"Time taken for encryption task: {encryption_counter}.")


# I/O-bound task (downloading image from URL)
def download_image(image_url):
    # start = perf_counter()
    print(
        f"Downloading image from {image_url} in thread {threading.current_thread().name}"
    )
    response = requests.get(image_url)
    with open("image.jpg", "wb") as f:
        f.write(response.content)
    # download_counter = perf_counter() - start
    # print(f"Time taken for I/O-bound task: {download_counter}.")


from time import perf_counter
from threading import Thread
from CPU_IO_bound_tasks import encrypt_file, download_image


"""if __name__ == "__main__":
    try:
        start = perf_counter()
        thread1 = Thread(target=encrypt_file, args=("rockyou.txt",))
        thread2 = Thread(target=download_image, args=("https://picsum.photos/1000/1000",))
        thread1.start()
        thread2.start()
        thread1.join()
        thread2.join()
        total = perf_counter() - start
        print(f"Total: {total} seconds")
    except Exception as e:
        print(f"Error occurred: {e}")"""


if __name__ == "__main__":
    try:
        start_encrypt_file = perf_counter()
        thread1 = Thread(target=encrypt_file, args=("rockyou.txt",))
        thread1.start()
        thread1.join()
        end1 = perf_counter()
        encryption_counter = end1 - start_encrypt_file
        start_download_image = perf_counter()
        thread2 = Thread(
            target=download_image, args=("https://picsum.photos/1000/1000",)
        )
        thread2.start()
        thread2.join()
        end2 = perf_counter()
        download_counter = end2 - start_download_image
        total = end2 - start_encrypt_file
        print(
            f"Time taken for encryption task: {encryption_counter}, I/O-bound task: {download_counter}, Total: {total} seconds"
        )
    except Exception as e:
        print(f"Error occurred: {e}")
from time import perf_counter
from multiprocessing import Process
from CPU_IO_bound_tasks import encrypt_file, download_image


if __name__ == "__main__":
    try:
        start = perf_counter()
        process1 = Process(target=encrypt_file, args=("rockyou.txt",))
        process2 = Process(
            target=download_image, args=("https://picsum.photos/1000/1000",)
        )
        process1.start()
        process2.start()
        process1.join()
        process2.join()
        total = perf_counter() - start
        print(f"Total: {total} seconds")
    except Exception as e:
        print(f"Error occurred: {e}")

"""if __name__ == "__main__":
    try:
        start = perf_counter()
        start_encrypt_file = perf_counter()
        process1 = Process(target=encrypt_file, args=("rockyou.txt",))
        process1.start()
        start_download_image = perf_counter()
        process2 = Process(target=download_image, args=("https://picsum.photos/1000/1000",))
        process2.start()
        process1.join()
        process2.join()
        end1 = perf_counter()
        end2 = perf_counter()
        encryption_counter = end1 - start_encrypt_file
        download_counter = end2 - start_download_image
        total = end2 - start
        print(f"Time taken for encryption task: {encryption_counter}, I/O-bound task: {download_counter}, Total: {total} seconds")
    except Exception as e:
        print(f"Error occurred: {e}")"""
