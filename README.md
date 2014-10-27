# Mercury

Build with [Flask](http://flask.pocoo.org/).

## Environment
- Install *python* and *pip* `brew install python`
- Install *virtualenv* and *virtualenvwrapper*

        pip install virtualenv virtualenvwrapper
        export WORKON_HOME=~/Envs
        mkdir -p $WORKON_HOME
        source /usr/local/bin/virtualenvwrapper.sh
        mkvirtualenv mercury

- Add the following lines to the end of `$VIRTUAL_ENV/bin/postactivate`

        cd [PROJECT_PATH]
        export APP_SETTINGS="config.DevelopmentConfig"
        export DATABASE_URL="postgresql://[YOUR_DB_USERNAME]pivotal@localhost/mercury"
        
- Run `workon mercury`


## Database
- Create database and run migrations

        createdb mercury
        python manage.py db upgrade


## Development
- Install dependencies with `pip install -r requirements.txt`
- Create database with `python createdb.py`
- Run server on `localhost:5000` with `python runserver.py`