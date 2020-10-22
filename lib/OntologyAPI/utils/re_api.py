"""
Relation engine API client.
"""
import json
import requests
from OntologyAPI.utils import config, namespace
from OntologyAPI.exceptions import REError

_CONF = config.get_config()
_NAMESPACE=namespace.load_namespaces()

def query(name, params, token=None):
    """Run a stored query from the RE API."""
    _params=params.copy();
    ns=_params['ns']
    del _params['ns']
    url=_CONF['re_url'] + '/api/v1/query_results'
    query=_NAMESPACE[ns]['prefix'] + '_' + name
    resp = requests.post(
        url,
        params={'stored_query': query},
        data=json.dumps(_params),
        headers={'Authorization': token}
    )
    if not resp.ok:
        error=json.loads(resp.text)
        #print("RE Error:", json.dumps(error['error']))
        #raise REError(resp)
        return {'stats': {}, 'results': [], 'error': error['error']}
    return resp.json()

