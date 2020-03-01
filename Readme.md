Project structure(https://web.archive.org/web/20140409085244/http://www.deploydjango.com/django_project_structure)<br>
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

測試帳號
1. test2/abcd12345678

# 如何跑起來（以虛擬環境為例）
１.在根目錄建立虛擬環境
```
python3 -m venv venv 
source ven/bin/activate 
cd gift_u
```
2.安裝套件
```
pip install -r requirements.txt
```

3.跑local server
```
python manage.py runserver
```


