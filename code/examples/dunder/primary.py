import secondary as s


def main():
    print(f'__name__ from primary: {get_name()}')
    print(f'__name__ from secondary: {s.get_name()}')
    
    
def get_name():
    return __name__


if __name__ == '__main__':
    main()