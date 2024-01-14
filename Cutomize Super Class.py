class Super:
    def method(self):
        print("In Super Method")
    def delegate(self):
        self.action()
class Inheritor(super):
    pass
class Inheritor(super):
    def method(self):
        print("In Replacer Method")
class Extender(super):
    def method(self):
        super.method(self)
        print("In Extender Method")
class Provider(super):
    def action(self):
        for klass in (Inheritor,Replacer,Extender):
            priny("\n"+kclass.__name__+'---')
            print('in Provider.action')
            klass.method()
            print("\n Provider")
x=Provider()
x.delegate()

            
