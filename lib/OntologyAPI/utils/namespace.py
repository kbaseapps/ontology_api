import yaml
import functools

_PATH='/kb/module/data/namespace.yaml'

@functools.lru_cache(maxsize=1)
def load_namespaces():
    namespaces = {}
    with open(_PATH) as fd:
        namespaces = yaml.safe_load(fd.read())
    return namespaces
