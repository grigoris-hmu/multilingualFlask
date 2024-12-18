# multilingualFlask
Multilingual Flask Boilerplate with smart routing optimised for search engines and including separate URL’s for each language.


## Tutorial
The tutorial which explains every part of the project can be found on medium:<br>
https://medium.com/@nicolas_84494/flask-create-a-multilingual-web-application-with-language-specific-urls-5d994344f5fd


# Flask-Babel mini How To

## Basics

### Create .pot file
pybabel extract -F babel.cfg -o messages.pot .

### Create .po file for each supported language
pybabel init -i messages.pot -d myApp/translations -l el<br/>
pybabel init -i messages.pot -d myApp/translations -l de<br/>
pybabel init -i messages.pot -d myApp/translations -l fr<br/>
pybabel init -i messages.pot -d myApp/translations -l ja<br/>

### Translate .po files

### Create binary .mo files
pybabel compile -d myApp/translations

## Flask-Babel Documentation
https://python-babel.github.io/flask-babel/


## Run mini How To

### Clone repository
clone https://github.com/grigoris-hmu/multilingualFlask.git<br/>
cd smart-plant-care-test/

### Initialize Python virtual enviroment
python3 -m virtualenv .venv<br/>
source .venv/bin/activate

### Install dependencies
pip install -r requirements.txt

### Run app locally (Running on http://127.0.0.1:5000)
python3 microblog.py


