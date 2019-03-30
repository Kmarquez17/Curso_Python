clients = 'Pablo, Ricardo, '


def create_clients(client_name):
    global clients

    if client_name not in clients:
        clients += client_name
        _add_coma()
    else:
        print('Client already is in the clien\'s list')


def list_client():
    print(clients)


def update_client(client_name, update_client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ',', update_client_name + ',')
    else:
        print('Client is not in clients list')


def _add_coma():
    global clients
    clients += ','


def _get_client_name():
    return input('What is the client name? ')


def _print_welcome():
    print("WELCOME TO PLATZI VENTAS")
    print('*' * 50)
    print('What would you like to do today?')
    print('[C] Create Client')
    print('[U] Create Client')
    print('[D] Delete Client')


if __name__ == '__main__':
    _print_welcome()
    command = input()
    command = command.upper()

    if command == 'C' or command == 'c':
        client_name = _get_client_name()
        create_clients(client_name)
        list_client()
    elif command == 'D':
        pass
    elif command == 'U' or command == 'u':
        client_name = _get_client_name()
        update_client_name = input('What is the updated client name ')
        update_client(client_name, update_client_name)
        list_client()
    else:
        print('Invalid Command')

    # list_client()
    # create_clients('Kevin')
    # list_client()
