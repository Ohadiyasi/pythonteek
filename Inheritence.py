class Parent:
    def sayHi(self):
        print("Hello, World!")

var = Parent()
#var.sayHi()



class Child(Parent):
    pass


sample = Child()
sample.sayHi()
