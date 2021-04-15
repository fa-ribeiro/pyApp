# PyApp

[![image](https://img.shields.io/travis/com/fa-ribeiro/pyApp?branch=main)](https://github.com/fa-ribeiro/pyApp)
[![image](https://img.shields.io/github/license/fa-ribeiro/pyApp)](https://github.com/fa-ribeiro/pyApp)
[![image](https://img.shields.io/github/languages/code-size/fa-ribeiro/pyApp)](https://github.com/fa-ribeiro/pyApp)
[![image](https://img.shields.io/github/pipenv/locked/python-version/fa-ribeiro/pyApp)](https://github.com/fa-ribeiro/pyApp)

[![image](https://img.shields.io/github/pipenv/locked/dependency-version/fa-ribeiro/pyApp/dev/flake8)](https://github.com/fa-ribeiro/pyApp)
[![image](https://img.shields.io/github/pipenv/locked/dependency-version/fa-ribeiro/pyApp/dev/black)](https://github.com/fa-ribeiro/pyApp)
[![image](https://img.shields.io/github/pipenv/locked/dependency-version/fa-ribeiro/pyApp/dev/pytest)](https://github.com/fa-ribeiro/pyApp)
[![image](https://img.shields.io/github/pipenv/locked/dependency-version/fa-ribeiro/pyApp/dev/pytest-cov)](https://github.com/fa-ribeiro/pyApp)
[![image](https://img.shields.io/github/pipenv/locked/dependency-version/fa-ribeiro/pyApp/dev/bandit)](https://github.com/fa-ribeiro/pyApp)
[![image](https://img.shields.io/github/pipenv/locked/dependency-version/fa-ribeiro/pyApp/dev/mypy)](https://github.com/fa-ribeiro/pyApp)

PyApp is a python application boilerplate capable of doing wonderful things.

This package can make wonderful things happen to you too. Dare yourself to
create amazing things by extending this package with you imagination.

Out of the box, it makes use of some great tools:

- **pipenv** to bring the best of all packaging worlds;
- **black**, the uncompromising Python code formatter;
- **flake8**, your to check the style and quality of your python code;
- **bandit**, a tool designed to find common security issues in Python code;
- **mypy** for type checking your Python code type annotations;
- **pytest** to run functional testing for applications and libraries;
- **pdoc3**, capable of auto-generate API documentation for Python projects.

## Installation

```shell
pip install pyapp
```

## Usage

The preferred way of use PyApp is as shown bellow.

```python
>>> from pyapp import PyApp
>>> app = PyApp()
>>> app.run()
"Doing something wonderful... done!"
```

Wonderful, isn’t it? Now it's your turn.

## Development setup

Clone the repository.

```shell
git clone https://github.com/fa-ribeiro/pyapp
```

Setup the virtual environment.

```shell
pipenv shell
~/pyapp $ pipenv install --dev
```

Install the required development packages:

```shell
pipenv install --dev
```

## Release History

- 0.0.1-dev
  - work in progress

## Meta

Fernando Ribeiro - [fribeiro@fribeiro.org](mailto:fribeiro@fribeiro.org)

Distributed under the MIT license. See `LICENSE` for more information.

## Contributing

1. Fork it (https://github.com/fa-ribeiro/pyapp/fork)
2. Create your feature branch (git checkout -b feature/fooBar)
3. Commit your changes (git commit -am 'Add some fooBar')
4. Push to the branch (git push origin feature/fooBar)
5. Create a new Pull Request
