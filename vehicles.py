from abc import ABC,abstractmethod
from time import sleep
class Vehicle(ABC):
    speed = {
       "car": 30,
       "bike" : 50,
       "cng"  : 15
          }
    def __init__(self,vehicle_type, license_plat,rate, driver ) -> None:
        self.vehicle_type = vehicle_type
        self.rate = rate
        self.driver = driver
        self.license_plat = license_plat
        self.status = 'available'
        self.speed = self.speed[vehicle_type] 

    @abstractmethod
    def start_driving(self):
        print("Phitron")
    
    @abstractmethod
    def trip_finished(self):
        pass

class Car(Vehicle):
    def __init__(self, vehicle_type,license_plat,rate, driver) -> None:
        super().__init__(vehicle_type,license_plat,rate, driver)

    def start_driving(self,start, destination):
        self.status = 'unavailable'
        print(self.vehicle_type, self.license_plat,'started')
        distance = abs(start - destination)
        for i in range(0, distance):
            sleep(0.5)
            print(f'Driving: {self.license_plat} current position: {i} of {distance}\n')
        self.trip_finished()
    
 


    def trip_finished(self):
        self.status = 'available'
        print(self.vehicle_type,self.license_plat,'completed trip')



class Bike(Vehicle):
    def __init__(self, vehicle_type,license_plat,rate, driver) -> None:
        super().__init__(vehicle_type,license_plat,rate, driver)

    def start_driving(self,start, destination):
        self.status = 'unavailable'
        print(self.vehicle_type, self.license_plat,'started')
        distance = abs(start - destination)
        for i in range(0, distance):
            sleep(0.5)
            print(f'Driving: {self.license_plat} current position: {i} of {distance}\n')
        self.trip_finished()
    
    def trip_finished(self):
        self.status = 'available'
        print(self.vehicle_type,self.license_plat,'completed trip')
class Cng(Vehicle):
    def __init__(self, vehicle_type,license_plat,rate, driver) -> None:
        super().__init__(vehicle_type,license_plat,rate, driver)

    def start_driving(self,start, destination):
        self.status = 'unavailable'
        print(self.vehicle_type, self.license_plat,'started')
        distance = abs(start - destination)
        for i in range(0, distance):
            sleep(0.5)
            print(f'Driving: {self.license_plat} current position: {i} of {distance}\n')
        self.trip_finished()
    
    def trip_finished(self):
        self.status = 'available'
        print(self.vehicle_type,self.license_plat,'completed trip')

        


















 