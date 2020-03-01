# GiftU

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

測試帳號 Test account
accout:test2
password:abcd12345678

## Setup（use virtual environment as an example）
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

