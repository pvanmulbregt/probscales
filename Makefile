test:
	py.test -v tests

sdist :
	python setup.py sdist

wheel :
	python setup.py bdist_wheel

init:
	pip install -r requirements.txt

gen : probscales/scipyscales.py

probscales/scipyscales.py : tools/gen_probscales.py

probscales/scipyscales.py :
	python tools/gen_probscales.py "--out=probscales/scipyscales.py"

.PHONY: init test wheel sdist gen
