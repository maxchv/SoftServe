"""
Elementary Task #8

Ряд Фибоначчи для диапазона
----------------

Программа позволяет вывести все числа Фибоначчи, которые находятся в указанном диапазоне.
Диапазон задаётся двумя аргументами при вызове главного класса.
Числа выводятся через запятую по возрастанию.
"""

import sys


class Fibonacci:
    def __init__(self, start=0, stop=1):
        if stop > start:
            self.start = int(start)
            self.stop = int(stop)
            self.fib_seq = []
        else:
            raise ValueError

    def fib(self, n):
        phi = ((1 + (5 ** (1 / 2))) / 2)
        return str(round((phi ** n) / (5 ** (1 / 2))))

    def sequence(self):
        for n in range(self.start, self.stop + 1):
            self.fib_seq.append(self.fib(n))

    def __str__(self):
        self.sequence()
        return "Fibonacci sequence for a given range {start}-{stop} is: {seq}".format(start=self.stop, stop=self.stop,
                                                                                      seq=', '.join(self.fib_seq))


def main():

    if len(sys.argv) == 1:
        print(__doc__)

    try:
        # creating instance of Fibonacci class in certain range which is given as arguments
        fib = Fibonacci(sys.argv[1], sys.argv[2])
        print(fib)
        exit()
    except ValueError:
        print("Wrong arguments. Give start and stop values where stop is bigger (start < stop)")
    except IndexError:
        print("Wrong arguments. Must be 2 parameters: start, stop (start < stop)")


if __name__ == "__main__":
    main()
