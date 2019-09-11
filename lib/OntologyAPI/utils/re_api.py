"""
Relation engine API client.
"""
import json
import requests
from OntologyAPI.utils.config import get_config
from OntologyAPI.exceptions import REError

_CONF = get_config()

def query(name, params, token=None):
    """Run a stored query from the RE API."""
    name_space=params['name_space']
    del params['name_space']
    url=_CONF['re_url'] + '/api/v1/query_results'
    query=_CONF['name_space'][name_space] + '_' + name
    resp = requests.post(
        url,
        params={'stored_query': query},
        data=json.dumps(params),
        headers={'Authorization': token}
    )
    if not resp.ok:
        raise REError(resp)
    return resp.json()

