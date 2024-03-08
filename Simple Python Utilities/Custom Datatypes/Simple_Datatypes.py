from Custom_Errors import *


# Array([el1, el2, el3, el4]) --> Array([el1 el2 el3 el4])
class Array:
    """Array([el1, el2, el3, el4]) --> Array([el1 el2 el3 el4])"""
    def __init__(self, data):
        self.list = data
        self.list = list(self.list)

    def __getitem__(self, index):
        try:
            return self.list[index]
        except:
            raise InvalidIndexError(
                index
            )

    def __setitem__(self, index, value):
        try:
            self.list[index] = value
        except:
            raise SetItemError()

    def __len__(self):
        return len(self.list)

    def __str__(self):
        return f"{self.__class__.__name__}([{' | '.join([str(x) for x in self.list])}])"

    def add_at_left(self, val):
        self.list = [val] + self.list

    def add_at_right(self, val):
        self.list.append(val)

    def remove_all(self, val):
        self.list = [i for i in self.list if i != val]

    def clear(self):
        self.list = []

    def remove_at_left(self, val):
        temp = []
        not_found = True
        for i in self.list:
            if i != val:
                temp.append(i)
            else:
                if not_found:
                    not_found = False
                elif not not_found:
                    temp.append(i)
        self.list = temp
        return self.list

    def remove_at_right(self, val):
        self.list = self.list[::-1]
        temp = []
        not_found = True
        for i in self.list:
            if i != val:
                temp.append(i)
            else:
                if not_found:
                    not_found = False
                elif not not_found:
                    temp.append(i)
        self.list = temp[::-1]

    def pop(self, index=-1):
        if len(self.list) <= index:
            raise InvalidIndexError(
                index
            )
        else:
            return self.list.pop(index)

    def __repr__(self):
        return self.list


# DictDatatype1((k1, k2), (v1, v2, v3)) --> DictDatatype1({k1: v1, k2: v2, None: v3})
class DictDatatype1:
    """DictDatatype1((k1, k2), (v1, v2, v3)) --> DictDatatype1({k1: v1, k2: v2, None: v3})"""
    def __init__(self, keys, values):
        keys = list(keys)
        values = list(values)
        while len(keys) > len(values):
            values.append(None)
        while len(values) > len(keys):
            keys.append(None)
        self.dict = {}
        for i, j in zip(keys, values):
            if i not in self.dict:
                self.dict[i] = []
            if i in self.dict:
                self.dict[i].append(j)

    def __getitem__(self, key):
        try:
            return self.dict[key]
        except:
            raise InvalidKeyError(
                key
            )

    def __setitem__(self, key, value):
        try:
            self.dict[key].append(value)
        except:
            raise SetItemError()

    def __len__(self):
        return len(list(self.dict.keys()))

    def __str__(self):
        return f"{self.__class__.__name__}({str(self.dict)})"

    def clear(self):
        self.dict = {}

    def __repr__(self):
        return self.dict


# ListToCounterDict([el1, el2, el3, el1, el3]) --> ListToCounterDict({el1: 2, el2: 1, el3: 2})
class ListToCounterDict:
    """ListToDictCounter([el1, el2, el3, el1, el3]) --> ListToDictCounter({el1: 2, el2: 1, el3: 2})"""
    def __init__(self, data):
        self.list = data
        self.list = list(self.list)
        temp = {}
        for i in self.list:
            if i not in temp:
                temp[i] = 1
            else:
                temp[i] += 1
        self.dict = temp

    def __getitem__(self, key):
        try:
            return self.dict[key]
        except:
            raise InvalidKeyError(
                key
            )

    def __len__(self):
        return len(list(self.dict.keys()))

    def __setitem__(self, var, count):
        try:
            temp = 0
            for i in self.list:
                if i == var:
                    temp += 1
            for _ in range(count - temp):
                self.list.append(var)
            self.dict[var] = count
        except:
            raise SetItemError()

    def __str__(self):
        return f"{self.__class__.__name__}({self.dict})"

    def clear_item(self, item):
        temp = []
        for i in self.list:
            if i != item:
                temp.append(i)
        self.list = temp
        if item in self.dict:
            del self.dict[item]

    def clear_all(self):
        self.list = []
        self.dict = {}

    def custom_mode(self, datatype=None):
        if datatype is None:
            return self.__str__()
        else:
            try:
                return datatype(self.dict)
            except:
                raise TypeError(
                    f"Unable to Convert into '{datatype}'"
                )

    def frequently_appeared(self):
        try:
            max_num = max(self.dict.values())
            max_vals = tuple()
            for i, j in self.dict.items():
                if j == max_num:
                    max_vals += (i, )
            return list(max_vals)
        except:
            return []

    def infrequently_appeared(self):
        try:
            min_num = min(self.dict.values())
            min_vals = tuple()
            for i, j in self.dict.items():
                if j == min_num:
                    min_vals += (i,)
            return list(min_vals)
        except:
            return []

    def __repr__(self):
        return self.dict
