def get_factors(number):
    return [i for i in range(1, number) if number % i == 0]

def factors_generator(number):
    return (False if len(get_factors(number)) == 1 else factor for factor in get_factors(number))

my_generator = factors_generator(5)
print("Number 5:")
print(my_generator.__next__())

my_generator = factors_generator(6)
print("Number 6:")
print(my_generator.__next__())
print(my_generator.__next__())
print(my_generator.__next__())

