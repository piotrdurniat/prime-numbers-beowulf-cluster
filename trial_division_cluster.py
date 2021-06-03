from mpi4py import MPI
import time
import sys


def trial_division_cluster(start_num, end_num, cluster_size):

    primes = []
    step = cluster_size * 2

    for current_num in range(start_num, end_num, step):
        is_prime = True

        # Check if the number is prime using Trial division
        for div_number in range(2, current_num):
            if current_num % div_number == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(current_num)

    return primes


# Setup the cluster
comm = MPI.COMM_WORLD
# The the current rank and the cluster size
current_rank = comm.Get_rank()
cluster_size = comm.Get_size()

# Number to start on, based on the node's rank
start_num = (current_rank * 2) + 3

# Get end number from args
end_num = int(sys.argv[1])

start_time = time.time()

# Rank number is used to divide calculation between nodes
primes = trial_division_cluster(start_num, end_num, cluster_size)

# Send results to the master node
results = comm.gather(primes, root=0)

# Show the results if current node is the master
if current_rank == 0:

    time_elapsed = round(time.time() - start_num, 2)

    all_primes = [item for sublist in results for item in sublist]
    all_primes.append(2)
    all_primes.sort()

    print(f'Calculate all primes up to: {end_num}')
    print(f'Number of nodes: {cluster_size}')
    print(f'Time elasped: {time_elapsed} seconds')
    print(f'Number of primes calculated: {len(all_primes)}')
