#
# .       - Any Character Except New Line /każdy znak oprócz nowej lini
# \d      - Digit (0-9) / liczby 0-9
# \D      - Not a Digit (0-9) / kązda nie liczba 0-9 - każda duża litera neguje wyrażenie z małej
# \w      - Word Character (a-z, A-Z, 0-9, _)
# \W      - Not a Word Character
# \s      - Whitespace (space, tab, newline)
# \S      - Not Whitespace (space, tab, newline)
# \t      - TAB / tabulator
#
# \b      - Word Boundary /wstawiamy przed słowem zaczynającym się np. \bHa - i znajdzie nam 2 słowa
# \B      - Not a Word Boundary
# ^       - Beginning of a String /wstawiamy na początku stringa
# $       - End of a String /wstawiamy na końcu stringa
#
# []      - Matches Characters in brackets /wstawiamy np [-.] i wyszukuje nam tylko te znaki w tekscie
# [^ ]    - Matches Characters NOT in brackets
# |       - Either Or
# ( )     - Group
#
# Quantifiers:
# *       - 0 or More
# +       - 1 or More
# ?       - 0 or One
# {3}     - Exact Number
# {3,4}   - Range of Numbers (Minimum, Maximum)
#
#
# #### Sample Regexs ####
#
# [a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+