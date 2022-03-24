def get_key(name_or_type):
    if hasattr(name_or_type, '__name__'):
        return name_or_type.__name__
    else:
        return name_or_type.__str__


def is_callable(value):
    return hasattr(value, '__call__')
