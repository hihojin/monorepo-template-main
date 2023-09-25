# Exercises

Update your answers to the following questions, make sure to commit this file and your improved code as well!


## Task 1 - oop.py

1. Is MObject an abstract or a concrete class? Explain why:
	concrete class. python module abc is not imported and there's no decorator as @abstractmethod

1. The 'Image' class has commented code for a `__del__` method. What does this commented-out method do?
	destructor. This method is called when an object is garbage collected.

1. What class does Texture inherit from?
	Image class

1. What methods and attributes does the Texture class inherit from 'Image'? 
	Subclass can inherit every public attributes and methods in Image(parent) class.

1. Do you think a texture should have a 'has-a' (composition) or 'is-a'(inheritance) relationship with 'Image'? If you think it is a 'has-a' relationship, refactor the code. As long as you defend your decision in the response below it could be either--but defend your position well!
	has-a relationship. 'An image has a texture' makes more sense.

1. I did not declare a constructor for Texture. Does Python automatically create constructors for us? 
	python automatically creates a default constructor.

## Task 2 - Singleton

1. Refactor the singleton.py file such that:
  - The first time the logger is constructed, it will print out:
  	-  `Logger created exactly once`
  - If the logger is already initialized, it will print:
  	-  `logger already created`
Note: You do not 'have' a constructor, but you construct the object in the *instance* member function where you will create an object.  
Hint: Look at Lecture 3 slides for an example of creating a Singleton in Python

1. Are singleton's in Python thread safe? Why or why not?

not thread-safe. If there are 2 threads, it might be possible the first thread is creating
the singleton instance but thread 2 might also does the same before the first instance was stored.

  
