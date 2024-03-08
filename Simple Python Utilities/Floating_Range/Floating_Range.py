from typing import Iterator, Generator


class frange:
    def __init__(self, starting_num: float = 0.0, ending_num: float = 1.0, interval_float: float = 1.0) -> Generator[float, None, None]:
        self.starting_num = starting_num
        self.ending_num = ending_num
        self.interval_float = interval_float

    def __iter__(self) -> Iterator[float]:
        i = self.starting_num
        if self.interval_float >= 0:
            while i < self.ending_num:
                yield i
                i += self.interval_float
        else:
            while i > self.ending_num:
                yield i
                i += self.interval_float

    length = property(lambda self: int((self.ending_num - self.starting_num) // self.interval_float))
    start = property(lambda self: self.starting_num)
    stop = property(lambda self: self.ending_num)
    step = property(lambda self: self.interval_float)

    def __getitem__(self, index) -> float:
        temp = self.start + (index * self.step)
        if (temp < self.stop) and (str(type(index)) == "<class 'int'>"):
            return temp
        elif str(type(index)) != "<class 'int'>":
            raise TypeError('frange indices must be integers or slices, not float')
        elif temp >= self.stop:
            raise IndexError('frange object index out of range')

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self.start}, {self.stop}, {self.step})"
