import concurrent.futures
import math

PRIMES = [
    11227253509529316545641695165156,
    11258270594217121561654981616213285,
    1122725350952932616169198516521653,
    11528009519077315149845162163,
    1157978480770991549159165132169,
    10997268992854191519616213215896]

def is_prime(n):
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('%d is prime: %s' % (number, prime))

if __name__ == '__main__':
    main()