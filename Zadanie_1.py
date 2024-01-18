import copy


class Prototype:
    def __init__(self):
        self._data = {}

    def add_item(self, key, value):
        self._data[key] = value

    def get_item(self, key):
        return self._data.get(key)

    def clone(self):
        return copy.deepcopy(self)


proto = Prototype()
proto.add_item('item1', 1)
proto.add_item('item2', 2)

copy1 = proto.clone()

copy1.add_item('item3', 3)

print('Prototype:')
print(proto.get_item('item1'))
print(proto.get_item('item2'))

print('Copy:')
print(copy1.get_item('item1'))
print(copy1.get_item('item2'))
print(copy1.get_item('item3'))