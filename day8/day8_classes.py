import copy
from abc import ABC, abstractmethod
from collections import namedtuple


class Printable(ABC):
    @abstractmethod
    def printDriverName(self):
        pass

class DeliveryVan(Printable):
    def __init__(self, mileage = 0, route=[], driver=""):
        self.mileage = mileage
        self.route = route[:]
        self.driver = driver

    def clone(self):
        clonedObject = DeliveryVan(self.mileage, self.route, self.driver)
        return clonedObject

    def __add__(self, other):
        if self.driver == other.driver and isinstance(other, DeliveryVan):
            self.mileage += other.mileage
            self.route.extend(other.route)
        return self

    def __lt__(self, other):
        if isinstance(other, DeliveryVan):
            return self.mileage < other.mileage
        return False

    def __str__(self):
        return "mileage: " + str(self.mileage) + ", route: " + str(self.route) +\
            ", driver: " + self.driver

    def printDriverName(self, salutation = "Mr."):
        print(salutation + " " + self.driver)


class ElectricDeliveryVan(DeliveryVan):
    def __init__(self, mileage = 0, route=[], driver="", autonomy=0):
        # super().__init__(self, mileage, route, driver)
        DeliveryVan.__init__(self, mileage, route, driver)
        self.autonomy = autonomy

class X(Printable):
    def printDriverName(self):
        print("There is no driver name")


def main():
    deliveryVan1 = DeliveryVan(100, ["A", "B", "C"], "John")
    deliveryVan2 = copy.deepcopy(deliveryVan1)
    deliveryVan2.route.append("D")
    print(deliveryVan1.route)
    print(deliveryVan2.route)
    deliveryVan3 = deliveryVan1.clone()
    deliveryVan3.route.append("Z")
    print(deliveryVan3.route)
    print(deliveryVan1.route)
    deliveryVan4 = deliveryVan1 + deliveryVan3
    print(deliveryVan4.route)
    deliveryVan1.mileage = 100
    deliveryVan2.mileage = 150
    print(deliveryVan1 <  deliveryVan2)
    print(deliveryVan1)

    electricDeliveryVan = ElectricDeliveryVan(200, ["A", "C"],
                                              "George", 250)
    print(electricDeliveryVan)
    print(issubclass(ElectricDeliveryVan, DeliveryVan))
    electricDeliveryVan.printDriverName()
    electricDeliveryVan.printDriverName("Dr.")
    x = X()
    x.printDriverName()
    x = electricDeliveryVan
    x.printDriverName()

    Product = namedtuple("Product", ["name", "count", "price"])
    product1 = Product("iPhone", 0, 0)
    print(product1)
    product2 = Product(name="Samsung", count=2, price=3500.6)
    print(product2)


if __name__ == "__main__":
    main()
