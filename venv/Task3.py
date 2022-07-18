""" 1 """
# def rps(p1: str, p2: str):
#     m = ["rock", "scissors", "paper"]
#     if p1 == p2:
#         return "TIE"
#     elif p1 == m[m.find(p2) - 1]:
#         return "Player 1 wins"
#     else:
#         return "Player 2 wins"
# print(rps(input(), input()))

""" 2 """
# def warOfNumbers(m: list):
#     sum = 0
#     for i in m:
#         sum += ((-1)**(i%2)) * i
#     return sum
# m = []
# n = int(input())
# {m.append(int(input())) for i in range(n)}
# print(warOfNumbers(m))

""" 3 """
# def reverseCase(s: str):
#     for i in s:
#         if i.islower():
#             i.upper()
#         else:
#             i.lower()
#     return s
# print(reverseCase(input()))

""" 4 """
# def inatorInator(s: str):
#     letters = "AEIOUYaeiouy"
#     if letters.find(s[len(s) - 1]) == -1:
#         return s + f"inator {len(s)}000"
#     else:
#         return s + f"-inator {len(s)}000"
# print(inatorInator(input()))

""" 5 """
# def doesBrickFit(a: int, b: int, c: int, h: int, w: int):
#     m = [a, b, c]
#     n = [h, w]
#     m.sort()
#     n.sort()
#     return m[0] <= n[0] and m[1] <= n[1]
# print(doesBrickFit(1, 2, 2, 1, 1))

""" 6 """
# def totalDistance(L: float, r: float, count: int, b: bool):
#     return 100*L/(r * (1 + count*0.05 + int(b)*0.1))
# print(totalDistance(70, 7, 10, True))

""" 7 """
# def mean(m: list):
#     sum = 0
#     for i in m:
#         sum += i
#     return sum / len(m)
# print(mean([1, 0, 4, 5, 2, 4, 1, 2, 3, 3, 3]))

""" 8 """
# def parityAnalysis(a: int):
#     sum = 0
#     a1 = a
#     while a1 != 0:
#         sum += a1 % 10
#         a1 //= 10
#     return a%2 == sum%2
# print(parityAnalysis(12))

""" 9 """
# def sevenBoom(m: list):
#     for i in m:
#         if str(i).find("7") != -1:
#             return "Boom!"
#     return "there is no 7 in the array"
# print(sevenBoom([2, 55, 60, 97, 86]))

""" 10 """
# def cons(m: list):
#     m.sort()
#     return (list(range(min(m),max(m)+1))) == m
# print(cons([5, 1, 4, 3, 2, 5]))
