account = input('do you want to sign up or login? ')
# enter whatever your file name is here
file = open('login.txt', 'r+')


def sign_up(filename):
    signing_up = True
    while signing_up:
        username = input('Enter user name here? ')
        password = input('Enter your password ')
        confirm_password = input('enter you password again ')
        if len(username) < 8:
            print('Your user name must be at least eight characters long')
            file.seek(0)
            continue
        if username in filename.read():
            print('pick a new user name as it is already taken')
            file.seek(0)
            continue
        if password != confirm_password:
            print('Please make sure your passwords match ')
            file.seek(0)
            continue
        filename.write(f'\n{username} - {password}')
        print('you are logged in')
        signing_up = False


def log_in(filename):
    logging_in = True
    while logging_in:
        username = input('Username: ')
        password = input('Password: ')
        in_file = f'{username} - {password}'
        if in_file in filename.read():
            print('you are logged in')
            file.seek(0)
            logging_in = False
        if in_file not in filename.read():
            file.seek(0)
            print('user name or password are incorrect')
            continue


if account == 'sign up':
    sign_up(file)
if account == 'login':
    log_in(file)
file.close()
