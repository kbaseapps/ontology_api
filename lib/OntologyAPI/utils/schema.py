import yaml
import functools

_PATH='/kb/module/data/schema.yaml'

@functools.lru_cache(maxsize=1)
def load_schemas():
    schemas = {}
    with open(_PATH) as fd:
        schemas = yaml.safe_load(fd.read())
    return schemas
