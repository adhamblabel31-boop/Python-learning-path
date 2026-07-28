# ----------------------------------------------------
# ! ------------------ inheritance -------------------
# ----------------------------------------------------


class Name:  # base class
    def __init__(self, name, price, mode):
        self.name = name
        self.price = price
        self.mode = mode
        print(f"{self.name} in base class")
        print(f"mode is {self.mode}")
        print("Adham in base class")

    def study(self):
        print("Adham studys in base class")


class adham(Name):  # derived class
    def __init__(self, name, price, mode):
        # Name.__init__(self, name, price)  # created instance from base class
        super().__init__(name, price, mode)
        self.mode = mode
        print(f"{self.name} in base class")
        print(f"price is {self.price}")
        print("adham in derived class")

    def baloot(self):
        print("baloot is here")

    def study(self):
        print("Adham studys in derived class")


name1 = Name("Adham", 9999, "lazy")
name2 = adham("adham", 9999, "lazy")

# name2.study()

# name2.baloot()
