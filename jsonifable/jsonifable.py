import typing as tp
import json


_T = tp.TypeVar('_T')
_ITERABLES = [list, tuple, set]
_BASIC_TYPES = [int, str, float, bool, None]


def _to_json(element: _T) -> tp.Dict[str, _T]:
    if type(element) in _BASIC_TYPES:
        return element
    
    elif type(element) == dict:
        return {key: _to_json(value) for (key, value) in element.items()}

    elif type(element) in _ITERABLES:
        return [_to_json(el) for el in element]

    else:
        obj = {}
        for var in vars(element):
            attr = getattr(element, var)
            obj[var] = _to_json(attr)
        
        return obj
    

def Jsonifable(cls: _T) -> _T:
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
                obj[var] = _to_json(attr)

            return json.dumps(obj)

        cls.to_json = to_json

    cls.__init__ = __init__
    return cls