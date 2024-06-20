from enum import Enum

# create new Enum for order item sizes
class OrderItemSize(Enum):
    # enums to specify order item sizes
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    XXL = 4
    
class Location(Enum):
    KOSOVO = 1
    GERMANY = 2
    
class ApplicationMode(Enum):
    ORDER = 1
    TABLE_RESERVATION = 2  