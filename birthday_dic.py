if __name__ == '__main__':#it sets a few special variables like __name__, and __main__

    Birth = {
        'Albert Einstein': '23-01-1999',
        'Benjamin Franklin': '01-17-1706',
        'Ada Lovelace': '28-5-2003',
        }

    print('Welcome to the birthday dictionary. We know the birthdays of:')
    for name in Birth:
        print(name)

    print('Who\'s birthday do you want to look up?')
    name = input()
    if name in Birth:
        print('{}\'s birthday is {}.'.format(name, Birth[name]))
    else:
        print(' we don't have {}'s birthday.'.format(name))
