import platform
import os
import time
from multiprocessing import Process, set_start_method

def process_fork():
    print("Main Process : ", str(os.getpid()))
    if platform.system() == 'Windows':
        from multiprocessing import Process, set_start_method
        set_start_method('fork')
        p = Process(target=getattr(run, func + '_run')())
        p.start()
        p.join()
    elif platform.system() == 'Linux':
        if os.fork() == 0:  # Child
            time.sleep(1)
            print("Sub Process : ", str(os.getpid()))
        else:
            print("Pre Process : ", str(os.getpid()))
    else:  # MacOS = Darwin
        if os.fork() == 0:  # Child
            time.sleep(1)
            print("Sub Process : ", str(os.getpid()))
        else:
            print("Pre Process : ", str(os.getpid()))

if __name__ == "__main__":
    process_fork()
    time.sleep(1)
    process_fork()

    time.sleep(2)