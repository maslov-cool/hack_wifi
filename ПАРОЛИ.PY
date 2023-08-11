# функции для подбора паролей
'''def generate_password1(length):
    s = ''
    for i in range(length):
        s += [choice(ascii_uppercase), choice(ascii_lowercase), choice(digits), choice(punctuation)][randrange(3)]
    return s

def generate_password2(length):
    s = ''.join([[choice(ascii_uppercase), choice(ascii_lowercase), choice(digits), choice(punctuation)][randrange(3)] for i in range(length)])
    cnt, flag1 = 0, False
    while not flag1:
        if cnt != 0:
            s = ''.join([[choice(ascii_uppercase), choice(ascii_lowercase), choice(digits), choice(punctuation)][randrange(3)] for i in range(length)])
            flag1 = False
        for i in s:
            if str(i) in ascii_uppercase:
                flag1 = True
        cnt += 1
    return s

def generate_password3(length):
    s = ''.join([[choice(ascii_uppercase), choice(ascii_lowercase), choice(digits), choice(punctuation)][randrange(3)] for i in range(length)])
    cnt, flag1, flag2 = 0, False, False
    while not (flag1 and flag2):
        if cnt != 0:
            s = ''.join([[choice(ascii_uppercase), choice(ascii_lowercase), choice(digits), choice(punctuation)][randrange(3)] for i in range(length)])
            flag1, flag2 = False, False
        for i in s:
            if str(i) in ascii_uppercase:
                flag1 = True
            if str(i) in ascii_lowercase:
                flag2 = True
        cnt += 1
    return s

def generate_password4(length):
    s = ''.join([[choice(ascii_uppercase), choice(ascii_lowercase), choice(digits), choice(punctuation)][randrange(3)] for i in range(length)])
    cnt, flag1, flag2, flag3 = 0, False, False, False
    while not (flag1 and flag2 and flag3):
        if cnt != 0:
            s = ''.join([[choice(ascii_uppercase), choice(ascii_lowercase), choice(digits), choice(punctuation)][randrange(3)] for i in range(length)])
            flag1, flag2, flag3 = False, False, False
        for i in s:
            if str(i) in ascii_uppercase:
                flag1 = True
            if str(i) in ascii_lowercase:
                flag2 = True
            if str(i) in digits:
                flag3 = True
        cnt += 1
    return s

def generate_password5(length):
    s = ''.join([[choice(ascii_uppercase), choice(ascii_lowercase), choice(digits), choice(punctuation)][randrange(3)] for i in range(length)])
    cnt, flag1, flag2, flag3, flag4 = 0, False, False, False, False
    while not (flag1 and flag2 and flag3 or flag4):
        if cnt != 0:
            s = ''.join([[choice(ascii_uppercase), choice(ascii_lowercase), choice(digits), choice(punctuation)][randrange(3)] for i in range(length)])
            flag1, flag2, flag3, flag4 = False, False, False, False
        for i in s:
            if str(i) in ascii_uppercase:
                flag1 = True
            if str(i) in ascii_lowercase:
                flag2 = True
            if str(i) in digits:
                flag3 = True
            if str(i) in punctuation:
                flag4 = True
        cnt += 1
    return s'''

