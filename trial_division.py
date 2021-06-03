import time
import sys


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


n = int(sys.argv[1])
start_time = time.time()

primes = trial_division(n)

time_elapsed = round(time.time() - start_time, 2)

print(f'Calculate all primes up to: {n}')
print(f'Time elasped: {time_elapsed} seconds')
print(f'Number of primes calculated: {len(primes)}')
# print(primes)
