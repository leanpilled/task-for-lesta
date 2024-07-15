"""
На языке Python написать минимум по 2 класса реализовывающих циклический буфер FIFO. Объяснить плюсы и минусы каждой реализации.

Оценивается:

Полнота и качество реализации
Оформление кода
Наличие сравнения и пояснения по быстродействию
"""
from typing import TypeVar, Generic

T = TypeVar('T')

class BufferError(Exception):
    pass

class BufferAtMaxCapError(BufferError):
    pass

class BufferIsEmptyError(BufferError):
    pass


class MyFIFO1(Generic[T]):
    def __init__(self) -> None:
        self.buffer = []

    def push(self, item: T) -> None:
        self.buffer.append(item)
        
    def pop(self) -> T:
        if len(self.buffer) == 0:
            raise BufferIsEmptyError
        return self.buffer.pop(0)


class Node():
    def __init__(self, value: T):
        self.value = value
        self.next = None


class MyFIFO2(Generic[T]):
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def push(self, item: T) -> None:
        node = Node(item)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def pop(self) -> T:
        if self.head is None:
            raise BufferIsEmptyError
        else:
            item = self.head.value
            self.head = self.head.next
        return item


"""
первая реализация это просто список
кладем в конец берем с начала, можно наоборот без разницы

второй вариант это по сути линкед лист
добавляем элементы в конец берем с начала

по времени в первой реализации какая-то операция будет О(n) вторая константная (push или pop)
что касается второй тут все константа

по памяти и там и там линия (через линкед лист займет больше но тоже линия)
"""
