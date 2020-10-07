def sum_of_divided(num):
    return sum([i for i in range(1, num) if num % i == 0]) >= num

print(sum_of_divided(12))