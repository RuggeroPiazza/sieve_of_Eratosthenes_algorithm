"""The program runs 3 ways of generate prime numbers up to 50_000_000
    and prints the running time.
    Algorithm: Sieve of Eratosthenes"""
import time


def sieve_with_set(n=50_000_000):
    """Using a set to store the multiples.
        Using the set.update method avoids explicit iteration in the interpreter."""
    multiples = set()
    for i in range(2, n + 1):
        if i not in multiples:
            yield i
            multiples.update(range(i * i, n + 1, i))
    return multiples


def sieve_with_array(limit=50_000_000):
    """Using array lookup to test for primality.
        Straightforward implementation of the Sieve of Eratosthenes algorithm."""
    is_prime = [False] * 2 + [True] * (limit - 1)
    for n in range(int(limit**0.5 + 1.5)):
        if is_prime[n]:
            for i in range(n * n, limit + 1, n):
                is_prime[i] = False
    return [i for i, prime in enumerate(is_prime) if prime]


def sieve_with_generator(limit=50_000_000):
    """Same approach but with a generator.
        Slightly slower than the previous one but uses no memory for output."""
    is_prime = [False] * 2 + [True] * (limit - 1)
    for n in range(int(limit**0.5 + 1.5)):
        if is_prime[n]:
            for i in range(n * n, limit + 1, n):
                is_prime[i] = False
    for i in range(limit + 1):
        if is_prime[i]:
            yield i


def benchmark(function):
    start_time = time.time()
    function()
    end_time = time.time()
    print(f"Program: {function.__name__}    runs in --- {round(end_time - start_time, 5)} seconds ---")


def benchmark_generators(function):
    start_time = time.time()
    for _ in function():
        pass
    end_time = time.time()
    print(f"Program: {function.__name__}    runs in --- {round(end_time - start_time, 5)} seconds ---")


if __name__ == "__main__":
    benchmark(sieve_with_array)
    benchmark_generators(sieve_with_set)
    benchmark_generators(sieve_with_generator)
