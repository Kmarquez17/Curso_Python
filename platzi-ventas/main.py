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
    
def _add_coma():
    global clients
    clients += ','

def _print_welcome():
    print("WELCOME TO PLATZI VENTAS")
    print('*' * 50)
    print('What would you like to do today?')
    print('[C] Create Client')
    print('[D] Delete Client')


if __name__ == '__main__':
    _print_welcome()
    command = input()

    if command == 'C' or command == 'c':
        client_name = input('What is the client name? ')
        create_clients(client_name)
        list_client()
    elif command == 'D':
        pass
    else:
        print('Invalid Command')

    # list_client()
    # create_clients('Kevin')
    # list_client()   