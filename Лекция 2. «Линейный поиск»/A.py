def input_read():
    return input().split()


def ascending_list(lst):
    if len(lst) < 2:
        return 'YES'
    for i in range(len(lst) - 1):
        if lst[i] >= lst[i + 1]:
            return 'NO'
    return 'YES'


def main():
    print(ascending_list(input_read()))


if __name__ == '__main__':
    main()
