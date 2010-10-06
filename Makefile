.PHONY: all tiddlywiki remotes clean test dist release pypi peermore makebundle uploadbundle bundle

all:
	@echo "No target"

clean:
	find . -name "*.pyc" |xargs rm || true
	rm -r dist || true
	rm -r build || true
	rm -r *egg-info || true
	rm *.bundle || true
	rm -r store tiddlyweb.log || true

test:
	py.test -x test

dist: test
	python setup.py sdist

release: clean remotes test pypi

pypi:
	python setup.py sdist upload
