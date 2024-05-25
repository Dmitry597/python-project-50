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
