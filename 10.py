a = input()
c = 0
for x in a:
    if x == '1':
        c += '1'
if c % 2 == '0':
    a += '0'
else:
    a += '1'
print(a)
