# # file=open('pi.txt')
# # pi=file.read()
# # print(pi)
# # file.close()
# with open('pi.txt','r') as f:
#     print(f.read())
# with open('pi.txt','w') as f:
#     f.write('alik')
d=1
try (with open('k.txt','r') as f):
        print(f.read())
        d=(f.read())+1
except with open('k.txt','w') as f:
    f.write(d)