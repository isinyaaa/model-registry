.PHONY: clean
clean:
	rm -rf model-registry.yaml src/model_registry/{api,models,kiota-lock.json,model_registry_client.py} kiota_tmp dist

.PHONY: install
install:
	poetry install

.PHONY: test
test:
	poetry run pytest -s

.PHONY: lint-check
lint-check:
	poetry run black ./ --check
	poetry run ruff check

.PHONY: lint-apply
lint-apply:
	poetry run ruff check --fix --unsafe-fixes
	poetry run black ./

.PHONY: build
build: install
	poetry build

.PHONY: publish
publish: install
	poetry publish --build -u ${PYPI_USERNAME} -p ${PYPI_PASSWORD}

.PHONY: update
update:
	poetry lock
