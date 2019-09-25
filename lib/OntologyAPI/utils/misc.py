import re
import time
import jsonschema

from OntologyAPI.utils import config, schema
from OntologyAPI.utils.schema import load_schemas
from OntologyAPI.exceptions import InvalidParamsError, REError
from jsonschema.exceptions import ValidationError

_CONF=config.get_config()
_SCHEMAS=schema.load_schemas()

def validate_params(params, schema='default'):
    _params={}
    try:
        _params=params.copy()
        _params['ts'] = _params.get('ts', int(time.time() * 1000)) 
        _params['ns'] = _params.get('ns', 'default') 
        _schema = _SCHEMAS[schema]
        _schema['properties']['ns']['enum']=list(_CONF['ns'].keys())
        jsonschema.validate(instance=_params, schema=_schema)
    except ValidationError as err:
        raise InvalidParamsError('Parameter validation error: ' + err.message)
    return _params

