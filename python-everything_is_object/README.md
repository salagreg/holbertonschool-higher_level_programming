# Blog article:


## Introduction :

This blog article presents, in the form of simple summaries, the essential concepts for understanding how Python manages its objects: their type, their identity, their behaviour when modified, and how they are passed to functions.


## Identifier and type :

Every value in Python is an object: it has a type (number, text, list, etc..) and an identifier, its address in memory.
Two objects can have the same value but be different in memory.


## Mutable objects :

These are objects that can be modified after they are created (lists, dictionaries).
If several variables point to the same mutable object, any modification will be visible everywhere.


## Immutable objects : 

These are objects that cannot be modified (numbers, text, tuples).
Any modification actually creates a new object, without changing the original.


## Importance and differences in how Python treats mutable and immutable objects :

Python optimises memory for immutable objects (reuse of identical objects).
Mutable objects can be modified in situ, which can cause indirect effects if several variables point to them.


## Passing arguments to functions and implications for mutable and immutable objects :

When passing an object to a function:
If the object is mutable, the function can modify it directly (effect on the original variable).
If the object is immutable, the function cannot modify the original: any modification creates a new value, with no impact on the outside world.
