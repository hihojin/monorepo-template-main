import jsonapi

'''
running pytest
'''

def test_encode_decode_complex():
    json_data = jsonapi.dumps(complex(1, 2))
    assert json_data == '{"real": 1.0, "imag": 2.0, "__extended_json_type__": "complex"}'
    decoded = jsonapi.loads(json_data)
    assert decoded == (1+2j)

def test_encode_decode_range():
    json_data = jsonapi.dumps(range(1, 10, 3))
    assert json_data == '{"start": 1, "stop": 10, "step": 3, "__extended_json_type__": "range"}'
    decoded = jsonapi.loads(json_data)
    assert decoded == range(1, 10, 3)

def test_encode_decode_json_friendly():
    json_data = jsonapi.dumps({73: False})
    assert json_data == '{"73": false}'
    decoded = jsonapi.loads(json_data)
    assert decoded == {'73': False}

