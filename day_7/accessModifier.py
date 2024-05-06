# By default the access modifiers don't exist in python this is just a workaround approach to tell people they shouldn't access these properties

class Employee:
    def __init__(self):
        self.name = "Harvey"
        # in order to set a property as private we add __ before its name like this
        # now it is set to private
        self.__nickname = "Big Game"
        # to show a protected access property we use single _
        self._profession = "Lawyer"

a = Employee()
# this is how we normally use class properties
print(a.name)

# this wont work since it is a private property
# print(a.__nickname)

# exception is like this, It'll work 

print(a._Employee__nickname)

# This returns all the kinds of things/methods that can be performed on a 
# print(a.__dir__())

