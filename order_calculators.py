from abc import ABC, abstractmethod
from base_model import OrderAmount as OrderAmount
from base_enums import OrderItemSize
from custom_exceptions import InvalidOrderItemSize
# created abstract order calculator, which implements IOrderCalculator abstract
class AbstractOrderCalculator(ABC):
    
    def calculate_total_order_amount(self, order):
        order_items = order.get_order_items()
        total_order_amount = 0.0
        for order_item in order_items:
            total_order_amount += self.calculate_order_item_price(order_item)

        return total_order_amount

    def calculate_order_item_price(self, order_item):
        size_rate_amount = self._get_size_rate_amount(order_item.get_order_item_size())
        product = order_item.get_product()
        total_order_item_price_single = product.get_price() * size_rate_amount
        order_item.set_order_item_price(total_order_item_price_single)

        return total_order_item_price_single * order_item.get_quantity()

        #if(order_item.get_quantity() == 0):
        #raise ValueError("Invalid order item quantity")
    
    # created a method provided by abstract class for all sub-classes
    def get_vat_rate(self, decimal):
        if decimal == True:
            return self._get_vat_rate()
        else:
            return self._get_vat_rate() * 100
 
    def calculate_total_order_amount_vat(self, total_order_amount):
            return total_order_amount * self._get_vat_rate()
        
    # call the method to calculate the total order amount from object of OrderClaculator by providing order as a parameter
    def calculate_order_amount(self, order): 
        total_order_amount = self.calculate_total_order_amount(order)
        
        # calculate also the VAT amount and add the total order amount with VAT as an own variable
        total_order_amount_vat = self.calculate_total_order_amount_vat(total_order_amount)
        total_order_amount_with_vat = total_order_amount + total_order_amount_vat

        order_amount = OrderAmount(total_order_amount, total_order_amount_vat, total_order_amount_with_vat)

        return order_amount

    # created an abstract method implementation to caclculate VAT of total order amount
    @abstractmethod        
    def _get_vat_rate(self):
        pass

    @abstractmethod        
    def _get_size_rate_amount(self, order_item_size):
        pass
 
 # created new class, which extends AbstractOrderCalculator
class OrderCalculatorKS (AbstractOrderCalculator):
    
    # defined constant variable for VAT rate
    def __init__(self):
        self.__VAT_RATE = 0.18

    def _get_vat_rate(self):
        return self.__VAT_RATE
 
    def _get_size_rate_amount(self, order_item_size):
        match order_item_size:
            case OrderItemSize.SMALL:
                return 0.7
            case OrderItemSize.MEDIUM:
                return 1
            case OrderItemSize.LARGE:
                return 1.2
            case OrderItemSize.XXL:
                return 1.25
            case _:
                raise InvalidOrderItemSize("No Valid order item size: " + order_item_size)
                return 1

# created new class, which class implements the AbstractOrderCalculator
class OrderCalculatorGER (AbstractOrderCalculator):

    # defined variable for VAT rate as final constant
    __VAT_RATE = 0.19
 
    def _get_vat_rate(self):
                return self.__VAT_RATE

    def _get_size_rate_amount(self, order_item_size):
        match order_item_size:
            case OrderItemSize.SMALL:
                return 0.8
            case OrderItemSize.MEDIUM:
                return 1
            case OrderItemSize.LARGE:
                return 1.25
            case OrderItemSize.XXL:
                return 1.3
            case _:
                raise InvalidOrderItemSize("No Valid order item size: " + order_item_size)
                return 1