# import builtins

def find_mapping(key):
    mappings = locals(), globals()
    for mapping in mappings:
        if key in mapping:
            return mapping[key]
    return "no mapping..."


print find_mapping("__name__")


# combo = collections.ChainMap(locals())
