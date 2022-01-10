users = []
admins = []
all_prods = []


def main():
    value = int(input('1-sign up; 2-sign in\n'))
    dd = dict([(1, lambda: sign_up()),
               (2, lambda: sign_in())]
              )
    return dd.get(value, lambda: default())()


def chunk(my_list, size):
    return [my_list[i:i + size] for i in range(0, len(my_list), size)]


def search():
    searchable_item = input('What product do you want to get information about?\n')
    if searchable_item in all_prods:
        quantity_of_item = all_prods[all_prods.index(searchable_item) + 1]
        print('Product name -', searchable_item.capitalize())
        print('Quantity of this product -', quantity_of_item)
    else:
        print('Product', searchable_item.capitalize(), 'does not exist!')
        search()


def sign_up():
    global account_type
    account_type = int(input('What type of user you wanna create?\n'
                             '1-Admin, 2-User\n'))
    if account_type == 1:
        login = str(input('Type login: '))
        a_pass = int(input('Think up a password: '))
        admins.append(login.upper())
        admins.append(a_pass)
        main_menu()
    elif account_type == 2:
        name = input('Type your name here: ')
        password = int(input('Think up a password: '))
        users.append(name.lower())
        users.append(password)
        main_menu()
    else:
        print('Try again')
        sign_up()


def sign_in():
    if account_type == 1:
        login = input('Login: ')
        password = int(input('Password: '))
        if login in admins and password == admins[admins.index(login) + 1]:
            print('Welcome,', login.capitalize() + '!')
            main_menu()
        else:
            print('The login or password is incorrect.')
            sign_in()
    elif account_type == 2:
        name = input('Name: ')
        password = int(input('Password: '))
        if name in users and password == users[users.index(name) + 1]:
            print('Welcome,', name.capitalize() + '!')
            main_menu()
        else:
            print('The username or password is incorrect.')
            sign_in()


def add_to_order():
    global order
    order = list()
    product = input('Type the name of product you wanna add to order:\n')
    wanted_quantity = int(input('How much?\n'))
    if product in all_prods and wanted_quantity < all_prods[all_prods.index(product) + 1]:
        quantity_of_prod = all_prods[all_prods.index(product) + 1]
        order.append(product)
        order.append(wanted_quantity)
        updated_quantity = quantity_of_prod - wanted_quantity
        all_prods.remove(quantity_of_prod)
        all_prods.insert(all_prods.index(product) + 1, updated_quantity)
        print('Your order items -', chunk(order, 2))
        main_menu()
    else:
        print('There is no item with such name or wanted quantity are more than in all products')
        add_to_order()


def add_item():
    while True:
        product_name = input('Type the name of product you wanna add:\n'
                             'Type 000 if you have finish\n')
        if product_name == '000':
            main_menu()
        else:
            product_quantity = int(input('Type the quantity of product:\n'))
            all_prods.append(product_name)
            all_prods.append(product_quantity)
            print('Item', product_name, 'was added!')
            print('Now the list of all products looks like this -', chunk(all_prods, 2))


def remove_item():
    removable_item = input('Which item do you wanna remove?\n')
    if removable_item in all_prods:
        quantity_of_item = all_prods[all_prods.index(removable_item) + 1]
        all_prods.remove(removable_item)
        all_prods.remove(quantity_of_item)
        print('Item', removable_item, 'was deleted!')
        print('Now the list of all products looks like this -', chunk(all_prods, 2))
    else:
        print('There is no item with name', removable_item)
        remove_item()


def main_menu():
    admins_dict = \
        dict([(1, lambda: add_item()),
              (2, lambda: remove_item()),
              (3, lambda: main()),
              (4, lambda: search()),
              (5, lambda: print('Admins -', chunk(admins, 2))),
              (6, lambda: print('Users -', chunk(users, 2)))]
             )

    users_dict = \
        dict([(1, lambda: add_to_order()),
              (2, lambda: main()),
              (3, lambda: search()),
              (4, lambda: print('Your order -', chunk(order, 2)))]
             )
    if account_type == 1:
        if not all_prods:
            value = int(input('What do you wanna do?\n'
                              '1-Add item\n'))
        else:
            value = int(input('What do you wanna do?\n'
                              '1-Add item; '
                              '2-Remove item; '
                              '3-Switch to another account; '
                              '4-Product search'
                              '5-Display all admin accounts'
                              '6-Display all user accounts\n'))
        return admins_dict.get(value, lambda: default())()

    elif account_type == 2:
        value = int(input('What do you wanna do?\n'
                          '1-Add item to card; '
                          '2-Switch to another account; '
                          '3-Product search'
                          '4-Display order items\n'))
        return users_dict.get(value, lambda: default())()


def default():
    print('Неизвестно как обработать')


main()
