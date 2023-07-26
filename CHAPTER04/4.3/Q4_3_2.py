def funk_square(*args):
    result = []
    for n in args:
        result.append(n * n)
    return results

numbers = [1, 2, 3, 4]
func_square(*numbers)
