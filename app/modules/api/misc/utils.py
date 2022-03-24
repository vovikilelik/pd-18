def omit(dictionary, *keys):
    return {i: dictionary[i] for i in dictionary if i not in keys}


def resolve(func, error=500):
    try:
        message, code = func()

        if not message:
            return 'Not Found', 404

        return message, code
    except Exception as e:
        return str(e), error
