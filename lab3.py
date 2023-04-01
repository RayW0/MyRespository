#1)	Написать программу используя цикл for и while. 
# Исходный список чисел
numbers = [10, 11, 12, 13]

# Используем цикл for для подсчета суммы чисел в списке
sum = 0
for num in numbers:
    sum += num

# Используем цикл while для подсчета количества чисел в списке
count = 0
i = 0
while i < len(numbers):
    count += 1
    i += 1

# Вычисляем среднее значение
average = sum / count

# Выводим результаты на экран
print(f"Сумма чисел: {sum}")
print(f"Количество чисел: {count}")
print(f"Среднее значение: {average}")

#используя функцию range() сделать список. в функцию range() введите данные с разными типами и выведите на экран в разных примерах. 

#Создание списка целых чисел с помощью функции range()
my_list = list(range(1, 10))
print(my_list)

#Создание списка чисел с плавающей точкой с помощью функции range()
my_list = list(range(1, 10, 2))
my_float_list = [float(num) for num in my_list]
print(my_float_list)

#Создание списка строк с помощью функции range()
my_list = list(range(97, 105))
my_str_list = [chr(num) for num in my_list]
print(my_str_list)

#Создание списка строк с помощью функции range()
my_bool_list = [bool(num % 2) for num in range(1, 6)]
print(my_bool_list)

