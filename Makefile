lint:
	poetry run flake8 brain_games

clean:
	rm -f dist/*

build: clean
	poetry build

install:
	poetry install

publish:
	poetry publish --dry-run

package-install: package-uninstall
	python3 -m pip install --user dist/*.whl

package-uninstall:
	python3 -m pip uninstall -y dist/*.whl

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc

brain-gcd:
	poetry run brain-gcd

brain-progression:
	poetry run brain-progression