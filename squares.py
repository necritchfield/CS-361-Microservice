def square_root(num):
    num = float(num)
    if (num < 0):
        return "Square root cannot be calculated."
    else:
        num_root = num ** 0.5
        return num_root

def square(num):
    num = float(num)
    num_square = num * num
    return num_square