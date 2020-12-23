# How to run the code?
Run `python setup.py develop` to install src as a package
This package will be used by `app` folder to apply some of the functions on genome sequences and amino acids
# Project Managment
We use trello as our project managment tool
The link to the board is: https://trello.com/b/N92bj53G/
# Our python coding style
## Introduction:
It's mandatory to accept these coding style, to have a clear and coherent code base.
## Comments
Try to keep inline comments short in length (max 72 character)
For example:
```python
# This is recommended
a = 2   # The first term 'a' in quadratic equation

# This is not
a = 20 # When you write Python code, you have to name a lot of things: variables, functions, classes, packages, and so on. Choosing sensible names will save you time and energy later. You’ll be able to figure out, from the name, what a certain variable, function, or class represents.
```

## Naming Styles
|Type | Naming Convention|Example|
|----:|:-------:|:-------|
|Function|Lowercase word or words, seperated by underscore.|function, my_function|
|Variable|Lowercase single letter, word, or words, seperated by underscore.|x, var, my_variable|
|Constant|Uppercase word or words, seperated by underscore|CONSTANT, MY_CONSTANT, MY_LONG_CONSTANT|
|Module|User a short, lowercasen word or words seperated by underscores|module.py, my_module.py|

## Condtions, loops
Before and after loops make sure you return to line. 
This rule have exceptions:
* Conditions or loops that are written at the beginning of a function
* Conditions/Loops that are written right after another condition/loop
* Conditions/Loops that are written right after another condition/loop

Example:
```python
#####################################################
# Example of :
#####################################################

#####################################################
# Example of exceptions of the rule mentioned above:
#####################################################
def test(x):
    a = 5
    
    # the exception lies here
    for i in range(0, x)
        for j in range(0, a)
            print(i)

def test(x):
    for i in range(0, x)
        print(i)
```
