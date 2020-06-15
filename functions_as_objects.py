def multiply_by_two(n):
    return n * 2

def sum_two(n):
    return n + 2

def apply(f, numbers):
    results= []
    for number in numbers:
        result= f(number)
        results.append(result)

nums= [1, 2, 3]

apply(multiply_by_two, nums)
apply(sum_two, nums)


sumar = lambda x, y: x + y

sumar(2, 3)
""" results 5"""

"""fx in data structures"""

def apply_operation(num):
    operations= [abs, float]

    result = []

    for operation in operations:
        result.append(operations(num))

    return result

apply_operation(-2)
"""result [2, -2.0]"""