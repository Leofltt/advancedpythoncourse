def greetings(func):
    func()

def hi():
    print('Hi')

greetings(hi)

def dumb(func):
    return func

ok = dumb(hi)
ok()

# greetings2 is decorating func
def greetings2(func):
    def wrapper():
        print('Hi 2')
        func()
    return wrapper

hi_2 = greetings2(hi)
hi_2()

@greetings2
def hi_deco():
    print('Hi 3')

hi_deco()