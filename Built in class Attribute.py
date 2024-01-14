class Test:
    'This is doc Statement'
    def __init__(self):
        print("Hello")
print(Test.__doc__)  #Docstring
print(Test.__name__)
print(Test.__module__)
print(Test.__bases__)
print(Test.__dict__)

