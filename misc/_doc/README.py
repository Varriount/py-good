import good
from exdoc import doc, getmembers

import json

doccls = lambda cls, *allowed_keys: {
    'cls': doc(cls),
    'attrs': {name: doc(m) for name, m in getmembers(cls, None, lambda key, value: key in allowed_keys or not key.startswith('_'))}
}

data = {
    'good': doc(good),
    'Schema': doccls(good.Schema, None, '__call__'),
}


class MyJsonEncoder(json.JSONEncoder):
    def default(self, o):
        # Classes
        if isinstance(o, type):
            return o.__name__
        return super(MyJsonEncoder, self).default(o)

print json.dumps(data, indent=2, cls=MyJsonEncoder)
