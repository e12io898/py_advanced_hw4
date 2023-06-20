import types


def flat_generator(list_of_lists):
    start, end, ind = 0, len(list_of_lists), 0
    while True:
        values = list_of_lists[start]
        item = values[ind]

        yield item

        control = len(values) - 1
        ind, start = [ind + 1, start] if ind != control else [0, start + 1]

        if start == len(list_of_lists):
            break


def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e',
                                                     'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()