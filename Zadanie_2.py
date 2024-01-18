import copy


class Prototype:
    def clone(self):
        pass


class ConcreteProtoA(Prototype):
    def __init__(self, value):
        self.value = value

    def clone(self):
        return copy.deepcopy(self)


class ConcreteProtoB(Prototype):
    def __init__(self, data):
        self.data = data

    def clone(self):
        return copy.deepcopy(self)


proto_a = ConcreteProtoA(10)
proto_b = ConcreteProtoB([1, 2, 3])

copy_a = proto_a.clone()
copy_b = proto_b.clone()

print(f"Copy A: {copy_a.value}")
print(f"Copy B: {copy_b.data} ")