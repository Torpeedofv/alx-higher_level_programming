#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        fun = fct(*args)
        return fun
    except Exception as error:
      
        print("Exception: {}".format(error), file=sys.stderr)
        return None
    else:
        return fun
