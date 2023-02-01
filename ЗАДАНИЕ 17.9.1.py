while True:
    N = input('Введите только числа через пробел: ')
    s = N.replace(' ', '')
    if s.isdigit():  # проверяем, что в веденных данных только цифры
        print('Введены корректные данные, продолжаем!')
        break
nums = list(map(int, N.split()))

try:
    num = int(input('Введите любое число: '))
    if num < min(nums) or num > max(nums):  # проверка введенного числа на принадлежность диапазону последовательности
        raise ValueError('Условия не удовлетворяются: число не входит в диапазон последовательности')
except ValueError as error:
    print(error)
    print('Окончание программы')

else:
    print('Вы ввели корректное число, работаем!')

    if num % 1 == 0:
        nums.append(num)
        print(f'Преобразованная в список последовательность чисел до сортировки: {nums}')

    def sort_list(nums):
        for i in range(len(nums)):
            idx_min = i
            for j in range(i, len(nums)):
                if nums[j] < nums[idx_min]:
                    idx_min = j
            if i != idx_min:
                nums[i], nums[idx_min] = nums[idx_min], nums[i]
        return nums
    print('Отсортированный по возрастанию элементов список с введеным числом: ', sort_list(nums))


    def binary_search(nums, num, left, right):
        if left > right:
            return False
        middle = (right + left) // 2
        if nums[middle] == num:
            return middle
        elif num < nums[middle]:
            return binary_search(nums, num, left, middle - 1)
        else:
            return binary_search(nums, num, middle + 1, right)

    index = binary_search(nums, num, 0, len(nums) - 1)
    print(f'Индекс элемента, который меньше введенного Вами числа: {index - 1}')






