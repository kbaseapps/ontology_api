"""
Manage configuration data for the app.
"""
import os
import functools


@functools.lru_cache(maxsize=1)
def get_config():
    config = {
        're_url': 'https://ci.kbase.us/services/relation_engine_api',
        'default_name_space': 'go_ontology',
        'ns': {
            'go_ontology': 'GO'
        }
    }
    return config


class ConfigError(Exception):
    """Error initializing configuration."""
    pass

