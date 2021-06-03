import math
import sys
import time


# Returns a list containing all primes in range [0, n]
def sieve_of_erastothenes(n):
    primes = []
    start_number = 2
    end_number = n + 1

    # Create a boolean list with all values set to True
    A = [True for i in range(end_number)]

    sqrtN = int(math.sqrt(n))
    for i in range(start_number,  sqrtN):

        # If the number is not marked, then mark all of it's multiples
        if (A[i] == True):
            # Mark all multiples of i, starting from i^2
            for j in range(i * i, end_number, i):
                A[j] = False

    # 0 and 1 are not prime numbers
    A[0] = False
    A[1] = False

    # Save all not marked numbers to the return list
    for i in range(n + 1):
        if A[i]:
            primes.append(i)

    return primes


n = int(sys.argv[1])
start_time = time.time()

primes = sieve_of_erastothenes(n)

time_elapsed = round(time.time() - start_time, 2)

print(f'Calculate all primes up to: {n}')
print(f'Time elasped: {time_elapsed} seconds')
print(f'Number of primes calculated: {len(primes)}')
# print(primes)
