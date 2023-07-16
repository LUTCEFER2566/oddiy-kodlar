# #string26
# n = int(input())
# satr = input()
# if len(satr)>n:
#     for har in satr:
#         if len(satr)<=n:
#             break
#         else:
#             satr=satr.replace(har, '')
#             print(satr)

# #satr27
# n1, n2 = map(int, input().split())
# s1, s2 = map(str, input().split())
# satr = ''
# for xx in range(n1):
#     satr += s1[xx]
# for xx in range(len(s2) - n2, len(s2) ):
#     satr += s2[xx]
# print(satr)


# #string28
# satr = ''
# c = input()
# s = input()
# for xx in s:
#     satr += xx
#     if xx==c:
#         satr +=xx
# print(satr)

# #string29
# c=input()
# s1,s2=map(str,input().split())
# satr =''
# for xx in s1:
#     if xx==c:
#         satr+=s2
#     satr+=xx
# print(satr)

# #string30
# c=input()
# s1,s2=map(str,input().split())
# satr =''
# for xx in s1:
#     satr+=xx
#     if xx==c:
#         satr+=s2
# print(satr)

# #string31
# s1, s2 = map(str, input().split())
# print(s2 in s1)

# #string32
# s1, s2 = map(str, input().split())
# print(s1.count(s2))




# #string41
# a = input().split()
# print(len(a))

# #string42
# a = input().split()
# s = 0
#
# for xx in range(len(a)):
#     for dnd in range(xx + 1, len(a)):
#         if a[xx][0] == a[dnd][0] and a[xx][-1] == a[dnd][-1]:
#             s += 1
# print(s)


# #string53
# tin = '.?!,()-:;"'
# son = 0
# a = input()
# for xx in a:
#     if xx in tin:
#         son += 1
# print(son)

# # string54
# kat = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# a = input()
# son = 0
# for xx in a:
#     if xx in kat:
#         son += 1
# print(son)

# # string55
# a = input().split()
# maks = ''
# for xx in a:
#     if len(xx) > len(maks):
#         maks = xx
# print(maks)

# #string56
# a = input().split()
# k = len(a)
# maks = a[-1]
# for xx in range(k-1, -1, -1):
#     if len(a[xx]) < len(maks):
#         maks = a[xx]
# print(maks)

# # string57
# a = input().split(' ')
# print(a)
# for xx in a:
#     if ' ' in xx:
#         a.remove(xx)
# for yy in a:
#     print(yy, end=' ')
#
# a = input().split()
# for xx in a:
#     print(xx, end=' ')

#string58
# a = input()
# satr = ''
# for xx in range(len(a) - 1, -1, -1):
#     if a[xx] == chr(92):
#         break
#     satr += a[xx]
# new = ''
# for kk in range(len(satr) - 1, -1, -1):
#
#     if satr[kk] == '.':
#         break
#     new += satr[kk]
# print(new)

# #string59
# a =input()
# x = a.find('.')
# print(a[x+1:])

# #string60
# a = input()
# aa = a.find(':')
# satr=''
# for xx in range(aa+2, len(a)):
#     if a[xx] == chr(92):
#         break
#     satr+=a[xx]
# print(satr)

# # string61
# a = input()
# xsa = ':' + chr(92)
# a = a.replace(xsa, '')
# aa = a.find(':')
# satr = ''
# for xx in range(aa + 2, len(a)):
#     if a[xx] == chr(92):
#         break
#     satr += a[xx]
# print(satr)

satr = input()
n = ''
och=0
yop=0
s=1

for xyz in satr:
    if xyz=='(':
        och+=1
        n +='('
    elif xyz==')':
        yop+=1
        n+=')'
    if och>=yop :
        s*=1
    else:
        s*=0
if och==yop and s==1 and n.startswith('('):
    print("TRUE")
else:
    print("FALSE")