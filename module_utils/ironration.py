#!/usr/bin/env python
"""
The Iron Ration.

A minimal set of functions to make python 2.x/3.x more pleasurable
without moving to full-blown third-party libraries.
"""
from functools import reduce, partial

# untested
def cons(elem, seq):
    if isinstance(seq, list):
        return [elem] + seq
    elif isinstance(seq, tuple):
        return (elem,) + seq
    raise ValueError("expect seq to be a tuple/list")

# untested
def append(elem, seq):
    if isinstance(seq, list):
        return seq + [elem]
    elif isinstance(seq, tuple):
        return seq + (elem,)

# untested
def iterp(obj):
    """True iff `obj` is iterable."""
    try:
        iter(obj)
        return True
    except:
        return False

def dict_merge(*dicts):
    """merge dictionaries in the order supplied."""
    def merge_two(dict1, dict2):
        # note: using in-place merging in this function
        dict1.update(dict2)
        return dict1
    return reduce(merge_two, dicts, {})

# untested
def dict_dissoc(d, iterable)
    """xxx"""
    d2 = d.copy()
    for k in iterable:
        d2.pop(k)
    return d2



class __Unset:
    """Used to mark an unset KW param."""
    pass
__unset = __Unset()

def unsetp(val):
    """True iff `val` is the magic 'unset' value."""
    return id(__unset) == id(val)

def get_in(obj, *path, default=__unset):
    """..."""
    if len(path) == 0:
        raise ValueError("path must be supplied")
    if len(path) == 1 and iterp(path[0]) and not isinstance(path[0], str):
        path = path[0]
    try:
        return reduce(lambda obj, key: obj[key], path, obj)
    except (KeyError) as e:
        if unsetp(default):
            raise e
        else:
            return default

def tostr(x, encoding='utf-8'):
    """string coercion."""
    if isinstance(x, bytes):
        return x.decode('utf-8')
    elif isinstance(x, str):
        return x
    return str(x)
