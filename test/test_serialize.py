
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

    module.serializer = Serializer('tiddlywebplugins.lazy.serialization',
            environ)


def test_lazy():
    tiddlers = store.list_bag_tiddlers(store.get(Bag('test')))

    output = ''.join(serializer.list_tiddlers(tiddlers))

    assert 'I am uniquely999' not in output
    assert 'title="LazyTiddlers"' in output
    assert 'test:monkey' in output







