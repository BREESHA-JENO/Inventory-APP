from datetime import date
import re

class Product:
    'Python OOps applied'
    def __init__(self,productid=None,productName=None,unitprice=None,categoryid=None,manufacturedate=None,is_active="Y"):
        self.__productid=productid
        self.__productname=None  #validating productname
        self.__unitprice=unitprice
        self.__category_id=categoryid
        self.__manufacture_date=manufacturedate if manufacturedate else date.today()
        self.__is_active=is_active

        if productName is not None:
            self.set_product_name(productName)

        #----------------------
        #GETTERS AND SETTERS
        #----------------------
    def get_product_id(self):
        return self.__productid
    def set_product_id(self,productid):
        self.__productid=productid

    def get_product_name(self):
        return self.__productname
    def set_product_name(self,productname):
        'validate product name before setting (2-30 alphabets/underscore)'
        pattern=re.compile(r"^[A-Za-z_]{2,30}$")
        while True:
            if pattern.match(productname):
                self.__productname=productname
                break
            else:
                print("\t\t Invalid product name must have only alphabets min character 3!!!....")
                productname=input("\t\t Enter Product Name again: ")

    def get_unitprice(self):
        return self.__unitprice
    def set_unitprice(self,unitprice):
        self.__unitprice=unitprice

    def get_category_id(self):
        return self.__category_id
    def set_category_id(self,categoryid):
        self.__category_id =categoryid

    def get_manufacture_date(self):
        return self.__manufacture_date
    def set_manufacture_date(self,manufacturedate):
        if isinstance(manufacturedate,date):
            self.__manufacture_date=manufacturedate
        else:
            raise ValueError("Manufacture date must be date object")

    def get_is_active(self):
        return self.__is_active
    def set_is_active(self,is_active):
        self.__is_active=is_active

    #override __str__
    def __str__(self):
        return f"Product ID:{self.__productid:<10},Product Name:{self.__productname:<20},Category ID:{self.__category_id:<10},Unit Price:{self.__unitprice:<15},Manufacture Date:{str(self.__manufacture_date) if self.__manufacture_date is not None else '':<15},Isactive:{self.__is_active:<10}"

    # def __str__(self):
    #     return (
    #         f"Product ID:{str(self.__productid) if self.__productid is not None else '':<10}, "
    #         f"Product Name:{str(self.__productname) if self.__productname is not None else '':<20}, "
    #         f"Category ID:{str(self.__category_id) if self.__category_id is not None else '':<10}, "
    #         f"Unit Price:{str(self.__unitprice) if self.__unitprice is not None else '':<15}, "
    #         f"Manufacture Date:{str(self.__manufacture_date) if self.__manufacture_date is not None else '':<15}, "
    #         f"Isactive:{str(self.__is_active) if self.__is_active is not None else '':<10}"
    #     )