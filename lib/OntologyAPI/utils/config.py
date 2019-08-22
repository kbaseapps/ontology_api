"""
Manage configuration data for the app.
"""
import os
import functools


@functools.lru_cache(maxsize=1)
def get_config():
    config = {
        're_url': 'https://ci.kbase.us/services/relation_engine_api',
        'default_name_space': 'GO',
        'name_space': {
            'GO': 'GO'
        }
    }
    return config


class ConfigError(Exception):
    """Error initializing configuration."""
    pass

