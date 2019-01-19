class Test:
    a='Hello World'
    def __init__(self):
        Test.a = 'Hell'
        try:
            print(a)
            print(1)
        except:
            print(Test.a)
            print(2)
    def p(self):
        print(Test.a)

t = Test()
t.p()
