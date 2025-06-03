from functools import reduce

def f_to_c(temp, f_to_c_lambda):
    return f_to_c_lambda(temp)

f_to_c_lambda = lambda f: (f - 32) * 5/9
f = 98.6
c = f_to_c(f, f_to_c_lambda)
print(f"{f}°F is {c:.2f}°C")

input_list = [0, 3, 10, 27, 45, 52, 70]
filter_list = list(filter(lambda x: x % 5 == 0, input_list))
print("Filtered list:", filter_list)

str_list = ["Hello", "world"]
uppercase_list = list(map(lambda s: s.upper(), str_list))
print("Uppercase list:", uppercase_list)

def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))

num = 3
result = factorial(num)
print(f"{num}! is {result}")