import ipdb
import random
from lib.classes import Cat, Owner

o1 = Owner( 'adam' )
o2 = Owner( 'ix' )

c1 = Cat( 'Luke', 5, o1 )
c2 = Cat( 'Murphy', 3, o1 )
c3 = Cat( 'Rose', 12, o2 )

# to exit, we "continue" the debugger by typing "c" then hitting enter
ipdb.set_trace()
print( 'bye bye!' )