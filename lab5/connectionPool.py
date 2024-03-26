import multiprocessing
import time
import random
from threading import Semaphore

class ConnectionPool:
    def __init__(self, size):
        self.connections = ['Connection #{}'.format(i+1) for i in range(size)]
        self.semaphore = multiprocessing.Semaphore(size)
    
    def get_connection(self):
        self.semaphore.acquire()
        return self.connections.pop()
    
    def release_connection(self, connection):
        self.connections.append(connection)
        self.semaphore.release()

def access_database(connection_pool):
    print("Process {} waiting for connection.".format(multiprocessing.current_process().name))
    connection = connection_pool.get_connection()
    print("Process {} acquired {}.".format(multiprocessing.current_process().name, connection))
    time.sleep(random.randint(1, 5))  
    print("Process {} released {}.".format(multiprocessing.current_process().name, connection))
    connection_pool.release_connection(connection)

def main():
    pool_size = 2  
    number_of_processes = 10 
    connection_pool = ConnectionPool(pool_size)
    
    processes = [multiprocessing.Process(target=access_database, args=(connection_pool,)) for _ in range(number_of_processes)]
    
    for process in processes:
        process.start()
    
    for process in processes:
        process.join()

if __name__ == "__main__":
    main()
