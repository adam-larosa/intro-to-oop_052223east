
# A "class" is nothing more than a "blueprint" to create "instances", which are
# one of the things the blueprint is trying to make

# So a "class" creates "instances", also called "objects"

class Cat:
    # Cat.all will be accessable to ALL the instances
    all = []

    # this special method runs once every time an instance is created
    def __init__( self, name_given, age_given, owner_instance ):
        self.owner = owner_instance
        self.name = name_given
        self._age = age_given
        # every time an instance is made, we can append a reference to it 
        # in the "all" list
        Cat.all.append( self )

    def get_age( self ):
        return self._age

    def set_age( self, new_age ):
        if new_age > 30:
            print( "cat's don't live that long!" )
        else:
            self._age = new_age
    
    age = property( get_age, set_age )


    # an instance method, a method we can call on an instance!
    # e.g. c1.meow()
    def meow( self ):
        print( f'I am {self.name}, mee-yaow' )


    def __repr__( self ):
        return f'<Cat name="{self.name}" age={self.age}>'


class Owner:
    def __init__( self, name ):
        self.name = name

    @property
    def cats( self ):
        # cat_list = []
        # for cat_instance in Cat.all:
        #     if cat_instance.owner == self:
        #         cat_list.append( cat_instance )
        # return cat_list


#          this is what ends up
#            in the new list
#                 |
#                 v    
        return [ cat for cat in Cat.all if cat.owner == self ]
#                         ^
#                         |
#                    a variable we 
#                  are declaring to 
#                 represent one of the
#                   cats in Cat.all


    def __repr__( self ):
        return f'<Owner name="{self.name}">'