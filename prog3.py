from mpi4py import MPI
import numpy as np
import time

def square(start, end):
    # Using numpy
    numbers = np.arange(start, end + 1, dtype=int)
    return numbers ** 2

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    n = int(1e9)
    chunk_size = n // size

    if rank == 0:
        # Main process
        start_time = time.time()
        
        # Calculating the main process chunk
        start = (size - 1) * chunk_size + 1
        result = square(start, n)
        final_result = np.empty(n, dtype=int)
        final_result[start-1:] = result

        # Gather results
        for i in range(1, size):
            start = (i - 1) * chunk_size
            end = start + chunk_size
            partial_result = comm.recv(source=i)
            final_result[start:end] = partial_result

        print("Size of final array:", final_result.size)
        print("Last square:", final_result[-1])
        print("Time taken:", time.time() - start_time)
    else:
        # Worker processes
        start = (rank - 1) * chunk_size + 1
        end = rank * chunk_size
        result = square(start, end)
        comm.send(result, dest=0)

if __name__ == "__main__":
    main()
