class FlatIterator:

    def __init__(self, list_of_list):
        self.content_list = list_of_list
        self.start = 0
        self.end = len(list_of_list)

    def __iter__(self):
        self.iter_index = 0
        return self

    def __next__(self):
        if self.start == self.end:
            raise StopIteration
        values = self.content_list[self.start]
        item = values[self.iter_index]
        if self.iter_index != len(values) - 1:
            self.iter_index += 1
        else:
            self.iter_index = 0
            self.start += 1
        return item


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e',
                                                   'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()