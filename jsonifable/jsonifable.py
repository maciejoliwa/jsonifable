import typing as tp
import json

from attr import has


T = tp.TypeVar('T')

_CONVERTABLE_TYPES = [dict, str, int, float, bool]

def Jsonifable(cls: T) -> T:
    """
    ## Jsonifable
    Adds a to_json method to your class, which after being called shall
    convert your class' properties and values into a JSON formatted string.

    If the decorated class contains another class, it will convert those aswell.

    ### Params:
    * cls -> class that you wish to decorate

    ### Returns:
    Decorated class
    """
    
    orign_init = cls.__init__

    def __init__(self, *args, **kwargs):
        orign_init(self, *args, **kwargs)

        def to_json(self) -> str:
            obj = {}

            for var in vars(self):
                attr = getattr(self, var)

                if hasattr(attr, 'to_json'):
                    obj[var] = json.loads(attr.to_json())

                # If an attr is iterable, go through
                # Every iterable is converted to list
                elif type(attr) in [list, tuple, set]:
                    obj[var] = list(attr)

                    for index, element in enumerate(attr):
                        if hasattr(element, 'to_json'):
                            obj[var][index] = json.loads(element.to_json())
                        elif type(element) in _CONVERTABLE_TYPES:
                            obj[var][index] = element
                        else:
                            obj[var][index] = json.loads(to_json(element))

                elif type(attr) in _CONVERTABLE_TYPES:
                    obj[var] = attr
                else:
                    obj[var] = json.loads(to_json(attr))

            return json.dumps(obj)

        cls.to_json = to_json

    cls.__init__ = __init__
    return cls