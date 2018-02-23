# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 13:43:33 2018

@author: tance
"""


class MenuItem:
    def __init__(self, name, price, picAddress, description, ingredients):
    
        self.__name = name
        
        if float(price) > 0.00:
            self.__price = float(price)
        else:
            self.__price = 0.00
            
        self.__picAddress = picAddress
        
        self.__description = description
        
        #self._ingredients.append(ingredients)
        self.__ingredients = ingredients
        
        # This needs to see if all ingredients are available and then determine if it is available
        if 1 == 1:
            self.__available = True
            
    __available = True  # This variable will be set to True when the object is created
                       # but will be correctly set once compared to avariablility of the
                       # ingredients needed depending on their quantity.
                       
    __picAddress = 'There is no Address'
    __description = 'This is a MenuItem'
                       
    #_ingredients = []
        
    #
    def setName(self, name):
        self.__name = name
        
    #
    def getName(self):
        return self.__name
    
    # It will set the price of the dish.  If the input is negative the price will
    # be set to $0.00.
    def setPrice(self, price):
        if float(price) > 0.00:
            self.__price = float(price)
        else:
            self.__price = 0.00
    
    #    
    def getPrice(self):
        return str(self.__price)
    
    #
    def setPic(self, picAddress):
        self.__picAddress = picAddress
    
    #    
    def getPic(self):
        return self.__picAddress
    
    #
    def setDescription(self, description):
        self.__description = description
        
    # 
    def getDescription(self):
        return self.__description
    
    # Allows you to add an ingredient to the list of ingredients.
    def addIngredient(self, ingredient):
        self.__ingredients += (', ' + ingredient)
        
    # Prints all of the things listed in the ingredients list.
    #def printIngredients(self):
     #   for n in range(len(_ingredients)):
      #      list += str(_ingredients[n])
       # return list    
        
        
    # 
    def getIngredients(self):
        return self.__ingredients
    
    # Prints out if the Dish is Available or not.  Prints nothing if available and
    # prints --OUT-- if it is out.
    def getAvailable(self):
        if self.__available == True:
            return ''
        else:
            return '--OUT--'
        
    def setAvailable(self, avail):
        self.__available
    
    # Prints out the values stored in the object.
    def printDish(self):
        print(self.getName() + ':' + self.getAvailable() + ' $' + self.getPrice() + '\n\t' + self.getPic() + '  ' + self.getDescription() + '\n\t-> ' + self.getIngredients())
        
    
class Supply:
    def __init__(self, name, quantity, decAmount, measurement):
        self.__name = name
        self.__quantity = quantity
        self.__decAmount = decAmount
        self.__measurement = measurement
        
    __decAmount = 1.0
    __quantity = 0.0
    __measurement = 'oz'
        
    def setName(self, name):
        self.__name = name
        
    def getName(self):
        return self.__name
    
    def setQuantity(self, quantity):
        self.__quantity = quantity
        
    # This will decrement the quantity of the supply by the decrement amount
    # specificied in the class. Ex:  it has 4 lbs and decrements by 1 lb.  This
    # will then set the quantity to be 3.
    def useQuantity(self):
        if (self.__quantity - self.__decAmount) < 0.00:
            self.__quantity = 0.00
        else:
            self.__quantity -= self.__decAmount
            
    def getQuantity(self):
        return self.__quantity
    
    def setDecAmount(self, decAmount):
        self.__decAmount = decAmount
        
    def getDecAmount(self):
        return self.__decAmount
    
    def setMeasurement(self, measurement):
        self.__measurement = measurement
        
    def getMeasurement(self):
        return self.__measurement
    
    def printSupply(self):
        print(self.getName() + ': ' + str(self.getQuantity()) + ' ' + self.getMeasurement())
        

# This is a Menu that contains MenuItems.  
# ?????SHOULD THIS HAVE A NAME VARIABLE SO WE CAN THEN HAVE DIFFERENT MENUS?????
class Menu:
    def __init__(self):
       return
        
    __items = []
    
    # Adds the first item into the list.  Afterwards it then alphabetizes the
    # items as they are put into the list.
    def addItem(self, item):
        if len(self.__items) == 0:
            self.__items.append(item)
            return
        else:
            for i in range(0, len(self.__items)):
                if item < self.__items[i]:
                    self.__items.insert(i, item)
                    return
                # If it goes through all of the list and still hasn't been added
                # it will be added here.
                elif i+1 >= len(self.__items):
                    self.__items.append(item)
                    return
                
        
    def popItems(self):
        for i in range(0, len(self.__items)):
            print(self.__items.pop())
        
        
    
    