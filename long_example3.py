def fibonacci(n):
    if n <= 0:  # Проверка на неотрицательное значение
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        for i in range(2, n):
            next_fib = fib_sequence[i - 1] + fib_sequence[i - 2]
            fib_sequence.append(next_fib)
        return fib_sequence


# Пример использования функции
n = 10
fibonacci_sequence = fibonacci(n)
print(f"Fibonacci sequence up to {n}: {fibonacci_sequence}")

# Это пример функции
