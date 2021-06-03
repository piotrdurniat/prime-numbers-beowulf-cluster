from mpi4py import MPI
import time
import argparse


def eratosthenes_cluster(start_num, end_num):
    primes = []

    return primes


# Parse args
parser = argparse.ArgumentParser(
    description='Finds all primes up to a given limit.')
parser.add_argument('limit', type=int, help='The limit')
parser.add_argument(
    '--print', help='Print all primes after execution', action="store_true")
args = parser.parse_args()

# Get end number from args
limit = args.limit

# Setup the cluster
comm = MPI.COMM_WORLD
# The the current rank and the cluster size
node_rank = comm.Get_rank()
cluster_size = comm.Get_size()

# Number to start on, based on the node's rank
# Divides the range [0, limit] into equal chunks
start_num = (limit / cluster_size) * node_rank
end_num = (limit / cluster_size) * (node_rank + 1)

start_time = time.time()

primes = eratosthenes_cluster(start_num, end_num)

# Send results to the master node
results = comm.gather(primes, root=0)

# Show the results if current node is the master
if node_rank == 0:

    time_elapsed = round(time.time() - start_time, 2)

    # Combine all of the primes into one list
    all_primes = [item for sublist in results for item in sublist]

    print(f'Calculate all primes up to: {limit}')
    print(f'Number of nodes: {cluster_size}')
    print(f'Time elasped: {time_elapsed} seconds')
    print(f'Number of primes calculated: {len(all_primes)}')
    if args.print:
        print(all_primes)
