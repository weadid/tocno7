def fibonacci(n):
    if n <= 0:  # E501 line too long (27 > 79 characters)
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        for i in range(2, n):
            next_fib = fib_sequence[i - 1] + fib_sequence[i - 2]
            fib_sequence.append(next_fib)  # E501 line too long (44 > 79 characters)
        return fib_sequence

# Пример использования функции
n = 10
print("Fibonacci sequence up to", n, ":", fibonacci(n))  # E501 line too long (54 > 79 characters)

# Комментарий без пробела
#Это пример функции
