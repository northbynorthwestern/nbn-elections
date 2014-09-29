nbn-elections
=============

## Requirements

- Django 1.7
- `virtualenvwrapper`

## Getting started

Please note – this guide assumes you are using OS X. If you aren't, you hopefully know the equivalent commands to make these things happen. If you don't, find someone to help you!

First, clone this project.

```bash
git clone git@github.com:northbynorthwestern/nbn-elections.git
```

Then, create the virtual environment for your project.

```bash
mkvirtualenv nbn-elections
```
And install the requirements:

```bash
pip install -r requirements.txt
```

Now create the database (this assumes you have postgres installed) and run Postgres:

```bash
createdb nbn_elections
pgup
```

You should be able to run your first `migrate` now:

```bash
python elections/manage.py makemigrations
python elections/manage.py migrate
```

To get the political race models filled, run:

```bash
python elections/manage.py create_races
```

You will also need to install Grunt and other Node dependencies to compile the Sass (this assumes you already have `node` and `grunt-cli` installed).

```bash
npm install
grunt dev
```

Then, you should be able to run the server:

```bash
python elections/manage.py runserver
```


