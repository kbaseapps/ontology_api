import re
import time
import jsonschema

from OntologyAPI.utils import config, schema, namespace
from OntologyAPI.exceptions import InvalidParamsError, REError
from jsonschema.exceptions import ValidationError

_CONF=config.get_config()
_SCHEMAS=schema.load_schemas()
_NAMESPACE=namespace.load_namespaces()

def validate_params(params, schema='default'):
    _params={}
    try:
        _params=params.copy()
        _params['ts'] = _params.get('ts', int(time.time() * 1000)) 
        _params['ns'] = _params.get('ns', _NAMESPACE['default']) 
        _ns = _NAMESPACE[_params['ns']]
        _schema = _SCHEMAS[schema]
        for x in ['@onto_terms', '@onto_edges']:
          if x in _ns and x in _schema['properties']:
            _params[x]=_ns[x]
        _schema['properties']['ns']['enum']=list(_NAMESPACE.keys())
        jsonschema.validate(instance=_params, schema=_schema)
    except ValidationError as err:
        raise InvalidParamsError('Parameter validation error: ' + err.message)
    except KeyError as err:
        raise InvalidParamsError('Parameter validation error: ' + _params['ns'] + " namespace doesn't exist")
    return _params

