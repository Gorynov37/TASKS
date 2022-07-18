import math
import re

""" 1 """
# def checkPerfect(n: int):
#     s = 1
#     for i in range(2, int(math.sqrt(n)+1)):
#         if n % i == 0:
#             s += i + n//i
#     return s == n
# print(checkPerfect(int(input())))

""" 2 """
# def isKaprekar(n: int):
#     s = str(n*n)
#     mid = len(s)//2
#     if len(s) != 1:
#         return int(s[:mid]) + int(s[mid:]) == n
#     else:
#         return n*n == n
# print(isKaprekar(int(input())))

""" 3 """
# def nextPrime(n: int):
#     if n <= 2:
#         return 2
#     m = list(range(2,2*n+1))
#     for i in m:
#         if i != 0:
#             for j in range(2*i, 2*n+1, i):
#                 m[j-2] = 0
#     n1 = n
#     while m[n1-2] == 0:
#         n1 += 1
#     return n1
# print(nextPrime(int(input())))

""" 4 """
# def wordProcessor(n: int, k: int, s: str):
#     m = s.strip().split()
#     ans = ""
#     lenth = 0
#     for i in m:
#         if len(i) + lenth > k:
#             lenth = len(i)
#             ans += '\n' + i
#         else:
#             lenth += len(i)
#             if ans != "":
#                 ans += ' '
#             ans += i
#     return ans
# print(wordProcessor(int(input()),int(input()),input()))

""" 5 """
# def mySplit(s: str):
#     d = {'(' : 1, ')': -1}
#     p = 0
#     m = []
#     s1 = ''
#     for i in s:
#         p += d[i]
#         s1 += i
#         if p == 0:
#             m.append(s1)
#             s1 = ''
#     return m
# print(mySplit(input()))

""" 6 """
# def toStarShorthand(s: str):
#     n = 0
#     s1 = ''
#     ans = ""
#     for i in s:
#         if i == s1:
#             n += 1
#         else:
#             ans += s1
#             if n > 1:
#                 ans += f"*{n}"
#             s1 = i
#             n = 1
#     ans += s1
#     if n > 1:
#         ans += f"*{n}"
#     return ans
# print(toStarShorthand(input()))

""" 7 """
# def doesRhyme(s1: str, s2: str):
#     m = ['a', 'e', 'i', 'o', 'u', 'y']
#     word1 = s1.strip().split()[-1].lower()
#     word2 = s2.strip().split()[-1].lower()
#     vowels1 = ''
#     vowels2 = ''
#     for i in word1:
#         if i in m:
#             vowels1 += i
#     for i in word2:
#         if i in m:
#             vowels2 += i
#     return vowels1 == vowels2
# print(doesRhyme(input(),input()))

""" 8 """
# def encrypt(s: str):
#     m = [ord(s[0])]
#     for i in range(1, len(s)):
#         m.append(ord(s[i]) - ord(s[i-1]))
#     return m
# def decrypt(m: list):
#     s = chr(m[0])
#     for i in range(1, len(m)):
#         s += chr(ord(s[-1]) + m[i])
#     return s
# print(encrypt("Sunshine"))
# print(decrypt([72, 33, -73, 84, -12, -3, 13, -13, -68]))

""" 9 """
# def sameVowelGroup(m: list):
#     d = ['a', 'e', 'i', 'o', 'u', 'y']
#     m0 = ""
#     ans = []
#     for i in m[0]:
#         if i in d:
#              m0 += i
#     vowels = set(m0)
#     for j in m:
#         m0 = ""
#         for i in j:
#             if i in d:
#                 m0 += i
#         if vowels == set(m0):
#             ans.append(j)
#     return ans
# print(sameVowelGroup(["hoops", "chuff", "bot", "bottom"]))

""" 10 """
# def numToEng(n: int):
#     d = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
#          10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
#          17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
#          60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}
#     n1 = n % 10
#     n10 = n % 100 - n1
#     n100 = n // 100
#     ans = ''
#     if n100 != 0:
#         ans += f"{d[n100]} hundred "
#     if n10 + n1 <= 20:
#         ans += d[n10 + n1]
#     else:
#         ans += d[n10] + ' ' + d[n1]
#     if n == 0:
#         ans = 'zero'
#     return ans
#
# def numToRus(n: int):
#     d = {0: '', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять',
#          10: 'десять', 11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать', 14: 'четырнадцать', 15: 'пятнадцать',
#          16: 'шестнадцать', 17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать', 20: 'двадцать', 30: 'тридцать',
#          40: 'сорок', 50: 'пятьдесят', 60: 'шестьдесят', 70: 'семьдесят', 80: 'восемьдесят', 90: 'девяносто',
#          100: 'сто', 200: 'двести', 300: 'триста', 400: 'четыреста', 500: 'пятьсот', 600: 'шестьсот', 700: 'семьсот',
#          800: 'восемьсот', 900: 'девятьсот'}
#     ans = ''
#     n1 = n % 10
#     n10 = n % 100 - n1
#     n100 = n - n10 - n1
#     if n100 != 0:
#         ans += f"{d[n100]} "
#     if n10 + n1 <= 20:
#         ans += d[n10 + n1]
#     else:
#         ans += d[n10] + ' ' + d[n1]
#     if n == 0:
#         ans = 'ноль'
#     return ans
#
# print(numToEng(int(input("Eng: "))))
# print(numToRus(int(input("Rus: "))))

""" 11 """
# def hexLattice(n: int):
#     if n < 1:
#         return "Invalid"
#     p = int(math.sqrt((n-1)//3)) + 1
#     if n != p*(p-1)*3 + 1:
#         return "Invalid"
#     s = ""
#     for i in range(p):
#         s += (p-i)*' ' + (p+i)*"o " + (p-i-1)*' ' + '\n'
#     for i in range(p-1):
#         s += (2+i)*' ' + (2*(p-1)-i)*"o " + (1+i)*' '
#         if i != p-2:
#             s += '\n'
#     return s
# print(hexLattice(int(input())))

""" 12 """
# def translateWord(s: str):
#     s1 = ''
#     if s[0] in "aeiouAEIOU":
#         s1 = s + 'yay'
#     else:
#         s1 = s[1:] + s[0].lower() + "ay"
#     if s.istitle():
#         s1 = s1.capitalize()
#     return s1
#
# def translateSentence(s: str):
#     for i in re.findall(r'\w+', s):
#         s = s.replace(i, translateWord(i))
#     return s
#
# print(translateSentence(input()))

""" 13 """
# def longestNonrepeatingSubstring(s: str):
#     maxSubstr = ''
#     substr = ''
#     it1 = 0
#     it2 = 0
#     while it2 != len(s):
#         if s[it2] in substr:
#             it1 += 1
#             substr = s[it1: it2+1]
#         else:
#             substr += s[it2]
#             it2 += 1
#             if len(substr) > len(maxSubstr):
#                 maxSubstr = substr
#     return maxSubstr
# print(longestNonrepeatingSubstring(input()))

""" 14 """
# def convertToRoman(n: int):
#     ans = ''
#     d = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I', 0: ''}
#     for i in range(4):
#         k10 = (n // 10**i) % 10
#         k5 = k10 % 5
#         if k5 != 4:
#             ans = d[(k10-k5) * 10**i] + k5 * d[10**i] + ans
#         else:
#             ans = d[10**i] + d[(k10 + 1) * 10**i] + ans
#     return ans
# print(convertToRoman(int(input())))

""" 15 """
# def formula(s: str):
#     m = [i.strip() for i in s.split("=")]
#     m0 = []
#     for i in m:
#         m1 = re.findall(r"\d+", i)
#         m2 = re.findall(r"[%/*+-]", i)
#         if len(m1) == 1:
#             m0.append(int(m1[0]))
#         elif m2[0] == '%':
#             m0.append(int(m1[0]) % int(m1[1]))
#         elif m2[0] == '/':
#             m0.append(int(m1[0]) // int(m1[1]))
#         elif m2[0] == '*':
#             m0.append(int(m1[0]) * int(m1[1]))
#         elif m2[0] == '+':
#             m0.append(int(m1[0]) + int(m1[1]))
#         elif m2[0] == '-':
#             m0.append(int(m1[0]) - int(m1[1]))
#     return len(set(m0)) == 1
# print(formula(input()))
