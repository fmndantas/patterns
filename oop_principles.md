# Open-closed principle

* Classes, objects and methods should be _open_ 
for extension. but _closed_ for modification.

This means that software should be written in the **most
generalized way**, because this enable the addition
of new functionalities through only extension, without
any classes change.

# The inversion of control principle

* High levels modules should not be dependent on
low-levels modules; they should both be dependent 
on _abstractions_. Details should depend on abstractions
and not the other way around.

If a module depends on an another base module,
this dependency should be implemented through 
an interface; the interface, thus, represents the
abstraction.

The details of any class should represent abstractions.

# The interface segregation principle

* Clients should not depend on interfaces they
don't use.

In others words, a good base class never implements
any functionality that won't be used by the 
inheriting classes.

# The single responsability principle

* Classes, methods and functions should have 
only _one reason to change_

A reason to change should be interpreted as 
*functionality*. 

Therefore, for example, if a class caters to
_N functionalities_, it means that this 
class has _N reasons to change_. Ideally, this 
class should be splitted in N class,
each of one catering only to one reason to change.

# The substitution principle

* Derived classes must be able to completely 
substitute the base classes  
 