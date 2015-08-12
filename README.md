xjson
=====

*eXtended JavaScript Object Notation -- JSON with comments*

Description
-----------

`xjson` *(pronounced as 'ex-ja-son')* is a tiny module, which extends the
standard JSON python module with the ability to process non-standard JSON files,
which have either single- or milti-line comments in them.

It can process JSON files like this:

```json
{
    "hello": "world", // a comment right after the content
    // a comment between two lines of contents
    "// this is not a comment!": true,
    // "this is not a string!"
    "another": /* a comment inline */ 12,
    /* and a
    multiline
    comment
    before
    content */ "xxx": "/* this is not a comment either!", /* But this one is! */
    "Fortunately this is not a comment */": 34,
    "With this neat little trick /*
    */we have multiline, concatenated /*
    */key here": "with some value"
}
```

> ***NOTE:*** `xjson` only defines `load` and `loads` functions, everything else
> is the same as in the built-in `json` module, they are only here for easier
> and shorter imports.

Dependencies
------------

None.

Installation
------------

On Linux and Macintosh:

```
$ git clone https://github.com/petervaro/xjson.git
$ cd xjson
$ sudo python3 setup.py install
```

Usage
-----

Process `str` to `dict`:

```python
from xjson import loads

data = """
{
    // Some comment
    "key": "value"
}
"""

print(loads(data))
```

And the output is:

```
{'key': 'value'}
```

Process file to `dict`:

```python
from xjson import load

data = load('/path/to/data.josn')
```
