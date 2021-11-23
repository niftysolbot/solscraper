# solscraper


### Dev Setup

Also check out CONTRIBUTING.rst

    $ make dev-init
    $ source ~/.virtualenvs/solscraper/bin/activate
    $ python setup.py develop
    $ ~/.virtualenvs/solscraper/bin/python solscraper/cli.py arg1 arg2

### Running the command line tool

    $ make install
    $ solscraper arg1 arg2 arg3

### Testing
Unit tests

    $ pytest

Tox (run pytest with different Python versions) + Flake8 (linting)

    $ tox