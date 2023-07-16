# # func4
# def triangl(a):
#     P = 3 * a
#     s = 0.43301 * a ** 2
#     return P, s
# print(triangl(5))

# # func8
# def addrigthdigit(k, r):
#     k=str(k)
#     r=str(r)
#
#     return int(k + r)
# print(addrigthdigit(5, 7))

# # func12
# def sort(a, b, c):
#     k = max(a, b, c)
#     x = min(a, b, c)
#     return x, (a + b + c) - x - k, k
#
#
# print(sort(5, 10, 9))

#func16

#func20
# def trianglp(a, b):
#     return a + b + (a * a + b * b) ** 0.5
#
#
# print(trianglp(3, 4))

# # func24
# def even(a):
#     if a % 2 == 0:
#         return True
#     else:
#         return False
#
#
# print(even(5))
# print(even(1548945))
# print(even(10))


# # func28
# def fun(n):
#     k = 2
#     while k * k <= n:
#         if n % k == 0:
#             s = 1
#             return False
#             break
#         k += 1
#
#     return True
#
#
# mass = [int(i) for i in input().split()]
# s = 0
# for xx in mass:
#     s += fun(xx)
# print(s)

# # func32
# def torad(n):
#     return n / 180

# # fun36
# def tofib(n):
#     mass = [0, 1, 1]
#     while len(mass) < n:
#         mass.append(mass[-1] + mass[-2])
#     return mass[-1]
#
#
# print(tofib(8))

#func40

# def tob(n, x):
#     s = 1
#     k = 1
#     for xx in range(n):
#         k *= (xx + 1)
#         s += x ** xx / k
#     return s
#
#
# print(tob(5, 5))

