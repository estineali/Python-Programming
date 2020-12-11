name = input('Your name please \n')
print('Welcome to the virtual store,', name +'!')


def mainmenu():
    x = open('mainmenu.txt')
    menu = x.read()
    print(menu)
def bakery():
    x = open('bakery.txt')
    baked = x.read()
    print(baked)
def fruits():
    x = open('fruits.txt')
    froot = x.read()
    print(froot)
def meat():
    x = open('meat.txt')
    meet = x.read()
    print(meet)
def drinks():
    x = open('drinks.txt')
    drunk = x.read()
    print(drunk)
def frozenitems():
    x = open('frozenitems.txt')
    mrfreez = x.read()
    print(mrfreez)
def buymenu(MENU):
    x = open(MENU)
    listed = []
    for i in x:
        a = i.strip()
        listed.append(a)
    listed = listed[3:]
    clean = [None]
    for i in listed:
        a = i.split()
        a.remove('Rs.')
        clean.append(a[1:])
    return clean
def modify_cart(cart):
    print()
    print('Press 1 to change quantity')
    print('Press 2 to remove')
    choice = int(input())
    while choice != 1 and choice != 2:
        print('invalid choice. choose again')
        choice = int(input())
    if choice == 1:
        for i in range(len(cart)):
            print(i+1, cart[i][0], cart[i][1], cart[i][2], cart[i][3])
        s = int(input('which item do you want to change the quantity of? (enter serial no.) \n'))
        q = int(input('New quantity?\n'))
        if q == 0:
            cart.pop(s-1)
        else:
            cart[s-1][2] = 'x' + str(q)
            cart[s-1][3] = int(cart[s-1][1])*q
        return cart
    else:
        for i in range(len(cart)):
            print(i + 1, cart[i][0], cart[i][1], cart[i][2], cart[i][3])
        s = int(input('which item do you want to remove? (enter serial no.) \n'))
        cart.pop(s-1)
        return cart

def shop():
    mainmenu()
    sec = input('Choose a section(number):\n')
    while len(sec) > 1 or not 49<=ord(sec)<=53:
        print('Error: invalid selection')
        sec = input('Choose a section(number):\n')
    cart = []
    want = True
    while want == True:
        if sec == '1':
            bakery()
            items = buymenu('bakery.txt')
            sub = int(input('Choose an item(number) or press 0 to exit this menu:\n'))
            while sub > len(items)-1:
                print('invalid selection')
                sub = int(input('Choose an item(number) or press 0 to exit this menu:\n'))
            if sub > 0:
                qty = int(input('How many?\n'))
                cart.append([items[sub][0], items[sub][1], 'x'+str(qty), qty*int(items[sub][1])])
        elif sec == '2':
            fruits()
            items = buymenu('fruits.txt')
            sub = int(input('Choose an item(number) or press 0 to exit this menu:\n'))
            while sub > len(items) - 1:
                print('invalid selection')
                sub = int(input('Choose an item(number) or press 0 to exit this menu:\n'))
            if sub > 0:
                qty = int(input('How many?\n'))
                cart.append([items[sub][0], items[sub][1], 'x'+str(qty), qty*int(items[sub][1])])
        elif sec == '3':
            meat()
            items = buymenu('meat.txt')
            sub = int(input('Choose an item(number) or press 0 to exit this menu:\n'))
            while sub > len(items) - 1:
                print('invalid selection')
                sub = int(input('Choose an item(number) or press 0 to exit this menu:\n'))
            if sub > 0:
                qty = int(input('How many?\n'))
                cart.append([items[sub][0], items[sub][1], 'x'+str(qty), qty*int(items[sub][1])])
        elif sec == '4':
            drinks()
            items = buymenu('drinks.txt')
            sub = int(input('Choose an item(number) or press 0 to exit this menu:\n'))
            while sub > len(items) - 1:
                print('invalid selection')
                sub = int(input('Choose an item(number) or press 0 to exit this menu:\n'))
            if sub > 0:
                qty = int(input('How many?\n'))
                cart.append([items[sub][0], items[sub][1], 'x'+str(qty), qty*int(items[sub][1])])
        elif sec == '5':
            frozenitems()
            items = buymenu('frozenitems.txt')
            sub = int(input('Choose an item(number) or press 0 to exit this menu:\n'))
            while sub > len(items) - 1:
                print('invalid selection')
                sub = int(input('Choose an item(number) or press 0 to exit this menu:\n'))
            if sub > 0:
                qty = int(input('How many?\n'))
                cart.append([items[sub][0], items[sub][1], 'x'+str(qty), qty*int(items[sub][1])])

        for i in cart:
            print(i[0], i[1], i[2], i[3])

        print()
        print('Press 1 to continue shopping')
        print('Press 2 to view/modify cart')
        print('Press 3 to checkout')
        drop = int(input())
        while drop > 3 or drop < 1:
            print('invalid selection')
            drop = int(input('Enter Valid selection number \n'))
        if drop == 1:
            mainmenu()
            sec = input('Choose a section(number):\n')
            while len(sec) > 1 or not 49 <= ord(sec) <= 53:
                print('Error: invalid selection')
                sec = input('Choose a section(number):\n')
        elif drop == 2:
            cart = modify_cart(cart)
            for i in cart:
                print(i[0], i[1], i[2], i[3])
        else:
            bill = 0
            print()
            for i in cart:
                bill += int(i[3])
                print(i[0], i[1], i[2], i[3])
            print('Your bill is', str(bill))
            points = int(bill/100)
            print('You have earned', points, 'loyalty points')
            print('Thank you for shopping with us')
            want = False


shop()
