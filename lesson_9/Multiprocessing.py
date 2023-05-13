from time import perf_counter
from multiprocessing import Process
from IO_CPU_bound_tasks import encrypt_file, download_image


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
