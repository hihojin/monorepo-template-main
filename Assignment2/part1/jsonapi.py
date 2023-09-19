import json

# references: lecture recording and https://mathspp.com/blog/custom-json-encoder-and-decoder

class BetterEncoder(json.JSONEncoder):
    '''
    encoding complex and range objects
    '''
    def default(self, obj):
        name = type(obj).__name__  # obj = complex(1, 2). Then, name = "complex"
        try:
            encoder = getattr(self, f"encode_{name}")  # look for method name encode_complex
        except AttributeError:
            super().default(obj) # if obj is native json object don't need special serialization
        else:
            encoded = encoder(obj) # pass complex(1,2) into encode_complex method
            encoded["__extended_json_type__"] = name # tag the encoding with the special key: __extended_json_type__
            return encoded

    def encode_complex(self, obj):
        return {"real": obj.real, "imag": obj.imag}

    def encode_range(self, obj):
        return {"start": obj.start, "stop": obj.stop, "step": obj.step}

class BetterDecoder(json.JSONDecoder):
    '''
    extneding json decoding for complex and range objects
    '''
    def __init__(self, **kwargs):
        kwargs["object_hook"] = self.object_hook
        super().__init__(**kwargs)

    def object_hook(self, obj):
        try:
            name = obj["__extended_json_type__"]
            decoder = getattr(self, f"decode_{name}")
        except (KeyError, AttributeError):
            return obj
        else:
            return decoder(obj)
    
    def decode_complex(self, obj):
        return complex(obj["real"], obj["imag"])

    def decode_range(self, obj):
        return range(obj["start"], obj["stop"], obj["step"])
    
def dumps(data, cls=BetterEncoder):
    return json.dumps(data, cls=cls)

def loads(data, cls=BetterDecoder):
    return json.loads(data, cls=cls)