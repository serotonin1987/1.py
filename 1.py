import time
import random
import threading

# Функция: записывает рандомное число в файл с задержкой 1 секунда
def write_random_to_file(index):
    time.sleep(1)
    number = random.randint(1, 1000)
    with open(f"output_{index}.txt", "w") as f:
        f.write(str(number))

# Последовательный запуск 1000 файлов
def run_sequential():
    start_time = time.time()
    for i in range(1000):
        write_random_to_file(i)
    end_time = time.time()
    print(f"⏱ Последовательное выполнение заняло: {end_time - start_time:.2f} секунд")

# Многопоточный запуск 1000 файлов
def run_multithreaded():
    start_time = time.time()
    threads = []

    for i in range(1000):
        t = threading.Thread(target=write_random_to_file, args=(i,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    end_time = time.time()
    print(f"⚡ Многопоточное выполнение заняло: {end_time - start_time:.2f} секунд")

# Выбор сценария запуска
if __name__ == "__main__":
    # Раскомментируйте нужный запуск:

    run_sequential()     # последовательный
    # run_multithreaded()    # многопоточный
