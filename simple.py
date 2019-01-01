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

# pattern = re.compile(r'\bHa')
# <re.Match object; span=(67, 69), match='Ha'>
# <re.Match object; span=(70, 72), match='Ha'>

# pattern = re.compile(r'^Start')
# <re.Match object; span=(0, 5), match='Start'>
#
# matches = pattern.finditer(sentence)
#
# for match in matches:
#     print(match)

# pattern = re.compile(r'end$')
# <re.Match object; span=(41, 44), match='end'>
# matches = pattern.finditer(sentence)

# for match in matches:
#     print(match)
#
# pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
# matches = pattern.finditer(text_to_search)
#
# for match in matches:
#     print(match)
# <re.Match object; span=(194, 206), match='321-555-4321'>
# <re.Match object; span=(207, 219), match='123.555.1234'>
# <re.Match object; span=(220, 232), match='123*555*1234'>
# <re.Match object; span=(233, 245), match='800-555-1234'>
# <re.Match object; span=(246, 258), match='900-555-1234'>

# pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')
# <re.Match object; span=(233, 245), match='800-555-1234'>
# <re.Match object; span=(246, 258), match='900-555-1234'>
#
# matches = pattern.finditer(text_to_search)
#
# for match in matches:
#     print(match)

# pattern = re.compile(r'Mr\.?')
# <re.Match object; span=(260, 263), match='Mr.'>
# <re.Match object; span=(272, 274), match='Mr'>
# <re.Match object; span=(290, 292), match='Mr'>
# <re.Match object; span=(304, 307), match='Mr.'>
# matches = pattern.finditer(text_to_search)
#
# for match in matches:
#     print(match)

# pattern = re.compile(r'Mr\.?\s[A-Z]')
# <re.Match object; span=(260, 265), match='Mr. S'>
# <re.Match object; span=(272, 276), match='Mr S'>
# <re.Match object; span=(304, 309), match='Mr. T'>
# matches = pattern.finditer(text_to_search)
#
# for match in matches:
#     print(match)

# pattern = re.compile(r'Mr\.?\s[A-Z]\w+')
# # <re.Match object; span=(260, 271), match='Mr. Schafer'>
# # <re.Match object; span=(272, 280), match='Mr Smith'>
# matches = pattern.finditer(text_to_search)
#
# for match in matches:
#     print(match)

#OTWIERANIE PLIKÓW I CZYTANIE Z NICH

with open('data.txt', 'r') as f:
    contents = f.read()

    pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
    matches = pattern.finditer(contents)

    for match in matches:
        print(match)

