install: # установить зависимости проекта
	poetry install

build: # позволяет создать "собранную" версию проекта
	poetry build

publish: # для отладки публикации
	poetry publish --dry-run

package-install: # для установки пакета из операционной системы
	python3 -m pip install dist/*.whl

package-reinstall: # для переустановки пакета из операционной системы
	pip install --force-reinstall dist/*.whl

installation:
	poetry install
	poetry build
	poetry publish --dry-run
	pip install --force-reinstall dist/*.whl

asciinema:
	asciinema rec

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml tests/

mytest:
	poetry run gendiff tests/fixtures/file1.json tests/fixtures/file2.json
	poetry run gendiff tests/fixtures/file_1.yml tests/fixtures/file_2.yml
	poetry run gendiff tests/fixtures/file1.json tests/fixtures/file_2.yml
	poetry run gendiff tests/fixtures/file_1.yml tests/fixtures/file2.json
	poetry run gendiff tests/fixtures/file3.json tests/fixtures/file4.json
	poetry run gendiff tests/fixtures/file_3.yml tests/fixtures/file_4.yml
	poetry run gendiff tests/fixtures/file3.json tests/fixtures/file_4.yml
	poetry run gendiff tests/fixtures/file_3.yml tests/fixtures/file4.json
	poetry run gendiff -f stylish tests/fixtures/file_3.yml tests/fixtures/file4.json
	poetry run gendiff -f plain tests/fixtures/file1.json tests/fixtures/file2.json
	poetry run gendiff -f plain tests/fixtures/file3.json tests/fixtures/file4.json
	poetry run gendiff -f plain tests/fixtures/file_1.yml tests/fixtures/file_2.yml
	poetry run gendiff -f plain tests/fixtures/file_3.yml tests/fixtures/file_4.yml
	poetry run gendiff -f plain tests/fixtures/file3.json tests/fixtures/file_4.yml
	poetry run gendiff -f json tests/fixtures/file1.json tests/fixtures/file2.json
	poetry run gendiff -f json tests/fixtures/file_3.yml tests/fixtures/file_4.yml


