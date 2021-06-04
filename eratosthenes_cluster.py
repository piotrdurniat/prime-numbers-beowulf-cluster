from mpi4py import MPI
import time
import argparse
import math


# Returns a Boolean list marking all primes in range [0, n]
def sieve_of_erastothenes(n):
    start_number = 2
    end_number = n + 1

    # Create a boolean list with all values set to True
    A = [True for i in range(end_number)]

    sqrtN = int(math.sqrt(n))
    for i in range(start_number,  sqrtN + 1):

        # If the number is not marked, then mark all of it's multiples
        if (A[i] == True):
            # Mark all multiples of i, starting from i^2
            for j in range(i * i, end_number, i):
                A[j] = False

    # 0 and 1 are not prime numbers
    A[0] = False
    A[1] = False

    return A


# Returns all primes in block: (start_num, end_num]
def eratosthenes_cluster(start_num, end_num):
    # list that will be returned containing all primes in this block
    primes = []
    block_size = end_num - start_num

    # Seperate list of primes used for sieving
    sieving_list_len = int(math.sqrt(end_num))
    sieving_list = sieve_of_erastothenes(sieving_list_len)

    # Boolean list for saving primes in the block
    A = [True for i in range(block_size)]

    # Loop through every number in the sieving_list
    for i in range(2,  sieving_list_len + 1):

        # If the number is not marked in the sieving list
        # then mark all of it's multiples in the restult list
        if (sieving_list[i] == True):

            # This is the first number that is smaller than start_num and is a multiple of i
            first_greater_multiple = start_num + i - (start_num % i)

            # Mark all multiples of i,
            # starting from the last multiple smaller than start_num up to end_num
            for j in range(first_greater_multiple, end_num, i):

                # Map values to be start from 0
                A[j - start_num] = False

    # 0 is not used, as it is eather a 0 or at the end of previous block
    A[0] = False

    # If this is the first block, then we need to add numbers from the sieving list
    if (start_num == 0):

        # Manually remove 1 in the first block as it won't appear in the multiples :(
        A[1] = False

        for i in range(sieving_list_len + 1):
            if sieving_list[i]:
                primes.append(i)

    # Save all not marked numbers to the return list
    for i in range(block_size):
        if A[i]:
            primes.append(i + start_num)

    return primes


precision = 6

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
start_num = int((limit / cluster_size) * node_rank)
end_num = int((limit / cluster_size) * (node_rank + 1))

start_time = time.time()

primes = eratosthenes_cluster(start_num, end_num)

# Send results to the master node
results = comm.gather(primes, root=0)

# Show the results if current node is the master
if node_rank == 0:

    time_elapsed = round(time.time() - start_time, precision)

    # Combine all of the primes into one list
    all_primes = [item for sublist in results for item in sublist]

    print(f'Calculate all primes up to: {limit}')
    print(f'Number of nodes: {cluster_size}')
    print(f'Time elasped: {time_elapsed} seconds')
    print(f'Number of primes calculated: {len(all_primes)}')
    if args.print:
        print(all_primes)
