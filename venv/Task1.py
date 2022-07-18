""" 1 """
# login = input()
# if len(login) < 7:
#     print('Некорректный логин')
# else:
#     password = input()
#     boo = True
#     for a in password:
#         if ord(a) >= 48 & ord(a) <= 57:
#             boo = False
#     if boo | password.find('@') != -1:
#         print('Некорректный пароль')
#     else:
#         print('OK')

""" 2 """
# message = input()
# n = len(message) * 4
# n1 = n // 10
# n2 = n % 10
# print(f'{n1} р. {n2}0 коп.')

""" 3 """
# OldPW = input();
# a3_1 = int(OldPW[0])
# a3_2 = int(OldPW[1])
# a3_3 = int(OldPW[2])
# if a3_1 >= a3_3:
#     print(a3_1 + a3_2, a3_2 + a3_3, sep='')
# else:
#     print(a3_3 + a3_2, a3_2 + a3_1, sep='')

""" 4 """
# m = []
# for i in [0, 1, 2]:
#     m.append(input())
# m.sort()
# m.reverse()
# for i in m:
#     print(i)

""" 5 """
# FullSum = 0.0
# Sum = 0.0
# a5 = float(input())
# while a5 >= 0:
#     FullSum += a5
#     if a5 > 500:
#         Sum += a5 * 0.15
#     a5 = float(input())
# print(FullSum)
# print(round(Sum, 1))
# print(round(FullSum - Sum, 1))

""" 6 """
# n = int(input())
# i = 0
# while n % 2 == 0 and n > 0:
#     n//=2
#     i+=1
# if n == 1:
#     print(i)
# else:
#     print("НЕТ")

""" 7 """
# n = int(input())
# m = int(input())
# sym = str(input())
# print(sym * m)
# for i in range(n-2):
#     if n == 1:
#         print(sym)
#     else:
#         print(sym, ' ' * (m-2), sym, sep='')
# if n > 1:
#     print(sym * m)

""" 8 """
# n = int(input())
# a = int(input())
# b = 0
# while n > a:
#     n = a
#     a = int(input())
# n = a
# b = int(input())
# while n < b:
#     n = b
#     b = int(input())
# while n != 0:
#     n = int(input())
# print(a, b, b-a)

""" 9 """
# import random
#
# a = int(input())
# b = int(input())
# n = int(input())
# m = []
# count = 0
# s = ''
# for i in range(n):
#     x = random.randint(a, b)
#     if ((x // 10) % 10) % 2 == 0:
#         count += 1
#     m.append(x)
#     s+=str(x)+' '
# print(s)
# print(count)

""" 10 """
# import random
#
# n = int(input())
# m = []
# s = ''
# for i in range(n):
#     m.append(i+1)
# for i in range(n):
#     m.append(m.pop(random.randint(0,n-i-1)))
# for i in m:
#     s += str(i) + ' '
# print(s)
