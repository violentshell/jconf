# Jconf
A simple module to write, load and update JSON config files for your python3 projects.

## Installation
jconf is packaged and distrubted with pip:

    pip install jconf

## Usage
Usage is designed to be simple and intuitive:

Create a config file:

    >>>> import jconf
    >>>> conf = jconf.Jconf('conf.json')
    >>>> conf.somevar1 = True
    >>>> conf.somevar2 = 3.14
    >>>> conf.write()
    
Read and access variables from a config file:
    
    >>>> conf = jconf.Jconf('conf.json')
    >>>> conf.read()
    >>>> conf.is_empty()
    False
    >>>> conf.keys()
    ['somevar1', 'somevar2']
    >>>> conf.somevar1
    True
    >>>> conf.somevar2
    3.14
    
Change a config files variables and save them:

    >>>> conf.somevar1 = False
    >>>> conf.somevar2 = 5.91
    >>>> conf.write()
    
Load, change and save to a new file:

    >>>> conf = jconf.Jconf('conf.json')
    >>>> conf.read()
    >>>> conf.somevar1 = True
    >>>> conf.somevar2 = 3.14
    >>>> conf.write('newconf.json')

## Gotchas
If you use a number as the json key, jconf will return it with a preceding 'n' so that it can call the setattr method
