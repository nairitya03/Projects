class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def info(self):
        return self.name + ': $' + str(self.price)

    def get_total_price(self, count):
        total_price = self.price * count
        
        
        if count >= 3:
            total_price = total_price * 0.9
        
       
          
        return round(total_price)

menu_item1 = MenuItem('Sandwich', 5)
menu_item2 = MenuItem('Chocolate Cake', 4)
menu_item3 = MenuItem('Coffee', 3)
menu_item4 = MenuItem('Orange Juice', 2)

menu_items = [menu_item1, menu_item2, menu_item3, menu_item4]

index = 0

for menu_item in menu_items:
    print(str(index) + '. ' + menu_item.info())
    index += 1

print('-------------------------------------------------')

order = int(input('Enter menu item number: '))
selected_menu = menu_items[order]
print('Selected item: ' + selected_menu.name)


count = int(input ("Enter quantity (10% off for 3 or more): "))

result =selected_menu.get_total_price(count)


print('Your total is $'+str(result))
