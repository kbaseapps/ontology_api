"""
Manage configuration data for the app.
"""
import os
import functools

@functools.lru_cache(maxsize=1)
def get_config():
    config = {
        're_url': os.environ.get('KBASE_ENDPOINT', 'https://ci.kbase.us/services').strip('/') + '/relation_engine_api',
        'default_ns': 'go_ontology',
        'ns': {
            'go_ontology': 'GO'
        }
    }
    return config


class ConfigError(Exception):
    """Error initializing configuration."""
    pass

