
from tiddlyweb.config import config
from tiddlywebwiki import init as twinit

from tiddlywebplugins.utils import get_store
from tiddlyweb.model.bag import Bag
from tiddlyweb.model.tiddler import Tiddler

from tiddlyweb.serializer import Serializer


def setup_module(module):
    twinit(config)
    store = get_store(config)
    bag = Bag('test')
    store.put(bag)
    environ = {'tiddlyweb.config': config}

    tiddler = Tiddler('monkey', 'test')
    tiddler.text = 'I am uniquely999'
    store.put(tiddler)

    module.store = store

    module.lserializer = Serializer('tiddlywebplugins.lazy.serialization',
            environ)
    module.fserializer = Serializer('tiddlywebwiki.serialization',
            environ)


def test_lazy():
    tiddlers = (store.get(tiddler) for tiddler in store.list_bag_tiddlers(store.get(Bag('test'))))
    output = ''.join(lserializer.list_tiddlers(tiddlers))
    assert 'I am uniquely999' not in output

    tiddlers = (store.get(tiddler) for tiddler in store.list_bag_tiddlers(store.get(Bag('test'))))
    output = ''.join(fserializer.list_tiddlers(tiddlers))
    assert 'I am uniquely999' in output, output
