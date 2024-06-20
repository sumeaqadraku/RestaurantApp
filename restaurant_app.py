from base_model import Restaurant, Client, Menu
from order_utils import OrderPrinter, OrderManager
from menu_utils import MenuPrinter, MenuImporter
from location_utils import LocationManager
from calculator_utils import OrderCalculatorFactory
from base_enums import Location, ApplicationMode
from application_utils import ApplicationModeManager

class RestaurantApp:
#Select location:
#1. KOSOVO
#2. GERMANY

   # created new attribute for current location
    def __init__(self):
        self.__current_location = None
        #created new attribute file_path
        self.__file_path = 'menu-list.csv'
        
    def start(self):
        
        self.__current_location = self.get_current_location()
        application_mode = self.get_application_mode()
        self.execute_application_mode(application_mode)
        
        
    def execute_application_mode(self, application_mode):
        match application_mode:
            case ApplicationMode.ORDER:
                self.run_order_process()
                return
            case ApplicationMode.TABLE_RESERVATION:
                self.run_table_reservation_process()
                return
            case _:
               #switched from normal print to raise exception 
                raise Exception("No valid application mode selected!")
              
                
    #new method to get current location
    def get_current_location(self):
        print("Please select the location (type number):")
        
        # for each Location literal of enum Location, print every option
        location_options = "".join([str(location_option.value) + ". " + location_option.name + "\n" for location_option in Location])  
        print(location_options) 

    #get input from user
        location_id_input = input()
        location_id = int(location_id_input)
    
        location = LocationManager.get_location_from_id(location_id)
        return location
    
    def get_application_mode(self):
        print("Please select an application mode (type number):")
        
        application_mode_options = ''.join([str(app_mode.value) + '. ' + app_mode.name + '\n' for app_mode in ApplicationMode])
        print(application_mode_options)
        
        application_mode_input = input()
        application_mode_id = int(application_mode_input)
        
        application_mode = ApplicationModeManager.get_application_mode_from_id(application_mode_id)
        
        return application_mode 
 
    
    def run_order_process(self):
        restaurant = Restaurant("Ora", "Rruga e Sallave")
        client = Client("Sumea Qadraku", "+38343123456") 

        menu_importer = MenuImporter()
        menu = menu_importer.import_menu(self.__file_path)
        menu_printer = MenuPrinter()
        menu_printer.print_menu(menu)

        order_manager = OrderManager()

        order = order_manager.create_order(menu)
        order_manager.get_orders().append(order)
        
        #printing new info from new files
        self.__calculate_and_print_order_details(restaurant, client, order)

    def __calculate_and_print_order_details(self, restaurant, client, order):
        order_calculator = self.get_order_calculator()
        order_amount = order_calculator.calculate_order_amount(order)
        
        order_printer = OrderPrinter()
        order_printer.print_order_info(restaurant, client, order, order_amount, order_calculator.get_vat_rate(False))

    def get_order_calculator(self):
        return OrderCalculatorFactory.get_order_calculator_by_location(self.__current_location)

    def run_table_reservation_process(self):
       print("Table reservation completed successfully.")


restaurantApp = RestaurantApp()
restaurantApp.start()