nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
    [1, 4, 5, 6, 9],
]

class FlatListIteration:
    def __init__(self, lst):
        self.lst = lst
        self.current_sublist = 0
        self.current_index = 0


    def __iter__(self):
        return self


    def __next__(self):
        if self.current_sublist >= len(self.lst):
            raise StopIteration
        sublist = self.lst[self.current_sublist]
        if self.current_index >= len(sublist):
            self.current_sublist += 1
            self.current_index = 0
            return self.__next__()
        item = sublist[self.current_index]
        self.current_index += 1
        return item


def get_flat_list(lst):
    for item in lst:
        if isinstance(item, list):
            yield from get_flat_list(item)
        else:
            yield item




if __name__ == '__main__':
    for item in FlatListIteration(nested_list):
        print(item)
    flat_list = [item for item in FlatListIteration(nested_list)]
    print(flat_list)

    for item in get_flat_list(nested_list):
        print(item)






