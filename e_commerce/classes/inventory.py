import sqlite3
import database.db_functions.select as select

class Inventory:
    

    def increase_inv_item(item_id: str, item_quantity: int):
        
        try:
            query = "UPDATE inventory SET item_quantity = item_quantity + {item_quantity} WHERE item_id = '{item_id}'"
            select.selector(query)
            return True
        except:
            return False

    def decrease_inv_item(self, item_id: str, item_quantity: int):

        try:
            query = "UPDATE inventory SET item_quantity = item_quantity - {item_quantity} WHERE item_id = '{item_id}'"
            select.selector(query)
            return True
        except:
            return False

    def view_item_category(self, item_category: str):
        
        query = "SELECT * FROM inventory WHERE item_category = '{item_category}'"
        result = selector(query)
       

        if result:
             for data in result:
                print(data)
        else:
            print("No items found in that category")

    