def generate_execution_observation_table(sizes):
    import math

    def fib_calls(n):
        if n <= 1:
            return 1
        return 1 + fib_calls(n - 1) + fib_calls(n - 2)

    result = []

    result.append("Algorithm Execution Observation Table")
    result.append("InputSize RecursiveFactorial IterativeFactorial RecursiveFibonacci IterativeFibonacci LinearSearch BinarySearch BubbleSort InsertionSort")

    rows = [
        str(n) + " " +
        str(n + 1) + " " +
        str(n) + " " +
        str(fib_calls(n)) + " " +
        str(n) + " " +
        str(n) + " " +
        str(math.floor(math.log2(n)) + 1) + " " +
        str(n * (n - 1) // 2) + " " +
        str(n * (n - 1) // 2)
        for n in sizes
    ]

    result.extend(rows)

    return result