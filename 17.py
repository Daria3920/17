try:
    number = input('введите число через пробел: ')
    user_num = int(input('введите любое число:'))
    if ',' in number:
        print("введите числа, соотвествующие условиям. перезагрузите программу и потворите попытку.")
    if type(user_num) != int:
        print("число не соответствует условиям. перезагрузите программу и повторите попытку.")
except ValueError:
    print('Введите целое число')


def is_int(str):
    str = str.replace(' ', '')
    try:
        int(str)
        return True
    except ValueError:
        return False


if " " not in number:
    print("\nв водде нет пробелов (введите числа, согласно условиям.)")
    sequence_numbers = input('Введите целые числа через пробел: ')
if not is_int(number):
    print('\nВ ВВОДЕ СОДЕРЖАТСЯ НЕ ЦИФРЫ ЛИБО НЕ ЦЕЛЫЕ ЧИСЛА (введите числа, согласно условиям.)\n')
    print(error)
else:
    number = number.split()

list_number = [int(item) for item in number]


def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1
    return result


list_number = merge_sort(list_number)


def binary_search(array, element, left, right):
    try:
        if left > right:
            return False
        middle = (right + left) // 2
        if array[middle] == element:
            return middle
        elif element < array[middle]:
            return binary_search(array, element, left, middle - 1)
        else:
            return binary_search(array, element, middle + 1, right)
    except IndexError:
        return 'Число выходит за диапазон, введите меньшее число.'

print(f'Упорядоченный по возрастанию список: {number}')