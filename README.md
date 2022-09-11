# Digicala Requests
This App is for Scrapping in Digicala Website.

<br>

## How Can i Run this Program

at first you must download Chrome Driver from this [Link](https://chromedriver.chromium.org/downloads),
After the file is downloaded, extract it and place it next to the "manage.py" file.

<br>

1. create a virtualenv:
```
python -m venv venv
```
<br>

2. activate a virtualenv:
```
.\venv\Scripts\activate
```

<br>

3. install requirements:
```
pip install -r requirements.txt
```

<br>

4. make migrations & migrate:
```
python manage.py makemigrations
python manage.py migrate
```

<br>

5. create admin:
```
python manage.py createsuperuser
```

<br>

6. run the server:
```
python manage.py runserver 8000
```

## Design
1. At first, I wanted to use Scrappy, but since I had no experience working with it, I used Selenium.
2. Digicala website is single page application(SPA). So i can't use 'requests' package
3. create CategoryModel for ordering in products
4. i used bulk_create() method for saving time

## Future features
1. select category of product from client
2. show comments and save them
3. get a string from user and search that in Digicala and show or save results

1. Use Condition statements when encountering errors while finding elements on the page
2. Use from Celery. Because this process is very time consuming.This trick prevents the browser from loading for a long time.
3. Solid principal is not observed. must be improve it!
4. we can use multi threading or multi procceing for save the time
5. Storing product links in the cache. this job will prevent repeated requests in the process