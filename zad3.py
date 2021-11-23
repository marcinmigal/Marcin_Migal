class Property:

    def __init__(self, area:str, rooms:int, price:float, address:str):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address


class House(Property):

    def __init__(self, area: str, rooms: int, price: float, address: str, plot:int):
        super().__init__(area, rooms, price, address)
        self.plot = plot
    def __str__(self) -> str:
        return f'House located in {self.area} area with {self.rooms} rooms, property size: {self.plot}. Price: {self.price}, Address: {self.address}'



class Flat(Property):
    def __init__(self, area: str, rooms: int, price: float, address: str, floor:str):
        super().__init__(area, rooms, price, address)
        self.floor = floor
    
    def __str__(self) -> str:
        return f'Flat located in {self.area} area with {self.rooms} rooms, placed at level {self.floor}. Price: {self.price}, Address: {self.address}'

house_1 = House('Central', 7, 920000, 'Main Street 12/45',800)
flat_1 = Flat('Central', 3, 420000, '9th Street 5/13',4)

print(house_1)
print(flat_1)