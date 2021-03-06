import time
import argparse


# Returns a list containing all primes in range [0, n]
def trial_division(n):
    start_num = 3

    primes = []
    primes.append(2)

    for current_num in range(start_num, n, 2):
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

precision = args.precision
n = args.limit
start_time = time.time()

primes = trial_division(n)

time_elapsed = time.time() - start_time

print(f'Calculate all primes up to: {n}')
print(f'Time elasped: {time_elapsed:.{precision}f} seconds')
print(f'Number of primes calculated: {len(primes)}')

if args.print:
    print(primes)
