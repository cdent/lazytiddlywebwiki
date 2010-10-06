


def test_compile():
    try:
        import tiddlywebplugins.lazy
        assert True
    except ImportError, exc:
        assert False, exc
