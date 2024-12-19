def compute_statistics(data):
    total = sum(data)
    mean = total / len(data)  # E501 line too long (36 > 79 characters)
    squared_diff = [(x - mean) ** 2 for x in data]
    variance = sum(squared_diff) / len(data)
    return mean, variance

def print_statistics(data):
    mean, variance = compute_statistics(data)
    print("Mean is: ", mean)  # W291 trailing whitespace
    print("Variance is: ", variance)  # E501 line too long (40 > 79 characters)

# Пример использования функции
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print_statistics(data)  # E501 line too long (73 > 79 characters)
