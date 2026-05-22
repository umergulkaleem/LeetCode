class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small  =small

        self.cars_space = [big,medium,small]
        

    def addCar(self, carType: int) -> bool:
        self.carType = carType
        print(carType)
        print(self.cars_space)
        if carType == 1 and self.cars_space[0]>0:
            self.cars_space[0] -=1
            return True
        elif self.carType == 2 and self.cars_space[1]>0:
            self.cars_space[1] -=1
            return True
        elif self.carType == 3 and self.cars_space[2]>0:
            self.cars_space[2] -=1
            return True
        
        return False
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)