'''6.1+++'''
# word = input('Enter your word:')
# a = word[::-1]
# if word == a:
#   print('yes')
# else:
#   print('no')

'''6.2++++'''
# text = input('enter your text :')
# word = input('enter your word :')
# if text.find(word) == -1:
#     print('no')
# else:
#     print('yes')


'''6.3+++'''
text = input('enter your text :')
text_str = text.startswith('abc')
if text_str:
    replaced_text = text.replace('abc', 'www')
    print(replaced_text)
else:
    s1 = text
    s2 = 'zzz'
    s3 = '{}{}'.format(s1, s2)
    print(s3)

'''6.4+++'''
# S = input('enter :')
# s = ''.join(x for x in S if not x.isdigit())
# print(s)

'''6.5+++'''
# post = input('enter your personal data :')
# if '@' in post and '.' in post:
#     print('yes')
# else:
#     print('no')

