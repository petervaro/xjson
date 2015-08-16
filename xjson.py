## INFO ##
## INFO ##

# Import python modules
from json      import *
from functools import wraps
from re        import (compile,
                       finditer,
                       DOTALL,
                       VERBOSE,
                       MULTILINE)
from json      import (load  as __json_load,
                       loads as __json_loads)



#------------------------------------------------------------------------------#
__PATTERN = compile(r"""
    # Catch non multiline strings first
    (?P<string>"(.(?!$))+?")
    | # or
    # Catch single line or multiline comments
    (?P<comment>//.+?$|/\*.+?\*/)
""", flags=DOTALL|VERBOSE|MULTILINE)



#------------------------------------------------------------------------------#
@wraps(__json_loads)
def loads(dirty, *args, **kwargs):
    clean = []
    index = 0
    # Go through all matches in the string
    for match in finditer(__PATTERN, dirty):
        # If a comment pattern matched
        if match.group('comment'):
            # Add everything since index
            clean.append(dirty[index:match.start()])
            # Increase index
            index = match.end()
    # Add everything what's left since index
    clean.append(dirty[index:])
    # Let the built-in json-function process the cleaned string
    return __json_loads(''.join(clean), *args, **kwargs)



#------------------------------------------------------------------------------#
@wraps(__json_load)
def load(file_path, *args, **kwargs):
    # Open passed file path
    with open(file_path, mode='r') as file:
        # Return processed object
        return loads(file.read(), *args, **kwargs)



#------------------------------------------------------------------------------#
if __name__ == '__main__':
    # Import python modules
    from collections import OrderedDict

    # Load file
    data = load('sample.json', object_pairs_hook=OrderedDict)
    # Get max length of the keys
    pair = '{{:<{}}} : {{}}'.format(len(max(data.keys(), key=len)))
    # "Pretty print" the returned object
    for key, value in data.items():
        print(pair.format(key, value))
