'''8.1'''

September = {'Dmitry', 'Oleh', 'Andrii', 'Lex', 'Philip', 'Ivan', 'Ilia', 'Taras'}
October = {'Dmitry', 'Taras', 'Andrii', 'Lex', 'Vova', 'Kyrulo', 'Ostap', 'Prohor'}
full_debtors = September.intersection(October)
print(full_debtors)
'''Должники за октябрь,без долга за сентябрь'''
print(October.difference(September))

'''8.2'''

# x = {'write': 'W', 'read': 'R', 'execute': 'X'}
# d = {}
# for i in range(int(input('Enter number :'))):
#     a, *b = input().split()
#     d[a] = set(b)
# for i in range(int(input('Enter number :'))):
#     a, b = input().split()
#     if x[a] in d[b]:
#         print('OK')
#     else:
#         print('Access denied')
#
