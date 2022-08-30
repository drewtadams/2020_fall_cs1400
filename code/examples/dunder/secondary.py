import primary as p


def main():
    print(f'__name__ from primary: {p.get_name()}')
    print(f'__name__ from secondary: {get_name()}')
    

def get_name():
    return __name__


if __name__ == '__main__':
    main()