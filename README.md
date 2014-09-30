nbn-elections
=============

## Requirements

- `virtualenv` and `virtualenvwrapper`

## Getting started
Please note – this guide assumes you are using OS X. If you aren't, you hopefully know the equivalent commands to make these things happen. If you don't, find someone to help you!

First, clone this project.

```bash
git clone git@github.com:northbynorthwestern/nbn-elections.git
cd nbn-elections
```

Then, create the virtual environment for your project.

```bash
mkvirtualenv nbn-elections
add2virtualenv .
```

Add this to your `~/.virtualenvs/nbn-elections/bin/postactivate` file:
```bash
export DJANGO_SETTINGS_MODULE=elections.config.settings.development
```

And install the requirements:

```bash
pip install Django==1.7
pip install -r requirements.txt
```

Note: Django is not in the requirements because django-faker requires it to be installed before it can be installed.

Now create the database (this assumes you have postgres installed) and run Postgres:

```bash
createdb nbn_elections
pgup
```

```
export DJANGO_SETTINGS_MODULE=elections.config.settings.development
```

You should be able to run your first `migrate` now:

```bash
django-admin makemigrations
django-admin migrate
```

To get the political race models filled, run:

```bash
django-admin create_races
```

You will also need to install Grunt and other Node dependencies to compile the Sass (this assumes you already have `node` and `grunt-cli` installed).

```bash
npm install
grunt dev
```

Then, you should be able to run the server:

```bash
django-admin runserver
```


