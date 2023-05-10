from time import perf_counter
from threading import Thread
from IO_CPU_bound_tasks import encrypt_file, download_image


if __name__ == "__main__":
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
        print(f"Error occurred: {e}")