import sys

clients = [
    {
        'name': 'Pablo',
        'company': 'Google',
        'email': 'pablo@google.com',
        'position': 'Sofware Engineer',
    },
    {
        'name': 'Kevin',
        'company': 'Facebook',
        'email': 'Kmarquez@facebook.com',
        'position': 'Frontend Developer',
    },
]


def _get_client_from_user():
    client = {
        'name': _get_client_field('name'),
        'company': _get_client_field('company'),
        'email': _get_client_field('email'),
        'position': _get_client_field('position'),
    }

    return client


def create_clients(client):
    global clients

    if client not in clients:
        clients.append(client)
    else:
        print('Client already is in the clien\'s list')


def list_clients():
    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'
              .format(
                  uid=idx,
                  name=client['name'],
                  company=client['company'],
                  email=client['email'],
                  position=client['position'],)
              )


def update_client(client_id, updated_client):
    global clients

    if len(clients) - 1 >= client_id:
        clients[client_id] = updated_client
    else:
        print('Client is not in clients list')


def delete_client(client_id):
    global clients
    cont = 0

    for idx, client in enumerate(clients):
        if idx == client_id:
            del clients[idx]
            cont = 0
            break
        else:
            cont = cont + 1

    if cont >= 1:
        print('Client is not in clients list')


def search_client(client_name):
    # global clients
    for client in clients:
        if client['name'] != client_name:
            continue
        else:
            return True


def _get_client_field(field_name):
    field = None

    while not field:
        field = input('What is the client {}?'.format(field_name))

    return field

# def _get_client_name():
#     client_name = None

#     while not client_name:
#         client_name = input('What is the client name? ')

#         if client_name == 'exit':
#             client_name = None
#             break
#     if not client_name:
#         sys.exit()

#     return client_name


def _print_welcome():
    print("WELCOME TO PLATZI VENTAS")
    print('*' * 50)
    print('What would you like to do today?')
    print('[C]reate Client')
    print('[L]ist Client')
    print('[U]pdate Client')
    print('[D]elete Client')
    print('[S]earch Client')


if __name__ == '__main__':
    _print_welcome()
    command = input()
    command = command.upper()

    if command == 'C' or command == 'c':
        client = _get_client_from_user()
        create_clients(client)
        list_clients()

    elif command == 'L':
        list_clients()

    elif command == 'U':
        list_clients()
        client_id = int(_get_client_field('id'))
        updated_client = _get_client_from_user()
        update_client(client_id, updated_client)
        list_clients()

    elif command == 'D':
        client_id = int(_get_client_field('id'))
        delete_client(client_id)
        list_clients()

    elif command == 'S':
        client_name = _get_client_field('name')
        found = search_client(client_name)

        if found:
            print('The client is in client\'s list')
        else:
            print('The client: {} is not in our clien\'s list '.format(client_name))
    else:
        print('Invalid Command')

    # list_clients()
    # create_clients('Kevin')
    # list_clients()
