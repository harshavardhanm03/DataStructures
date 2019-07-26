# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 23:01:55 2019

@author: harsh
"""

class ParkingLot:
    def disployBoard(self):
        pass
    
    
        
        
        
        
        


class Vehicle:
    counter=1000
    def __init__(self,vechicletype):
        self.vechicletype=vechicletype
        Vehicle.counter=Vehicle.counter+1
        
    
    @staticmethod
    def assignTicket(self):   
        return self.vechicletype[0]+str(Vehicle.counter)
    
    b=Billing()
    

class Car(Vehicle):
    #hourlrate_car=3
    def __init__(self,vechicletype,carType,city):
        super().__init__(vechicletype)
        self.carType=carType
        self.city=city
    
    def Cartype(self):
        return self.carType+""+self.city
    
    p1=ParkingLot()
    
    



class Billing:
    d={"car":3,"truck":6,"bike":9}
    def input_customer():
        payment=input("Which type of pyament you want made, Enter m for money, c for card")
        if(payment_type=='c'):
            return "Attendant"
        else:
            return "please insert card"
        
    def billingCustomer(self,vehiceltype,number_of_hours):
        bill=d[vehiceltype]*number_of_hours
        return bill
    
    

car=Car("V-6 Enginer","Benz","LosAngels")
print(car.assignTicket(car))
print(car.Cartype())
        
        
vehicle=Vehicle("car LA123")
vehicle.assignTicket(vehicle)
vehicle=Vehicle("bike 123")
vehicle.assignTicket(vehicle)
        
        
        


class Vehicle:
    @static