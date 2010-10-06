

def init(config):
    from tiddlyweb.util import merge_config
    from tiddlywebplugins.lazy.config import config as lconfig

    merge_config(config, lconfig)

