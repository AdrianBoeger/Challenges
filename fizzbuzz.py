# Implement the FizzBuzz algorithm. Print numbers from 1 to 100, but for multiples of 3,
# print "Fizz" instead of the number, and for multiples of 5, print "Buzz."
# For numbers that are multiples of both 3 and 5, print "FizzBuzz."
import math


def fizzbuzz(number):
    if math.remainder(number, 3) == 0.0 and math.remainder(number, 5) == 0.0:
        return 'FizzBuzz'
    elif math.remainder(number, 3) == 0.0:
        return 'Fizz'
    elif math.remainder(number, 5) == 0.0:
        return 'Buzz'
    else:
        return number


def main():
    for number in range(1, 101):
        print(fizzbuzz(number))


if __name__ == '__main__':  # pragma: no cover
    main()
