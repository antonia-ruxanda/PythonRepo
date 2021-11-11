def my_func(*args, **kwargs):
    my_sum = 0
    for i in args:
        if type(i) is int or type(i) is float:
            my_sum += i
    return my_sum


def recursive_func(n: int) -> (int, int, int):
    if n == 0:
        return 0, 0, 0
    if n % 2 == 1:
        return n + recursive_func(n - 1)[0], n + recursive_func(n - 1)[1], recursive_func(n - 1)[2]
    return n + recursive_func(n - 1)[0], recursive_func(n - 1)[1], n + recursive_func(n - 1)[2]


def check_type():
    val = input("Write something: ")
    try:
        val_int = int(val)
        return val_int
    except ValueError as e:
        return 0


print(f'The sum is:{my_func(1, 5, -3, "abc", [12, 56, "cad"])}')
print(f'The sum is:{my_func()}')
print(f'The sum is: {my_func(2, 4, "abc", param_1 = 2)}')

print(f'The total, odd and even sum is: {recursive_func(10)}')

print(f'{check_type()}')