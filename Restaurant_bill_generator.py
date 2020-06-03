# Coded by Yashowardhan Shinde FC059
# Object oriented program
# Restaurant Bill Generator
''' 
To run this program you will have to download the menu.txt file as well,
as data is being extracted from this file while running this program.
'''

# Getting the restaurant menu from the Data file
menu = []
menu_item = open('menu.txt', 'r')
for line in menu_item.readlines():
    x = list(line.split('  '))
    menu.append(x)

# Taking the information of the customer
name = input('Enter your name : ')
number = int(input('Enter your Mobile Number: '))

# Printing the menu so that the customer will be able to select The items they want
print(f'''
Hi {name} Welcome to Our Restaurant!!
Here is the menu of Our Restaurant:
SNACKS :
Sr Items                     Price
1  French Fries               106 Rs.
2  Chili Cheese Toast         115 Rs.
3  Chili Cheese Garlic Toast  115 Rs.
4  Garlic Bread               98 Rs.
5  Garlic Bread with Cheese   119 Rs.

SANDWICH :
6  Plain Sandwich             175 Rs.
7  Grilled Sandwich           175 Rs.
8  Club Sandwich              175 Rs.

MAIN COURSE :
9  Tandoori Paneer Tikka      220 Rs.
10  Malai Paneer Tikka 	      220 Rs.
11  Soya Tandoori Tikka       175 Rs.
12  Tandoori Aloo             179 Rs.
13  Punjabi Soya Chap         179 Rs.

KEBAB and PLATTERS :
14  Hare-Bhara Kebab          162 Rs.
15  Paneer ke Kebab           179 Rs.
16  Veg Platter               325 Rs.

SOUTH INDIAN :
17  Dosa (Butter)             125 Rs.
18  Onion Dosa (Butter)       136 Rs.
19  Paper Dosa                130 Rs.
20  Mysore Dosa               123 Rs.
21  Rawa Dosa 	              119 Rs.
22  Onion Rawa Dosa           136 Rs.

INDIAN GRAVY :
23  Shahi Paneer              210 Rs.
24  Kadhai Paneer             210 Rs.
25  Paneer Butter Masala      210 Rs.
26  Mushroom Masala           215 Rs.

INDIAN BREAD :
27  Roti                      20  Rs.
28  Naan                      40  Rs.
29  Butter Roti               30  Rs.
30  Butter Naan               50  Rs.
''')

# Taking order from customer
bill_items = input(f'{name} Enter the code of items you want to order leaving space between them : ').split()
quantity = list(map(int, input(f'{name} Now Enter the quantity of each item u want to order : ').split()))


# Declaration of a class Restaurant
class Restaurant:
    # initialising variables
    def __init__(self, menu, bill_items, quantity):
        self.menu = menu
        self.bill_items = bill_items
        self.quantity = quantity

    # Collecting Names of all food items
    def bill_item_food(self):
        food = []
        for i in self.bill_items:
            for j in range(len(self.menu)):
                if i == menu[j][0]:
                    food.append(self.menu[j][1])
        return food

    # Collecting the prices of ech dish ordered
    def bill_item_prices(self):
        price = []
        for i in self.bill_items:
            for j in range(len(self.menu)):
                if i == menu[j][0]:
                    price.append(int(self.menu[j][2]))
        return price

    # Finding out the total bill without gst
    def bill_total(self):
        total = 0
        obj = Restaurant(menu, bill_items, quantity)
        for i in range(len(self.bill_items)):
            total += obj.bill_item_prices()[i]*self.quantity[i]
        return total

    # Printing The final Bill using all data available
    def bill_structure(self):
        object1 = Restaurant(menu, bill_items, quantity)
        gst = object1.bill_total()*0.05
        final_bill = []
        for k in range(len(self.bill_items)):
            final_bill.append([object1.bill_item_food()[k], self.quantity[k], object1.bill_item_prices()[k]])
        print(f'''
Here you go {name} This is your bill:
Item                    Quantity   Price in Rs.''')
        for i in final_bill:
            print(str(i[0]).ljust(27), str(i[1]).ljust(9), i[1]*i[2])
        print('Total :', object1.bill_total())
        print(f'CGST on total bill is 5%: {gst}')
        print(f'SGST on total bill is 5%: {gst}')
        print('Total Due Amount:', object1.bill_total()+(gst*2))
        print('ThankYou for Visiting!!!')

    # Saving The customer details like name and mobile number which will help in future marketing
    def customer_info(self):
        customer_data = open('customer_data.txt', 'a')
        customer_data.write(f'Customer Name: {name} \nCustomer Mobile Number: {number} \n \n')


# Removing the items which do not exist in the menu which have been accidentally entered by the user
m = [bill_items.index(_) for _ in bill_items if int(_) > 30]
bill_items = [d for d in bill_items if int(d) <= 30]
for o in m:
    quantity[o] = 0
quantity = [b for b in quantity if b != 0]

# Cross checking for any errors and proceeding for the function calling
if len(quantity) != len(bill_items):
    print('The number of items do not match number of quantities ')
    print('Please Enter your order again')
else:
    x = Restaurant(menu, bill_items, quantity)
    x.bill_structure()
    x.customer_info()
 
