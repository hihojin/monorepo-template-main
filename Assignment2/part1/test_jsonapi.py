import jsonapi

json_data = jsonapi.dumps(complex(1, 2))
print(json_data)
decoded = jsonapi.loads(json_data)
print(decoded)

json_data = jsonapi.dumps(range(1, 10, 3))
print(json_data)
decoded = jsonapi.loads(json_data)
print(decoded)

json_data = jsonapi.dumps(range(1, 10))
print(json_data)
decoded = jsonapi.loads(json_data)
print(decoded)

json_data = jsonapi.dumps({73: False})
print(json_data)
decoded = jsonapi.loads(json_data)
print(decoded)

