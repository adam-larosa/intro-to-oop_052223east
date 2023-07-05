# Object Oriented Python

## Setup
* `pipenv install` will allow us to use the `ipdb` library.
* `pipenv shell` will bring us to an environment with `ipdb`.
* Once in that shell running `python run.py` will bring us to a prompt where our classes are in scope.


## Objectives

* Define `object` in programming domain 
    - OOP: Organize code like real objects
    - Object = data + functions/methods
* Create a class and instantiate an instance of the class
    - Invoking the class, e.g. `Cat()`
    - Saving to a variable: `c1 = Cat()`
* Explain the difference between a class and an instance
    - Class : Instance as Blueprint : House
    - Class : Instance as Factory : Car
* Pass arguments to `__init__` by defining an dunder init method in class
    - Python knows to look for the `__init__` method when an instance is created.
    - e.g.  `c1 = Cat( 'Luke', 5 )`
* Create instance methods
    - Same function syntax as with normal Python functions, only now all methods will have one parameter of `self`, which represents the instance.
* Define attribute readers and writers using the `property` function.
    - A `property` is a way to access instance attributes that involve additional logic. 
* Represent the instance with another dunder method: `__repr__`.
    - The `__repr__` method is used when one wants to change how an instance is viewed, e.g. when passed as an argument to `print`