# solscraper



### Dev Setup

Also check out CONTRIBUTING.rst

- Install Chromium: https://chromedriver.chromium.org/downloads (version 96)
- Unzip and copy the executable to ./binaries -> `mv ~/Downloads/chromedriver ./binaries`
- Add the executable to your PATH (add this to ~/.bash_profile) -> `export PATH=$PATH:/Users/zman/PycharmProjects/solana-projects/solscraper/binaries`
- Run the following commands:

    $ make dev-init
    $ source ~/.virtualenvs/solscraper/bin/activate
    $ python setup.py develop
    $ ~/.virtualenvs/solscraper/bin/python solscraper/cli.py arg1 arg2
- Add Chromium to your new virtualenv bin:
- `which python`
- `/Users/zman/.local/share/virtualenvs/solscraper--Jf6takQ/bin/python`
- `mv ./binaries/chromedriver /Users/zman/.local/share/virtualenvs/solscraper--Jf6takQ/bin/`

### Running the command line tool

    $ make install
    $ solscraper arg1 arg2 arg3

### Testing
Unit tests

    $ pytest

Tox (run pytest with different Python versions) + Flake8 (linting)

    $ tox


### Chromium Selenium Docker
https://github.com/joyzoursky/docker-python-chromedriver/blob/master/py-debian/3.9-selenium/Dockerfile
