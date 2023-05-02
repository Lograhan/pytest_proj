

def get_val(collection, key, default='git'):
    data = collection
    if data.get(key) is None:
        return default

    return data.get(key)
