# python-reporter-testsuite
An example testsuite for all supported Applause Python SDK test runners

## Supported Test Runners
- pytest (https://github.com/ApplauseOSS/pytest-applause-reporter)

## Execution

### Prerequisites

```bash
pip install poetry
poetry install        # installs python dependencies into poetry
poetry install --dev  # installs python dev-dependencies into poetry
```

Optionally, run this command to stick python virtualenv to project directory.

poetry config virtualenvs.in-project true

### Building

We use tox to automate our build pipeline. Running the default tox configuration will install dependencies, format and lint the project, run the unit test and run the build. This will verify the project builds correctly for python 3.8, 3.9, 3.10, and 3.11. 

```bash
poetry run tox
```

### Linting

The plugin can be linted through tox `tox run -e lint`

### Running Unit Tests

The unit tests can be executed through tox `tox run -e test`

### Intellij setup

https://www.jetbrains.com/help/idea/poetry.html

### Helpful commands

```bash
# list details of the poetry environment
poetry env info 

# To activate this project's virtualenv, run the following:
poetry shell

# To exit the virtualenv shell:
exit

# To install packages into this virtualenv:
poetry add YOUR_PACKAGE
```