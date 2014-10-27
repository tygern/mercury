# Mercury

Build with [Flask](http://flask.pocoo.org/).

## Setup
- Install virtualenv and virtualenvwrapper

        pip install virtualenv virtualenvwrapper
        export WORKON_HOME=~/Envs
        mkdir -p $WORKON_HOME
        source /usr/local/bin/virtualenvwrapper.sh
        mkvirtualenv mercury

- Add the following two lines to the end of `$VIRTUAL_ENV/bin/postactivate`

        cd [PROJECT_PATH]
        export APP_SETTINGS="config.DevelopmentConfig"
        
- Run `workon mercury`


## Development
- Install dependencies with `pip install -r requirements.txt`
- Create database with `python createdb.py`
- Run server on `localhost:5000` with `python runserver.py`