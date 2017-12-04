import functools
import operator
def square_of_sum(inp):
    return operator.pow(functools.reduce(operator.add,range(1,inp+1)),2)


def sum_of_squares(inp):
    return functools.reduce(operator.add, list(operator.pow(x,2) for x in range(1,inp+1)))


def difference(inp):
    return square_of_sum(inp) - sum_of_squares(inp)

if __name__ == '__main__':
    print(difference(5))
