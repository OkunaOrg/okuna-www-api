<img alt="Okuna logo" src="https://i.snag.gy/FAgp8K.jpg" width="200">

[![CircleCI](https://circleci.com/gh/OkunaOrg/okuna-www-api.svg?style=svg)](https://circleci.com/gh/OkunaOrg/okuna-www-api) [![Maintainability](https://api.codeclimate.com/v1/badges/fea3aa6354f1ea11fb21/maintainability)](https://codeclimate.com/github/OkunaOrg/okuna-www-api/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/fea3aa6354f1ea11fb21/test_coverage)](https://codeclimate.com/github/OkunaOrg/okuna-www-api/test_coverage) [![gitmoji badge](https://img.shields.io/badge/gitmoji-%20😜%20😍-FFDD67.svg?style=flat-square)](https://github.com/carloscuesta/gitmoji)

The code for [api.open-book.org](https://api.open-book.org).

## Table of contents

- [Requirements](#requirements)
- [Project overview](#project-overview)
- [Contributing](#contributing)
    + [Code of Conduct](#code-of-conduct)
    + [License](#license)
    + [Other issues](#other-issues)
    + [Git commit message conventions](#git-commit-message-conventions)
- [Getting started](#getting-started)

## Requirements

* [Pipenv](https://github.com/pypa/pipenv)

## Project overview

The project is a [Django](https://www.djangoproject.com/start/) application. 

## Contributing

There are many different ways to contribute to the website development, just find the one that best fits with your skills and open an issue/pull request in the repository.

Examples of contributions we love include:

- **Code patches**
- **Bug reports**
- **Patch reviews**
- **Translations**
- **UI enhancements**

#### Code of Conduct

Please read and follow our [Code of Conduct](https://github.com/OkunaOrg/okuna-www-api/blob/master/CODE_OF_CONDUCT.md).

#### License

Every contribution accepted is licensed under [AGPL v3.0](http://www.gnu.org/licenses/agpl-3.0.html) or any later version. 
You must be careful to not include any code that can not be licensed under this license.

Please read carefully [our license](https://github.com/OkunaOrg/okuna-www-api/blob/master/LICENSE.txt) and ask us if you have any questions.

#### Git commit message conventions

Help us keep the repository history consistent 🙏!

We use [gitmoji](https://gitmoji.carloscuesta.me/) as our git message convention.

If you're using git in your command line, you can download the handy tool [gitmoji-cli](https://github.com/carloscuesta/gitmoji-cli).

## Getting started

Clone the repository

```sh
git clone git@github.com:OkunaOrg/okuna-www-api.git
```

Create and configure your .env file

```bash
cp sample.env .env
nano .env
```

Install the dependencies
```bash
$ pipenv install
```

Activate the pipenv environment
```bash
pipenv shell
```

Serve with hot reload at http://127.0.0.1:8000
```bash
$ python manage.py runserver
```

<br>

#### Happy coding 🎉!


