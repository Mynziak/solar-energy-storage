def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def test_fibonacci_generator():
    n = 90  # Enter the Number for Fibonacci generator

    assert isinstance(n, int) and n >= 0, "n must be a non-negative integer!"

    fib_gen = fibonacci_generator()

    for i in range(n):
        result = next(fib_gen)
        print(f"Fibonacci number {i+1}: {result}")

