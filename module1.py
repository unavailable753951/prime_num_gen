class PrimeGenerator:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def generate_primes(self):
        return [num for num in range(self.start, self.end + 1) if self.is_prime(num)]
