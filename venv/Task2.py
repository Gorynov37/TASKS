""" 1 """
# def points(a: int, b: int):
#     return a*2 + b*3
#
# a = int(input())
# b = int(input())
# print(points(a, b))

""" 2 """
# def divisibleByFive(a: int):
#     return a%5 == 0
# a = int(input())
# print(divisibleByFive(a))

""" 3 """
# def divisibleByFive(n: int, w: int, h: int):
#     return n // (w * h)
# n = int(input())
# w = int(input())
# h = int(input())
# print(divisibleByFive(n, w, h))

""" 4 """
# def profitableGamble(prob: float, prize: float, pay: float):
#     return prob * prize > pay
# n = float(input())
# w = float(input())
# h = float(input())
# print(profitableGamble(n, w, h))

""" 5 """
# def mod(a: int, b: int):
#     return a - (a//b) * b
# a = int(input())
# b = int(input())
# print(mod(a, b))

""" 6 """
# def oppositeHouse(n: int, L: int):
#     return 2*L+1 - n
# a = int(input())
# b = int(input())
# print(oppositeHouse(a, b))

""" 7 """
# def differenceMaxMin(M: list):
#     return max(M) - min(M)
# n = int(input())
# m = []
# for i in range(n):
#     m.append(int(input()))
# print(differenceMaxMin(m))

""" 8 """
# def equal(a: int, b: int, c: int):
#     count = 0
#     if a==b or b==c or a==c:
#         count+=2
#     if a==b and b==c:
#         count+=1
#     return count
# n = int(input())
# w = int(input())
# h = int(input())
# print(equal(n, w, h))

""" 9 """
# def getXO(s: str):
#     x = 0
#     o = 0
#     for i in s:
#         if i == 'x':
#             x+=1
#         if i == 'o':
#             o += 1
#     return x==o
# print(getXO(input()))

""" 10 """
# def bomb(s: str):
#     if s.lower().find("bomb") != -1:
#         return "DUCK!"
#     else:
#         return "Relax, there's no bomb."
# print(bomb(input()))
