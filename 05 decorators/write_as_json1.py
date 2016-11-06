import json
import functools

@functools.singledispatch
def write_as_json(file, data):
    json.dump(data, file)

@write_as_json.register(str)
@write_as_json.register(bytes)
def write_as_json_filename(file, data):
    with open(file, 'w') as fh:
	write_as_json(fh, data)

data = dict(a=1, b=2, c=3)
write_as_json('test1.json', data)
write_as_json(b'test2.json', 'w')
with open('test3.json', 'w') as fh:
    write_as_json(fh, data)