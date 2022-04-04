from multiprocessing import *
import time


class PrimeNumber:
    def __init__(self, limit):
        self.limit = limit
        self.list = [2, 3, 5, 7]

    def add_prime(self, number):
        self.list.append(number)

    def prime_range(self, number):
        return (prime for prime in self.list if prime <= int(number ** 0.5))

    def is_prime(self, number):
        for prime in self.prime_range(number):
            if not number % prime:
                return False
        else:
            return True


if __name__ == '__main__':
    tic = time.time()

    prime = PrimeNumber(1000)
    workers = 4

    pool = Pool(workers)
    for number in range(11, prime.limit + 1, 4):
        checks = pool.map(prime.is_prime, range(number, number + 4))
        for index, check in enumerate(checks):
            if check:
                prime.list.append(number + index)
    pool.close()

    prime.list.sort()
    print(prime.list)

    toc = time.time()
    print(f'This process took {toc - tic : .4f} seconds')
