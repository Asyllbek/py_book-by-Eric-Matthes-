# # import this
# bicycles = ['trek', 'reder', 'tenet', 'roar']
# print(bicycles)
# print(bicycles[0].title())
# print(bicycles[-1])
# message = "My first bicycle was a " + bicycles[2].title() + "."
# print(message)
#
# # Имена: сохраните имена нескольких своих друзей в списке с именем names. Выведите
# # имя каждого друга, обратившись к каждому элементу списка (по одному за раз).
#
# my_friends = ['Elchibek', 'Denis', 'Bayastan', 'Kudaiar', 'Janybek']
# print(my_friends[0], my_friends[1], my_friends[2], my_friends[3], my_friends[4])
#
# # 3-2. Сообщения: начните со списка, использованного в упражнении 3-1, но вместо вывода
# # имени каждого человека выведите сообщение. Основной текст всех сообщений должен
# # быть одинаковым, но каждое сообщение должно включать имя адресата.
# greeting = 'Hello, '
# dot = '.\n'
# print(greeting + my_friends[0] + dot, greeting + my_friends[1] + dot, greeting + my_friends[2] + dot, greeting +
#       my_friends[3] + dot, greeting + my_friends[4] + dot)
#
# # 3-3. Собственный список: выберите свой любимый вид транспорта (например, мотоциклы
# # или машины) и создайте список с примерами. Используйте свой список для вывода утверж-
# # дений об элементах типа: «Я хотел бы купить мотоцикл Honda».
#
# my_favorite_cars = ['Bugatti Veyron', 'Lykan Hypersport', 'Lamborghini Veneno Roadster', 'Koenigsegg CCXR Trevita',
#                     'Mercedes Benz Maybach Exelero', 'Rolls Royce Sweptail', 'Bugatti La Voiture Noire']
#
# print('I want/would like to buy ' + my_favorite_cars[0] + '!\n', 'I want/would like to buy ' + my_favorite_cars[1]
#       + '!\n', 'I want/would like to buy ' + my_favorite_cars[2] + '!\n', 'I want/would like to buy '
#       + my_favorite_cars[3] + '!\n', 'I want/would like to buy ' + my_favorite_cars[4]
#       + '!\n', 'I want/would like to buy ' + my_favorite_cars[5] + '!\n', 'I want/would like to buy '
#       + my_favorite_cars[6] + '!\n',)
#
# # change
# my_favorite_cars[1] = 'Aston Martin'
# print(my_favorite_cars)
#
# # addition
# my_favorite_cars.append('Aston Martin Valkyrie')
# print(my_favorite_cars)
# # append
# empty_list = []
# empty_list.append('Aston Martin Valkyrie')
# empty_list.append('Honda')
# empty_list.append('Suzuki')
# print(empty_list)
#
# # Deletion
# # del
# del empty_list[1]
# print(empty_list)
# empty_list.append('Jeep')
# print(empty_list)
# popped_empty_list = empty_list.pop()
# print(popped_empty_list)
# popped_empty_list_two = empty_list.pop(0)
# print(popped_empty_list_two)
# print(empty_list)
#
# motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
# print(motorcycles)
# too_expensive = 'ducati'
# motorcycles.remove(too_expensive)
# print(motorcycles)
#
# guests = ['Leonardo', 'Michelangelo', 'Donatello', 'Raphael']
# text = 'I invite you to my birthday '
# print(text + guests[0] + '!,  sincerely Asylbek ;)\n', text + guests[1] + '!,  sincerely Asylbek ;)\n',
#       text + guests[2] + '!,  sincerely Asylbek ;)\n', text + guests[3] + '!,  sincerely Asylbek ;)')
# print(guests.pop(2))
# print(guests)
# guests.insert(2, 'Bruce')
# print(guests)
# guests.pop()
# guests.pop()
# print(guests)
# del guests[0]
# del guests[0]
# print(guests)
# new_list = []
# new_list.append('Leo')
# new_list.insert(0,'Don')
# new_list.append('Lord Genry')
# new_list.append('Antuan')
# print(new_list)
# new_list.sort()
# print(new_list)
# new_list.append('Avatar')
# print(new_list)
# print(sorted(new_list))
# print(new_list)
# new_list.reverse()
# print(new_list)
# print(len(new_list))
# print(type(len(guests)))
# print(new_list[-1])

# Error of indexing
# error_list = ['Key', 'for', 'your', 'heart', 'is', 'love']
# print(len(error_list))
# print(error_list[6])
# Traceback (most recent call last):
#   File "/home/asylbek/pyhonbook/lists.py", line 103, in <module>
#     print(error_list[6])
# IndexError: list index out of range

# print('E')
#
# list_of_names = ['Aristotle', 'Plato', 'Friedrich Nietzsche', 'René Descartes', 'Confucius', 'Socrates',
#                  'Jean-Jacques Rousseau', 'John Locke', 'John Calvin', 'Swami Vivekananda']
# for list_of_name in list_of_names:
#     print(list_of_name + ', your philosophy is relatively great !')
#     print('I would be glad to talk with you about life if I got into your time...' + list_of_name + '\n')
# print('Just for it')
# # Logic error
# print(list_of_name)


# types_of_pizza = ['Neapolitan Pizza', 'Chicago Pizza', 'New York-Style Pizza', 'Sicilian Pizza', 'Greek Pizza',
#                   'California Pizza', 'Detroit Pizza', 'St. Louis Pizza']
#
# for type_of_pizza in types_of_pizza:
#     print(type_of_pizza)
#     print('I like ' + type_of_pizza)
# print('Yes !')

# list_of_names_animals = ['Acinonyx', 'Caracal', 'Catopuma', 'Felis']
# for name_of_animal in list_of_names_animals:
#     print('A ' + name_of_animal + 'very strong and tenacious')
# print('The whole feline family is great')

# for value in range(1, 11):
#     print(value)
#
# even_numbers = list(range(2, 11, 2))
# print(even_numbers)

# Использование range() для создания числового списка
# numbers = list(range(1,11))
#
# print(numbers)

# even_numbers = list(range(2,11,2))
# print(even_numbers)

# squares = []
# for value in range(1,11):
#     square = value ** 2
#     squares.append(square)
# print(squares)

# digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# print(min(digits))
# print(max(digits))
# print(sum(digits))

# Генераторы списков (list comprehension)
# squares = [value ** 2 for value in range(1, 11)]
# print(squares)

# Считаем до 20: используйте цикл for для вывода чисел от 1 до 20 включительно
# for i in range(1, 21):
#     print(i)
# print(type(i))

# Миллион: создайте список чисел от 1 до 1 000 000, затем воспользуйтесь циклом for
# для вывода чисел. (Если вывод занимает слишком много времени, остановите его нажатием
# Ctrl+C или закройте окно вывода

# list_of_million = list(range(1, 1000001))
# for i in list_of_million:
#     print(i)
#


# Суммирование миллиона чисел: создайте список чисел от 1 до 1 000 000, затем вос-
# пользуйтесь функциями min() и max() и убедитесь в том, что список действительно начи-
# нается с 1 и заканчивается 1 000 000. Вызовите функцию sum() и посмотрите, насколько
# быстро Python сможет просуммировать миллион чисел

# list_million = [value * 1 for value in range(1, 1000001)]
# print(list_million)
# print('max=', max(list_million), 'min=', min(list_million), 'sum=', sum(list_million))

# Нечетные числа: воспользуйтесь третьим аргументом функции range() для создания
# списка нечетных чисел от 1 до 20. Выведите все числа в цикле for.

# list_kubs = []
# for i in range(1, 21, 2):
#     list_kubs.append(i)
# print(list_kubs)


# 4-7. Тройки: создайте список чисел, кратных 3, в диапазоне от 3 до 30. Выведите все числа
# своего списка в цикле for

# lisst = []
# for i in range(3, 31, 3):
#     lisst.append(i)
# print(lisst)

# Кубы: результат возведения числа в третью степень называется кубом. Например,
# куб 2 записывается в языке Python в виде 2**3. Создайте список первых 10 кубов (то есть
# кубов всех целых чисел от 1 до 10) и выведите значения всех кубов в цикле for.

# list = []
# for i in range(1, 11):
#     i = i ** 3
#     list.append(i)
#
# print(list)


# Генератор кубов: используйте конструкцию генератора списка для создания списка
# первых 10 кубов.

# list_cubes = [value ** 3 for value in range(1, 11)]
# print(list_cubes)


# Работа с частью списка
# В главе 3 вы узнали, как обращаться к отдельным элементам списка, а в этой главе
# мы занимались перебором всех элементов списка. Также можно работать с конкрет-
# ным подмножеством элементов списка; в Python такие подмножества называются
# срезами (slices).

# Создание среза

# players = ['Elliott', 'Mike', 'Leo', 'Niko', 'Paul']
# print(players[0:3])
# print(players[:4])
# print(players[2:])

# my_foods = ['pizza', 'falafel', 'carrot cake', 'apple cake', 'cake']
# friend_foods = my_foods[:]
# print("My favorite foods are:")
# print(my_foods)
# print("\nMy friend's favorite foods are:")
# print(friend_foods)
# my_foods.append('conelli')
# friend_foods.append('ice cream')
# print("My favorite foods are:")
# print(my_foods)
# print("\nMy friend's favorite foods are:")
# print(friend_foods)
# # сообщение «The first three items in the list are:», а затем использует срез для
# # вывода первых трех элементов из списка.
# print(my_foods)
# print(my_foods[:3])

# Выводит сообщение «Three items from the middle of the list are:», а затем использует
# срез для вывода первых трех элементов из середины списка.
# print(len(my_foods))
# print(my_foods[1:4])

# Выводит сообщение «The last three items in the list are:», а затем использует срез для
# вывода последних трех элементов из списка.
# print(len(my_foods))
# print(my_foods[2:])

# Моя пицца, твоя пицца: начните с программы из упражнения 4-1. Создайте копию
# списка с видами пиццы, присвойте ему имя friend_pizzas. Затем сделайте следующее.


# my_pizza = ['Neapolitan Pizza', 'Chicago Pizza', 'New York-Style Pizza', 'Sicilian Pizza', 'Greek Pizza',
#             'California Pizza', 'Detroit Pizza', 'St. Louis Pizza']
# friends_pizza = my_pizza[:]
# print('My pizza :', my_pizza)
# print('\nMy friends pizza: ', friends_pizza)
# # Добавьте новую пиццу в исходный список.
#
# my_pizza.append('Pepperoni pizza')
#
#
# # Добавьте другую пиццу в список friend_pizzas.
# friends_pizza.append('Turin pizza')
#
# print('My favorite pizzas are: ', my_pizza)
# print("\n My friend's favorite pizzas are:", friends_pizza)
#
# for ipizza in my_pizza:
#     print(ipizza)
#
# for fpizza in friends_pizza:
#     print(fpizza)


# # Кортежи
#
# dimensions = (500, 1000, 900)
# print(dimensions)
# print(dimensions[0])
# print(dimensions[1])
# # Error dimensions[1] = 5000
# # print(dimensions)
# # TypeError: 'tuple' object does not support item assignment
# for dimension in dimensions:
#     print(dimension)
#
# # Замена кортежа
# dimensions = (200, 50)
# print("Original dimensions:")
# for dimension in dimensions:
#     print(dimension)
#
# dimensions = (400, 100)
# print("\nModified dimensions:")
# for dimension in dimensions:
#     print(dimension)

# Шведский стол: меню «шведского стола» в ресторане состоит всего из пяти пунктов.
# Придумайте пять простых блюд и сохраните их в кортеже.

# food = ('Neapolitan Pizza', 'Chicago Pizza', 'New York-Style Pizza', 'Sicilian Pizza', 'Greek Pizza')
# print(food)
# Используйте цикл for для вывода всех блюд, предлагаемых рестораном.
# for f in food:
#     print(f)

# Попробуйте изменить один из элементов и убедитесь в том, что Python отказывается
# вносить изменения
# food[2] = 'Error'
# Traceback (most recent call last):
#   File "/home/asylbek/pyhonbook/lists.py", line 325, in <module>
#     food[2] = 'Error'
# TypeError: 'tuple' object does not support item assignment

# food = ('New York-Style Pizza', 'Sicilian Pizza', 'Greek Pizza', 'Detroit Pizza', 'St. Louis Pizza')
# print('New Menu: ', food)

# cars = ['audi', 'bmw', 'subaru', 'toyota']
# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())

# requested_topping = 'mushrooms'
#
# if requested_topping != 'achovies':
#     print("Hold the achieves !")
#
# answer = 121
# if answer != 45:
#     print('That is not the correct answer. Please try again!')

# car = "Alfa Romeo"
# print("Is car 'Alfa Romeo' ?, I predict True.")
# print(car == 'Alfa Romeo')
# print("\nIs car 'BMW' ?, I predict False.")
# print(car == 'BMW')
# car = "Bugatti"
# print("Is car 'Alfa Romeo' ?, I predict False.")
# print(car == 'Alfa Romeo')
# print("\nIs car 'BMW' ?, I predict False.")
# print(car == 'BMW')
# car = "Lamborgini"
# print("Is car 'Lamborgini' ?, I predict True.")
# print(car == 'Lamborgini')
# print("\nIs car 'BMW' ?, I predict False.")
# print(car == 'BMW')

# Больше условий: количество условий не ограничивается 10. Попробуйте написать дру-
# гие условия и включить их в conditional_tests.py. Программа должна выдавать по крайней
# мере один истинный и один ложный результат для следующих видов проверок.
# • Проверка равенства и неравенства строк.
# • Проверки с использованием функции lower().
# • Числовые проверки равенства и неравенства, условий «больше», «меньше», «больше
# или равно», «меньше или равно».
# • Проверки с ключевым словом and и or.
# • Проверка вхождения элемента в список.
# • Проверка отсутствия элемента в списке.

# string = 'SlowMo'
# print(string == 'SlowMO')
# print('\nFalse = ', string == 'slowmo')
# print('\nTrue = ', string != 'slowmo')
# print('\nwith lower:True', string.lower() == 'slowmo')
# print(string.lower() != 'slowmo')
# number = 88
# number_one = 56
# if number > 99:
#     print("Yes n > 99")
# else:
#     print("Noo!")
# if number < 99:
#     print("number<99")
# if number > 45 or number < 45:
#     print("Lawyer?")
# if number > 18 and number < 99:
#     print("True!")
# if number != 85 and number != 5:
#     print("Yes!")
# if number != 85 or number_one != 5:
#     print("Yes! !")

# age = int(input("Your age: "))
# if age < 4:
#     print("Your admission cost is 0$")
# elif age < 18:
#     print("Your admission is 8$")
# else:
#     print("Your admission cost is 15$")

# age = int(input("Your age: "))
# if age < 4:
#     price = 0
# elif age < 18:
#     price = 5
# elif age < 65:
#     price = 10
# elif age >= 65:
#     price = 5
# print("Your admission cost is $" + str(price) + ".")


# Цвета 1: представьте, что в вашей компьютерной игре только что был подбит корабль
# пришельцев. Создайте переменную с именем alien_color и присвойте ей значение ‘green’,
# ‘yellow’ или ‘red’.

# alien_color = 'yellow'
# if alien_color == 'green':
#     print("Вы заработали 5 очков")
# alien_color = 'green'
# if alien_color == 'green':
#     print("Вы заработали 5 очков")

# alien_color = 'green'
# if alien_color == 'green':
#     print("Вы заработали 5 очков")
#
# #  Если переменная содержит любое другое значение, выведите сообщение о том, что
# # игрок только что заработал 10 очков.
# alien_color = 'yellow'
# if alien_color != 'green':
#     print("Вы заработали 10 очков")
#
# # Напишите одну версию программы, в которой выполняется блок if, и другую версию,
# # в которой выполняется блок else.
#
# alien_color = 'red'
# if alien_color == 'red':
#     print("Вы заработали 5 очков")
# else:
#     print("Вы заработали 10 очков")
#
# alien_color = 'yellow'
# if alien_color == 'red':
#     print("Вы заработали 5 очков")
# else:
#     print("Вы заработали 15 очков")

# alien_color = str(input("Color name: ").title())
#
# if alien_color == "Yellow":
#     print("You have earned 15 points !")
# elif alien_color == "Red":
#     print("You have earned 10 points !")
# else:
#     print("You have earned 5 points !")

# age = int(input("Enter the age: "))
# if age <= 2:
#     print("baby")
# elif 2 <= age < 4:
#     print("kid")
# elif 4 <= age < 13:
#     print("child")
# elif 13 <= age < 20:
#     print("teenager")
# elif 20 <= age < 65:
#     print("Adult")
# elif age > 64:
#     print("old man")

# Множественные списки
# Любимый фрукт: составьте список своих любимых фруктов. Напишите серию независи-
# мых команд if для проверки того, присутствуют ли некоторые фрукты в списке.
# fruits = ['Apple', 'Apricots', 'Avocado', 'Banana', 'Blackberries' 'Blackcurrant', 'Blueberries', 'Breadfruit']
# if "Apple" in fruits:
#     print("Apple")
# if "Banana" in fruits:
#     print("Banana")
# requested_toppings = ['mushrooms', 'green peppers', 'french cheese']
# available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
#
# for requested_topping in requested_toppings:
#     if requested_topping in available_toppings:
#         print("Adding " + requested_topping + ".")
#     else:
#         print("Sorry, we don't have " + requested_topping + ".")
# print("\nFinished making your pizza!")
#
# Hello Admin: создайте список из пяти и более имен пользователей, включающий имя
# ‘admin’. Представьте, что вы пишете код, который выводит приветственное сообщение для
# каждого пользователя после его входа на сайт. Переберите элементы списка и выведите
# сообщение для каждого пользователя.
# • Для пользователя с именем 'admin’ выведите особое сообщение — например: «Hello
# admin, would you like to see a status report?»
# • В остальных случаях выводите универсальное приветствие — например: «Hello Eric,
# thank you for logging in again».

# names_list = ['Liam', 'Olivia', 'Noah', 'Emma', 'admin']
# del names_list[:]
# print(len(names_list))
# names_list.append('Liam')
# if len(names_list) <= 0:
#     print("We need to find some users!")
# else:
#     for name in names_list:
#         if name == 'admin':
#             print("Hello " + name + ", would you like to see a status report?")
#         else:
#             print("Hello " + name, ", thank you for logging in again")

# Проверка имен пользователей: выполните следующие действия для создания про-
# граммы, моделирующей проверку уникальности имен пользователей.
# • Создайте список current_users, содержащий пять и более имен пользователей.
# • Создайте другой список new_users, содержащий пять и более имен пользователей.
# Убедитесь в том, что одно или два новых имени также присутствуют в списке current_
# users.
# • Переберите список new_users и для каждого имени в этом списке проверьте, было ли
# оно использовано ранее. Если имя уже использовалось, выведите сообщение о том,
# что пользователь должен выбрать новое имя. Если имя не использовалось, выведите
# сообщение о его доступности.
# • Проследите за тем, чтобы сравнение выполнялось без учета регистра символов. Если
# имя 'John’ уже используется, в регистрации имени ‘JOHN’ следует отказать.

# current_users = ["Asylbek", 'John', 'Rast', 'Nick', 'Mike']
# new_users = ['Liam', 'Olivia', 'Noah', 'Emma', 'admin', 'Mike', 'ASYLBEK']
# for new_user in new_users:
#     if new_user.upper().title() in current_users:
#         print("You must change the " + new_user + ", because this name already used")
#     else:
#         print("Welcome " + new_user)

# Порядковые числительные: порядковые числительные в английском языке заканчива-
# ются суффиксом th (кроме 1st, 2nd и 3rd).
# • Сохраните числа от 1 до 9 в списке.
# • Переберите элементы списка.
# • Используйте цепочку if-elif-else в цикле для вывода правильного окончания числи-
# тельного для каждого числа. Программа должна выводить числительные «1st 2nd 3rd
# 4th 5th 6th 7th 8th 9th», причем каждый результат должен располагаться в отдельной
# строке.

# numbers = [x for x in range(1,10)]
# print(numbers)
# for number in numbers:
#     if number == 1:
#         print(str(number) + 'st')
#     elif number == 2:
#         print(str(number) + 'nd')
#     elif number == 3:
#         print(str(number) + 'rd')
#     else:
#         print(str(number) + 'th')


# Словари
alien_0 = {}