# DemoTZ

```sh
$ https://github.com/Dimskay1988/DemoTZ.git
```

```sh
$ cd/DemoTZ
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python3.9.13 -m venv .venv
$ source .venv/bin/activate
```


Note the `(.venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `venv`.
Once `pip` has finished downloading the dependencies:

```sh
python -m pip install -r requirements. txt
```

Create migrations:


```sh
python manage.py migrate
```

Create .env file in CryptoAnalytics root folder:

```sh
touch .env
```

```sh
SECRET_KEY = config('SECRET_KEY')
```

```sh
DEBUG = config('DEBUG')
```



Your secret key, token and debug should be in .env file like this:

```sh
DJANGO_SECRET=asddsad231jsfjp32ojrjpfjsdoivzoidvhoxicj 
```

```sh
DEBUG=True/False
```
Start the server with the command:
```sh
(.venv)$ python manage.py runserver
```

And navigate to `http://127.0.0.1:8000/`

List of possible urls may be seen in urls.py in Crypto-analytics.
Have fun! :)
