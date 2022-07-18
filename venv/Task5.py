import math

""" 1 """
# def takeDownAverage(m: list):
#     n = len(m)
#     s = 0
#     for i in m:
#         s += int( i.replace('%','') )
#     return f"{(s - 5*n*(n+1)) // n}%"
# m = []
# n = int(input())
# {m.append(input()) for i in range(n)}
# print(takeDownAverage(m))

""" 2 """
# def rearrange(s: str):
#     m1 = s.strip().split()
#     m = list(range(len(m1)))
#     for i in m1:
#         n = ''
#         s = ''
#         for j in i:
#             if j.isdigit():
#                 n += j
#             else:
#                 s += j
#         n = int(n)
#         m[n-1] = s
#     return ' '.join(m)
# print(rearrange(input()))

""" 3 """
# def maxPossible(a: int, b: int):
#     s = str(a)
#     m = list(str(b))
#     m.sort()
#     m.reverse()
#     for i in range(len(s)):
#         if (len(m) != 0):
#             if (m[0] > s[i]):
#                 s = s[:i] + m[0] + s[i+1:]
#                 m.remove(m[0])
#     return int(s)
# print(maxPossible(int(input()), int(input())))

""" 4 """
# def twoProduct(m: list, n: int):
#     for i in range(len(m)-1):
#         for j in range(i+1, len(m)):
#             if m[i]*m[j] == n:
#                 return [m[i], m[j]]
#     return []
# m = input().strip().split()
# m = [int(i) for i in m]
# n = int(input())
# print(twoProduct(m,n))

""" 5 """
# def isExact(n: int, p = 1):
#     if n == 1:
#         return [n, p]
#     elif n % (p+1) == 0:
#         m = isExact(n // (p+1), p+1)
#         if len(m) != 0:
#             return [n, m[1]]
#     return []
# print(isExact(int(input())))

""" 6 """
# def fractions(s: str):
#     dot = s.find('.')
#     bracket = s.find('(')
#     b = int('9'*(len(s) - bracket - 2) + '0'*(bracket - dot - 1))
#     a = int(s[:dot])*b + int(s[dot + 1: bracket] + s[bracket + 1: -1])
#     if  s[dot + 1: bracket] != '':
#         a -= int(s[dot + 1: bracket])
#     p = math.gcd(a,b)
#     a //= p
#     b //= p
#     return f"{a}/{b}"
# print(fractions(input()))

""" 7 """
# def sumsUp(m: list):
#     ans = []
#     for i in range(len(m)-1):
#         for j in range(i+1, len(m)):
#             if m[i] + m[j] == 8:
#                 l = [m[i], m[j]]
#                 l.sort()
#                 ans.append(l)
#     ans.sort()
#     return ans
# m = input().strip().split()
# m = [int(i) for i in m]
# print(sumsUp(m))

""" 8 """
# def isNew(n: int):
#     m = list(str(n))
#     m.sort()
#     i = 0
#     while (i < len(m)-1) & (m[i] == '0'):
#         i += 1
#     m[0], m[i] = m[i], m[0]
#     n1 = int(''.join(m))
#     return n == n1
# print(isNew(int(input())))
