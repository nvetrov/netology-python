'''
Учитывая целое число, выполните следующие условные действия:

Если нечетное, выведите Weird
Если четно и находится в диапазоне от  2 до 5, выведите Not Weird
Если четно и находится в диапазоне от 6 до 20, выведите Weird
Если даже 20 и больше, выведите Not Weird

'''
n = int(input())

if not n % 2 == 0:
    print('Weird')  # Если нечетное, выведите Weird
elif n % 2 == 0:
    if 2 <= n <= 5:
        print('Not Weird')
    if 6 <= n <= 20:
        print('Weird')
    if n > 20:
        print('Not Weird')

# print(True and True)
# print(True and False)
# print(True or False)
# print(not True)


# Дана переменная, в которой хранится шестизначное число (номер проездного билета).
# Напишите программу, которая будет определять, является ли данный билет "счастливым".
# Билет считается счастливым, если сумма первых трех цифр совпадает с суммой последних трех цифр номера.

#
# happy_ticket = input()
#
# # happy_ticket = happy_ticket.split()
# a = (happy_ticket[:3])
# b = (happy_ticket[3:])
#
# if int(a[0]) + int(a[1]) + int(a[2]) == int(b[0]) + int(b[1]) + int(b[2]):
#     print('Билет счастливый!')
# else:
#     print('No')
