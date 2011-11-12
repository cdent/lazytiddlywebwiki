"""
Initialize the plugin by merging config.
"""

def init(config):
    """
    Update the standard config with tiddlywebplugins.lazy.config.
    """
    from tiddlyweb.util import merge_config
    from tiddlywebplugins.lazy.config import config as lconfig

    merge_config(config, lconfig)
