# Introduction
A statistical and genomic study of the SARS-CoV-2 virus.
The project contains implementation wide range of statisitical functions as well as different genomic analysis algorithms like Levenshtein distance algorithm, Needleman-Wunsch for global alignement...

## Group Members:
Groupe Number 13.\
Group members:
* Omar CHIDA
* Mathis DUMAS
* Chaima TOUNSI OMEZZINE
* Céline ZHANG

# How to run the code?
## Required packages:
Please install the following packages in order to be able to run the code
|Library |Usage|Installing|
|----|:-------|:-------|
|BioPython|Parsing FASTA files and testing| `python -m pip install -U biopython`|
|MatPlotLib|Used to plot graphs |`python -m pip install -U matplotlib`|
|NumPy|Dependcy and testing | `python -m pip install -U numpy`|
|SetupTools|To install src as a package | `python -m pip install -U setuptools`|
|PyTest|Test driver to run the  tests | `python -m pip install -U pytest`|

The `setuptools` package normally comes installed by default.
## Setup
Run `python setup.py develop` to install `src` as a package.\
This package will be used by `app` and the `tests` folder to apply some of the functions on genome sequences and amino acids.
## Execution
- Make sure you are in the root directory of the project (the one that contain the sub folders: 'src', 'tests', 'app', ...)
- To run the tests please type: `pytest` (these take a while to run)
- To run the python files in 'app' please type: `python ./app/file_to_run.py`

# Project Structure
|Folder |Content|
|----|:-------|
|src|Containts all the source files and functions used to analyse the genome. This acts like a library used by app.|
|tests|Test cases of the functions written in `src`.|
|app|Uses the functions and utilities defined in `src` to apply them to genomes and amino acids sequences|
|genome|Containts the genomic data downloded from the internet.|
|rapport|Contains the files used in the report. (Latex files, notices, etc)|

# Project Managment
We use trello as our project managment tool
The link to the board is: https://trello.com/b/N92bj53G/

# Our python coding style
## Why ?
It's mandatory to stick to this coding style, to have a clear and coherent code base.
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
