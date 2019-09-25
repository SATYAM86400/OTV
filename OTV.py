"""This is the program of Online Ticket Vending System.
Which is developed and maintained by SATYAM."""

import datetime


#The first page:-

print("\t\t\t********************************************************************************")
print("\n\n")
print("\t\t\t\t\t\t\tWELCOME\n\n\n\t\t\t\t\t\t\t  TO\n\n\n\t\t\t\t\t\t\t  OTV")
print("\n\n\n\n")

input("Press Enter to Continue...")

print("\n\n\n\n")


#The second page:-

name = str(input("\t\t\t\t\t\tEnter your Name : "))
print("\n")
phone = int(input("\t\t\t\t\t\tEnter your Phone number : "))



print("\n\n\n\n")


input("Press Enter to Continue...")

print("\n\n\n")


#The third page:-


print("\n\t\t\t\t\t\tENTER DETAILS BELOW :- \n\n\n")


class Start:
    def __init__(self, location):
        self.__location = location

    def set_location(self,value):
        self.__location = value

    def get_location(self):
        return self.__location



from1 = Start("Not Selected.")

from1.set_location(input("\t\t\t\t\t\tEnter the starting location : "))

location = from1.get_location()

print("\n")        

class Dest:
    def __init__(self, destination):
        self.__destination = destination

    def set_destination(self,value):
        self.__destination = value

    def get_destination(self):
        return self.__destination


to1 = Dest("Not Selected.")

to1.set_destination(input("\t\t\t\t\t\tEnter the destination : "))

destination = to1.get_destination()


date = datetime.datetime.today()

print("\n\n\n\n")

input("Press Enter to Continue...")

print("\n\n\n")



#the fourth page:-

print("\t\t\t\t\t\tCHOOSE THE BUS :-\n\n")
print("\t\t\t\t\t\t1.  534  Anand Vihar Terminal")
print("\t\t\t\t\t\t2.  874  Connaught Place")
print("\t\t\t\t\t\t3.  473  Badarpur Border")
print("\t\t\t\t\t\t4.  348  Mayur Vihar - 2")
print("\t\t\t\t\t\t5.  448  Rajendra Palace")
print("\t\t\t\t\t\t6.  085  Punjabi Bagh")
print("\t\t\t\t\t\t7.  079  Saket")
print("\t\t\t\t\t\t8.  770  Tugalkabad")
print("\t\t\t\t\t\t9.  678  Mehrauli")
print("\t\t\t\t\t\t10. 002  India Gate")

bus_no = int(input("\n\n\t\t\t\t\t\tEnter the bus number : "))

print("\n\n\n\n")

input("Press Enter to Continue...")

print("\n\n\n")


#the fifth page:-

print("\t\t\t\t\t\t  YOU CHOOSE :-\n\n")
print("\t\t\t\t\tJourney from " + location + " to " + destination + "\n")
print("\t\t\t\t\t\tTotal Fare = 10 Rupees.")


print("\n\n\n\n")

input("Press Enter to Continue...")

print("\n\n\n")

#the sixth page:-


print("\t\t\t\t\t\tPAYMENT OPTIONS:-\n\n")
print("\t\t\t\t\t\t1. Paytm")
print("\t\t\t\t\t\t2. Amazon Pay")
print("\t\t\t\t\t\t3. Netbanking")
print("\t\t\t\t\t\t4. Credit/Debit Card")
print("\t\t\t\t\t\t5. Google Pay")
print("\t\t\t\t\t\t6. PhonePe")


payment = input("\n\n\t\t\t\t\t\tEnter the payment option : ")


print("\n\n\n\n")

input("Press Enter to Continue...")

print("\n\n\n")

#the seventh page:-


print("\t\t\t\t\t\t TO THE PAYMENT GATEWAY.....")

print("\n\n\n\n")

input("Press Enter to Continue...")

print("\n\n\n")


#the eight page:-


print("\t\t\t\t\t\t PAYMENT WAS SUCCESSFUL.....")

print("\n\n\n\n")

input("Press Enter to Continue...")

print("\n\n\n")

#the ninth page

print("\t\t\t\t\t\tYOUR E-TICKET :-\n\n")
print("\t\t\t\t\t\tName    :  " + name)
print("\t\t\t\t\t\tFrom    :  " + location)
print("\t\t\t\t\t\tTo      :  " + destination)
print("\t\t\t\t\t\tBus no  :  " + str(bus_no))
print("\t\t\t\t\t\tDate    :  " + str(date))
print("\t\t\t\t\t\tPayment :  " + payment)
print("\n\n\t\t\t\t\t\tQR CODE :-  \n")

print("\n\n\n\n")

input("Press Enter to Continue...")

print("\n\n\n")

#the final page


input("Thank You for using this software...\nPress enter to exit.")
