users = []
admins = []
all_prods = []
order = None
account_type = None


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
        main_menu('admin' or 'user')
    else:
        print('Product', searchable_item.capitalize(), 'does not exist!')
        search()


def sign_up():
    global account_type
    account_type = int(input('What type of user you wanna create?\n'
                             '1-Admin, 2-User\n'))
    match account_type:
        case 1:
            admins_sign_up()
        case 2:
            users_sign_up()
        case _:
            print('Try again')
            sign_up()


# def sign_up(user_type):
#     match user_type:
#         case 'admin':
#

def admins_sign_up():
    login = input('Enter login: ')
    admin_pass = int(input('Think up a password: '))
    for i in admins:
        if i == login:
            print('This login name already taken!')
            admins_sign_up()
    if isinstance(login, int):
        print('Log in name must be a string value')
        admins_sign_up()
    elif len(str(admin_pass)) < 4:
        print('Password must be 4 or more digits!')
        admins_sign_up()
    else:
        admins.append(login)
        admins.append(admin_pass)
        main_menu('admin')


def users_sign_up():
    name = input('Enter your name here: ')
    user_pass = int(input('Think up a password: '))
    for i in users:
        if i == name:
            print('This username already taken!')
            users_sign_up()
    if len(str(user_pass)) < 4:
        print('Password must be 4 or more digits!')
        users_sign_up()
    else:
        users.append(name)
        users.append(user_pass)
        main_menu('user')


def sign_in():
    type_of_user = int(input('Which account do you want to log in to?'
                             '1-Admin; 2-User\n'))
    match type_of_user:
        case 1:
            login = input('Login: ')
            password = int(input('Password: '))
            if login in admins and password == admins[admins.index(login) + 1]:
                print('Welcome,', login.capitalize() + '!')
                main_menu('admin')
            else:
                print('The login or password is incorrect.')
                sign_in()
        case 2:
            name = input('Name: ')
            password = int(input('Password: '))
            if name in users and password == users[users.index(name) + 1]:
                print('Welcome,', name.capitalize() + '!')
                main_menu('user')
            else:
                print('The username or password is incorrect.')
                sign_in()
        case _:
            print('Enter 1 or 2!')
            sign_in()


def add_to_order():
    global order
    order = []
    product = input('Type the name of product you wanna add to order:\n')
    wanted_quantity = int(input('How much?\n'))
    if product in all_prods and wanted_quantity < all_prods[all_prods.index(product) + 1]:
        quantity_of_prod = all_prods[all_prods.index(product) + 1]
        updated_quantity = quantity_of_prod - wanted_quantity
        order.append(product)
        order.append(wanted_quantity)
        all_prods.remove(quantity_of_prod)
        all_prods.insert(all_prods.index(product) + 1, updated_quantity)
        print('Item', product, 'was added to your order!')
        main_menu('user')
    else:
        print('There is no item with such name or wanted quantity are more than in all products')
        add_to_order()


def add_item():
    while True:
        product_name = input('Type the name of product you wanna add:\n'
                             'Type 000 if you have finish\n')
        if product_name == '000':
            main_menu('admin')
        elif product_name in all_prods:
            print('A product with that name already exists.')
            add_item()
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
        main_menu('admin')
    else:
        print('There is no item with name', {removable_item})
        remove_item()


def display_info(content):
    match content:
        case 'admin':
            print('Admins -', chunk(admins, 2))
            main_menu('admin')
        case 'user':
            if not users:
                print('User accounts does not exist!')
            else:
                print('Users -', chunk(users, 2))
            main_menu('admin')
        case 'products':
            if not all_prods:
                print('List of all products is empty')
            else:
                print('List of all products -', chunk(all_prods, 2))
            main_menu('admin')
        case 'orderItem':
            if not order:
                print('Your order is empty')
            else:
                print('Your order items -', chunk(order, 2))
            main_menu('user')


def main_menu(user_type):
    admins_dict = \
        dict([(1, lambda: add_item()),
              (2, lambda: remove_item()),
              (3, lambda: main()),
              (4, lambda: search()),
              (5, lambda: display_info('admin')),
              (6, lambda: display_info('user'))]
             )

    users_dict = \
        dict([(1, lambda: add_to_order()),
              (2, lambda: main()),
              (3, lambda: search()),
              (4, lambda: display_info('orderItem')),
              (5, lambda: display_info('products'))]
             )
    match user_type:
        case 'admin':
            if not all_prods:
                value = int(input('What do you wanna do?\n'
                                  '1-Add item\n'))
            else:
                value = int(input('What do you wanna do?\n'
                                  '1-Add item; '
                                  '2-Remove item; '
                                  '3-Switch to another account; '
                                  '4-Product search; '
                                  '5-Display all admin accounts; '
                                  '6-Display all user accounts; \n'))
            return admins_dict.get(value, lambda: default())()

        case 'user':
            value = int(input('What do you wanna do?\n'
                              '1-Add item to card; '
                              '2-Switch to another account; '
                              '3-Product search; '
                              '4-Display order items; '
                              '5-Display list of all products; \n'))
            return users_dict.get(value, lambda: default())()


def default():
    print('Неизвестно как обработать')


main()
