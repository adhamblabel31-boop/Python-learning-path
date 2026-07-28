# ----------------------------------------------------
# ! ----------------- polymorphism -------------------
# ----------------------------------------------------

print(len("Adham"))
print(len([1, 2, 3, 4, 5]))
print(len({"adham": 1, "Adham": 2}))
# one function do diffrect tasks


class A:
    def thing(self):
        print("Adham in class A")
        raise NotImplementedError("derived classes must implement this method")


class B(A):
    def thing(self):
        print("Adham in class B")


class C(A):
    def thing(self):
        print("Adham in class C")


# one = A()
# one.thing() error

two = B()
two.thing()

thr = C()
thr.thing()
