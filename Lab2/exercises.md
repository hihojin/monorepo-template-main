# Exercises (Modify this file)

Answer and complete the following exercises.

## Python Standard Library

1. How you name functions and member functions matter. Take a look at the [dictionary](https://docs.python.org/3/library/stdtypes.html#typesmapping) 
and [list](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range) member functions in the SL. 
Do the names of the member functions correlate to what they do? That is, are they good 'verbs' where the name of the function describes the action the code is doing? A good example would be a function called 'pop' which only removes one element. A bad example would be a function called 'pop' where one element is removed **and** that value is returned. A better name would be 'popAndGet' or 'popAndReturn', which captures the two events happening.

*Edit your responses here*
I think python member function/function names are clearly defined. For example, sort(), len() are well defined. Pop() it pops and returns an item so I agree it could have been named as pop_and_get().

2. How does a dictionary differ from a list? (i.e. What is the underlying data structure of each container.)

*Edit your response here*
dictionary - mapping type; maps hashable value to arbitrary objects.; stored as key-value pairs
list - mutable sequences. stores collections of items

3. Does a list allow for random access? Meaning can I access any element(e.g. myList[7])?

*Edit your response here*
yes, random acess is allowed with index number.

4. Observe that all the container data structures (i.e. list, set, dictionary, etc.) can work with any data type (integers, floats, custom data types, etc.). 
What do you think are the pros/cons of a library that can work with any data type?

*Edit your response here*
pros: flexible to store any data types
cons: Because we are not specifying a type of data structure(myList) we don't get to see the list of supported functions of i.e. string class.
If we specified a list type as string, list can only accept string types so when we write code in IDE as 'myList.' IDE shows all possible functions we can use for string class, including toString() method, for example, in Java.

## requests

1. Take a look at the requests API documentation here: https://requests.readthedocs.io/en/latest/  
Comment if the functions are well named in the Requests module (Follow the previous link to the documentation to see if you can find the Requests module (hint: look for API Reference)).

*Edit your responses here*
I think function names in the Request module makes sense and easy to understand if we have previous RESTapi experience.
But because all 7 methods in the Request module returns Response object, I believe function name could have been named as request_and_get_response(), etc.

2. Take a look at the [Requests](https://requests.readthedocs.io/en/latest/api/#lower-level-classes) class. APIs that have more than say 5 arguments in a function can be confusing or error prone to use. This is a heuristic of course, but do you see any member functions that include lots of arguments?

*Edit your responses here*
requests.Request(method=None, url=None, headers=None, files=None, data=None, params=None, auth=None, cookies=None, hooks=None, json=None)

3. Take another look at the Requests class. Note that many of the methods includes `**kwargs` as an argument. What is `**kwargs`? Why might it be good for a method to have a `**kwargs` argument? Why might it be bad?  

*Edit your responses here*
**kwargs (keyword arguments) - we can pass a variable number of keyword arguments. we can think of **kwargs as dictionary.
for example,

def foo(**kwargs):
    for k, v in kwargs.items():
        print(k)
        print(v)
foo(fruit1='banana', fruit2='apple', 'fruit3'='pineapple')

-> this function will print out each key and value as fruit1, banana, ...


4. Take a look at the [Session class.] (https://requests.readthedocs.io/en/latest/api/#request-sessions) Not only can you read the API's for that class, you can also view the source code by clicking the 'source' text. 
Notice how some methods have arguments that are set to `None` while other arguments are not set to anything. Why is that? Can arguments be set to anything besides `None`? Why might it be good to set an argument by some predetermined value?

*Edit your responses here*
Argument with default value as None -> python treats that argument as optional so if the second arugment has default value of None, and
we didn't pass the second argument python doesn't raise error. We can make default value besides None. For example, if we'd wanted to set it as 1, it is possible.

post(url, data=None, json=None, **kwargs)