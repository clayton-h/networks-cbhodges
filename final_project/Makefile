TEST = pytest 
TEST_ARGS = --verbose --color=yes
TYPE_CHECK = mypy --strict --allow-untyped-decorators --ignore-missing-imports
STYLE_CHECK = flake8
STYLE_FIX = autopep8 --in-place --recursive --aggressive --aggressive
COVERAGE_CHECK = pytest --cov=. --cov-report=html -v --cov-report=term
GENERATE_UML = pyreverse -o png --colorized .
GENERATE_HTML = pdoc --html --output-dir docs .

.PHONY: all
all: style-check type-check run-test clean
	@echo -e "\nAll checks passed\n"

.PHONY: generate-html
generate-html:
	$(GENERATE_HTML)
.PHONY: generate-uml
generate-uml:
	$(GENERATE_UML)

.PHONY: coverage-test
coverage-test:
	$(COVERAGE_CHECK)

.PHONY: type-check
type-check:
	$(TYPE_CHECK) .

.PHONY: style-check
style-check:
	$(STYLE_CHECK) .

# discover and run all tests
.PHONY: run-test
run-test:
	$(TEST) $(TEST_ARGS) .

.PHONY: clean
clean:
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf .hypothesis


.PHONY: push
push: run-test clean
	

.PHONY: fix-style
fix-style:
	$(STYLE_FIX) .
