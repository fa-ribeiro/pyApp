# Setting up

## Virtual environment

### pipenv

Pipenv: Python Development Workflow for Humans

Pipenv is a tool that aims to bring the best of all packaging worlds (bundler, composer, npm, cargo, yarn, etc.) to the Python world. It automatically creates and manages a virtualenv for your projects, as well as adds/removes packages from your `Pipfile` as you install/uninstall packages. It also generates the ever-important `Pipfile.lock`, which is used to produce deterministic builds.

Installation:

```shell
pip install pipenv
```

Usage:

To initialize a Python 3 virtual environment, run:

```shell
mkdir myProject && cd MyProject
pipenv --three
```

To activate a virtualenv, run:

```shell
pipenv shell
```

The main commands are `install`, `uninstall`, and `lock`, which generates a `Pipfile.lock`.

Other commands are:

- `shell` will spawn a shell with the virtualenv activated.
- `run` will run a given command from the virtualenv, with any arguments forwarded (e.g. $ pipenv run python).
- `check` asserts that PEP 508 requirements are being met by the current environment.
- `graph` will print a pretty graph of all your installed dependencies.

## Tools

### Formatters

#### black

Black is the uncompromising Python code formatter. By using it, you agree to cede control over minutiae of hand-formatting. In return, Black gives you speed, determinism, and freedom from pycodestyle nagging about formatting. You will save time and mental energy for more important matters.

Installation:

```shell
pipenv install --dev black
```

Usage:

```shell
black --line-length=119 pyapp
```

### Linters

#### flake8

Flake8 is a wrapper around these tools: PyFlakes, pycodestyle and Ned Batchelder’s McCabe script. Flake8 runs all the tools by launching the single flake8 command. It displays the warnings in a per-file, merged output.

Installation:

```shell
pipenv install --dev flake8
```

Usage:

```shell
flake8 . --ignore=E501 --count --show-source --statistics 
```

#### bandit

Bandit is a tool designed to find common security issues in Python code.

Installation:

```shell
pipenv install --dev bandit
```

Usage:

```shell
bandit -r pyapp
```

#### mypy

Add type annotations to your Python programs, and use mypy to type check them. Mypy is essentially a Python linter on steroids, and it can catch many programming errors by analyzing your program, without actually having to run it. Mypy has a powerful type system with features such as type inference, gradual typing, generics and union types.

Installation:

```shell
pipenv install --dev mypy
```

Usage:

```shell
mypy pyapp
```

## Testing

### pytest

The pytest framework makes it easy to write small tests, yet scales to support complex functional testing for applications and libraries.

Installation:

```shell
pipenv install --dev pytest pytest-cov
```

Usage:

```shell
pytest --cov-report term-missing --cov pyapp
```

## Documentation

## pdoc3

Auto-generate API documentation for Python projects.

Pdoc3 generates documentation simply from your project's already-existing public modules' and objects' docstrings.

Installation:

```shell
pip install pdoc3
```

Usage:

Build HTML documentation by running:

```shell
pdoc3 --output-dir ./docs --force --html pyapp
```

The docs will appear in ./docs directory

## References

- [Python Coding Guidelines 12/14/07](https://web.archive.org/web/20111010053227/http://jaynes.colorado.edu/PythonGuidelines.html#module_formatting)
