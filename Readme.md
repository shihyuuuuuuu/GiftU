# GiftU
A website that provides service for connecting with your old friends! A registered user can fill out surveys with three options and warm messages, which will later transform to an email and send to your friends; your friends can also select an option and send it back to you.

## Project structure
（參考：https://web.archive.org/web/20140409085244/http://www.deploydjango.com/django_project_structure)<br>
```
├── gift_u
│   ├── apps
│   │   ├── survey
        │   ├── static/survey
        │   ├── templates/survey
            │   ├── questionnaire.html
            │   ├── questionnaire_mail.html
            |   └── survey.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── templates
│   ├── base.html
│   ├── dashboard.html
│   ├── homepage.html
│   └── profile.html
└── requirements.txt
```


## Setup（take virtual environment as an example）
### １. Setup virtual environment
```
python3 -m venv venv 
source ven/bin/activate 
cd gift_u
```
### 2. Install dependency
```
pip install -r requirements.txt
```

### 3.Run local server
```
python manage.py runserver
```




## Login 

Test account:test2 <br>
password:abcd12345678
