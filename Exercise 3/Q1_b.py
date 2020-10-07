def sum_of_divided(num):
    return sum([i for i in range(1, num) if num % i == 0]) >= num


def dict_Of_Divided(myList):
  return {k: [factor for number in myList if sum_of_divided(number) for factor in [i for i in range(1, number) if number % i == 0]].count(k)
          for k in set([factor for number in myList if sum_of_divided(number) for factor in [i for i in range(1, number) if number % i == 0]])}


myList = [12, 34, 28, 53, 64]
print(dict_Of_Divided(myList))