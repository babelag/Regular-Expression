import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Znaki specjalne które pomijamy, przed nimi należy użyć \):

. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''


sentence = 'Start a sentence and then bring it to an end'

#SZUKANIE W TEKŚCIE I ZWROTKI

#pattern = re.compile(r'abc')
#<re.Match object; span=(1, 4), match='abc'>
#print(text_to_search[1:4])


# pattern = re.compile(r'coreyms\.com')
# <re.Match object; span=(181, 192), match='coreyms.com'>

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

