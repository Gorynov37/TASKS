""" 1 """
# def unmix(s: str):
#     new_s = ""
#     for i in range(1,len(s),2):
#         new_s += s[i] + s[i-1]
#     if len(s) % 2 == 1 :
#         new_s += s[len(s)-1]
#     return new_s
# print(unmix(input()))

""" 2 """
# def noYelling(s: str):
#     i = len(s)-1
#     while ((s[i-1] == '?') & (s[i] == '?')) | ((s[i-1] == '!') & (s[i] == '!')) | ((s[i-1] == '.') & (s[i] == '.')):
#         i-=1
#     return s[:i+1]
# print(noYelling(input()))

""" 3 """
# def xPronounce(s: str):
#     new_s = ' ' + s + ' '
#     # if new_s.startswith("x "):
#     #     new_s = "ecks" + new_s[1:]
#     # elif new_s.startswith("x"):
#     #     new_s = "z" + new_s[1:]
#     # if new_s.endswith(" x"):
#     #     new_s = new_s[:-1] + "ecks"
#     new_s = new_s.replace(" x ", " ecks ")
#     new_s = new_s.replace(" x", " z")
#     new_s = new_s.replace("x", "cks")
#     return new_s.strip()
# print(xPronounce(input()))

""" 4 """
# def largestGap(m: list):
#     m.sort()
#     lg = 0
#     for i in range(len(m)-1):
#          lg = max(m[i+1] - m[i], lg)
#     return lg
# m = []
# n = int(input())
# {m.append(int(input())) for i in range(n)}
# print(largestGap(m))

""" 5 """
# def sortInt(n: int):
#     s = str(n)
#     m = list(s)
#     m.sort()
#     s = ''.join(m);
#     return n - int(s)
# print(sortInt(int(input())))

""" 6 """
# def commonLastVowel(s: str):
#     letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
#     d = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0, 'y': 0}
#     for i in range(len(s)-1):
#         if (s[i].lower() in d) & (letters.find(s[i+1]) == -1):
#             d[s[i].lower()] = d[s[i].lower()] + 1
#     if s[-1].lower() in d:
#         d[s[-1].lower()] = d[s[-1].lower()] + 1
#     return max(d, key=d.get)
# print(commonLastVowel(input()))

""" 7 """
# def memeSum(a: int, b: int):
#     s1 = str(a)
#     s2 = str(b)
#     s = ''
#     l = max(len(s1), len(s2))
#     s1 = '0' * (l - len(s1)) + s1
#     s2 = '0' * (l - len(s2)) + s2
#     for i in reversed(range(l)):
#         s = str( int(s1[i]) + int(s2[i]) ) + s
#     return s
# print(memeSum(int(input()),int(input())))

""" 8 """
# def unrepeated(s: str):
#     m = []
#     for i in s:
#         if i not in m:
#             m.append(i)
#     return ''.join(m)
# print(unrepeated(input()))

""" 9 """
# def digitsCount(n: int):
#     if n//10 == 0:
#         return 1
#     else:
#         return digitsCount( n//10 ) + 1
# print(digitsCount(int(input())))

""" 10 """
# def longestRun(m: list):
#     n = 0
#     p = 1
#     n1 = 1
#     for i in range(len(m)-1) :
#         if m[i+1] == m[i] + p:
#             n1 += 1
#             n = max(n1, n)
#         elif m[i+1] == m[i] - p:
#             n1 = 2
#             p = -p
#             n = max(n1, n)
#         else:
#             n1 = 1
#             n = max(n1, n)
#     return n
# m = []
# n = int(input())
# {m.append(int(input())) for i in range(n)}
# print(longestRun(m))
