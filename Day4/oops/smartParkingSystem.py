from abc import ABC, abstractmethod
from collections import defaultdict
import sys
class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass
class CashPayment(Payment):
    def process_payment(self, amount):
        print(f"Payment successful: ₹{amount} paid via cash")
class CardPayment(Payment):
    def process_payment(self, amount):
        print(f"Payment successful: ₹{amount} paid via credit/debit card")
class UPIPayment(Payment):
    def process_payment(self, amount):
        print(f"Payment successful: ₹{amount} paid via UPI")
class Vehicle(ABC):
    def __init__(self, vehicle_id, license_plate, owner_name):
        self.vehicle_id = vehicle_id
        self.__license_plate = license_plate
        self.__owner_name = owner_name
        self.license_plate = license_plate  
    @abstractmethod
    def calculate_parking_fee(self):
        pass
    def get_license(self):
        return self.__license_plate
    def get_owner_name(self):
        return self.__owner_name
    def display(self):
        return f"ID: {self.vehicle_id}, Plate: {self.__license_plate}, Owner: {self.__owner_name}"
class Bike(Vehicle):
    def __init__(self, vehicle_id, license_plate, owner_name, helmet_required):
        super().__init__(vehicle_id, license_plate, owner_name)
        self.helmet_required = helmet_required
        self.vechile_type = 'Bike'
    def calculate_parking_fee(self):
        return 30
    def __str__(self):
        return f"{self.vechile_type} → {self.display()}"
class Car(Vehicle):
    def __init__(self, vehicle_id, license_plate, owner_name, seats):
        super().__init__(vehicle_id, license_plate, owner_name)
        self.seats = seats
        self.vechile_type = 'Car'
    def calculate_parking_fee(self):
        return 50
    def __str__(self):
        return f"{self.vechile_type} → {self.display()}"
class SUV(Vehicle):
    def __init__(self, vehicle_id, license_plate, owner_name, four_wheel_drive):
        super().__init__(vehicle_id, license_plate, owner_name)
        self.four_wheel_drive = four_wheel_drive
        self.vechile_type = 'SUV'
    def calculate_parking_fee(self):
        return 70   
    def __str__(self):
        return f"{self.vechile_type} → {self.display()}"
class Truck(Vehicle):
    def __init__(self, vehicle_id, license_plate, owner_name, max_load_capacity):
        super().__init__(vehicle_id, license_plate, owner_name)
        self.max_load_capacity = max_load_capacity
        self.vechile_type = 'Truck'
    def calculate_parking_fee(self):
        return 100 
    def __str__(self):
        return f"{self.vechile_type}→ {self.display()}"
class Parkingspot:
    def __init__(self, spot, size):
        self.spot = spot
        self.size = size
        self.occupied = False
        self.vechile = None
    def __hash__(self):
        return hash((self.spot, self.size))
    def __lt__(self, other):
        return self.spot < other.spot
    def assign_vechile(self, vechile):
        if not self.occupied:
            self.vechile = vechile
            self.occupied = True
        else:
            print('Cannot assign vehicle, already occupied')
    def remove_vechile(self):
        self.occupied = False
        self.vechile = None
class Parkinglot:
    dic = {
        'Bike': ['S', 'M', 'L', 'XL'],
        'Car': ['M', 'L', 'XL'],
        'SUV': ['L', 'XL'],
        'Truck': ['XL']
    }
    def __init__(self, lot_name):
        self.lot_name = lot_name
        self.list_parkingspots = set()
        self.dic1 = defaultdict(int)
        print(f"Parking Lot Created: {lot_name}")
    def add_spot(self, parkingspot):
        if parkingspot in self.list_parkingspots:
            print("Spot is already present")
        else:
            self.list_parkingspots.add(parkingspot)
            self.dic1[parkingspot.size] += 1
    def show_spots(self):
        """Shows the status of all parking spots."""
        arr1 = sorted(self.list_parkingspots)
        print("\nParking Status:")
        for i in arr1:
            if not i.occupied:
                print(f"Spot {i.spot} ({i.size}): Empty")
            else:
                print(f"Spot {i.spot} ({i.size}): Occupied → {i.vechile.vechile_type} ({i.vechile.license_plate})")
    def park_vehicle(self, vechile):
        arr1 = sorted(self.list_parkingspots)
        for size in Parkinglot.dic[vechile.vechile_type]:
            if self.dic1[size] > 0:
                for i in arr1:
                    if not i.occupied and i.size == size:
                        print(f"{vechile.vechile_type} ({vechile.license_plate}) parked successfully at Spot {i.spot} ({i.size})")
                        self.dic1[size] -= 1
                        i.assign_vechile(vechile)
                        return
        print("Parking place is not available")
    def unpark_vehicle(self, vechile, hours):
        arr1 = list(self.list_parkingspots)
        for i in arr1:
            if i.vechile == vechile:
                fee = vechile.calculate_parking_fee() * hours
                print(f"\n{vechile.vechile_type} ({vechile.license_plate}) removed from Spot {i.spot}")
                print(f"Parking Fee for {hours} hours = ₹{fee}")
                print("Select Payment Method: 1. Cash 2. Card 3. UPI")
                choice = "1"
                
                if choice == "1":
                    payment = CashPayment()
                elif choice == "2":
                    payment = CardPayment()
                elif choice == "3":
                    payment = UPIPayment()
                else:
                    print("Invalid choice, defaulting to Cash")
                    payment = CashPayment()
                payment.process_payment(fee)
                i.remove_vechile()
                self.dic1[i.size] += 1
                return
        print("Vehicle is not parked")
print(" Step 1: Create Parking Lot and Spots")
lot = Parkinglot("CityMall Parking")
lot.add_spot(Parkingspot(1, "S"))
lot.add_spot(Parkingspot(2, "M"))
lot.add_spot(Parkingspot(3, "M"))
lot.add_spot(Parkingspot(4, "L"))
lot.add_spot(Parkingspot(5, "XL"))
print(f"Total Spots Added: {len(lot.list_parkingspots)}")
print("\n Step 2: Create Vehicles")
bike1 = Bike("B101", "TS01AB1234", "Rahul", True)
car1 = Car("C201", "TS05CD5678", "Priya", 5)
suv1 = SUV("S301", "TS09EF9012", "Anjali", True)
truck1 = Truck("T401", "TS11XY4455", "Ravi", 12)
print("Vehicles Created:")
print(f"Bike  → {bike1.display()}")
print(f"Car   → {car1.display()}")
print(f"SUV   → {suv1.display()}")
print(f"Truck → {truck1.display()}")
print("\n Step 3: Park Vehicles")
lot.park_vehicle(bike1)
lot.park_vehicle(car1)
lot.park_vehicle(suv1)
lot.park_vehicle(truck1)
lot.show_spots()
print("\n Step 4: Unpark a Vehicle + Payment")
lot.unpark_vehicle(car1, hours=3)
print("\n Step 5: Final Status")
lot.show_spots()
