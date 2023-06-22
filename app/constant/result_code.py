from enum import Enum

class ResultCode(Enum):
    SUCCESS = '0000', 'Success'
    NAVER_ERROR = '1000', 'Naver response code is not 200'
    PARAM_ERROR = '2000', 'You missing required parameter'
    KNOWN_ERROR = '9000', 'Known error found'
    
    def __new__(cls, *args, **kwds):
        obj = object.__new__(cls)
        obj._value_ = args[0]
        return obj

    # ignore the first param since it's already set by __new__
    def __init__(self, _: str, description: str = None):
        self._description_ = description

    def __str__(self):
        return self.value

    # this makes sure that the description is read-only
    @property
    def description(self):
        return self._description_
