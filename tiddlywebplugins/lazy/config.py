"""
The default configuration information for tiddlywebplugins.lazy.

This gets merged when the plugin is initialized.
"""

config = {
        #instance_tiddlers':
        'extension_types': {
            'lwiki': 'text/x-ltiddlywiki',
            },
        'serializers': {
            'text/x-ltiddlywiki': ['tiddlywebplugins.lazy.serialization',
                'text/html; charset=UTF-8'],
            },
        }
