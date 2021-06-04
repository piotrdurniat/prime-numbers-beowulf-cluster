from mpi4py import MPI
import time
import argparse


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


# Parse args
parser = argparse.ArgumentParser(
    description='Finds all primes up to a given limit.')
parser.add_argument('limit', type=int, help='The limit')
parser.add_argument(
    '--print', help='Print all primes after execution', action="store_true")
parser.add_argument(
    '--precision', help='The number of decimal places in elapsed time', default=6, type=int)
args = parser.parse_args()


# Setup the cluster
comm = MPI.COMM_WORLD
# The the current rank and the cluster size
current_rank = comm.Get_rank()
cluster_size = comm.Get_size()

# Number to start on, based on the node's rank
start_num = (current_rank * 2) + 3

precision = args.precision
end_num = args.limit

start_time = time.time()

primes = trial_division_cluster(start_num, end_num, cluster_size)

# Send results to the master node
results = comm.gather(primes, root=0)

# Show the results if current node is the master
if current_rank == 0:

    time_elapsed = time.time() - start_time

    all_primes = [item for sublist in results for item in sublist]
    all_primes.append(2)
    all_primes.sort()

    print(f'Calculate all primes up to: {end_num}')
    print(f'Number of nodes: {cluster_size}')
    print(f'Time elasped: {time_elapsed:.{precision}f} seconds')
    print(f'Number of primes calculated: {len(all_primes)}')

if args.print:
    print(all_primes)
