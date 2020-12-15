## How To run on localhost
1. clone project to local
2. Create Database
3. Install packages
    ```shell
    $ pip install -r requirements.txt
    ```
4. Change config DATABASE in settings.py
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'internshop',
            'PROT': 5432,
            'HOST': 'db',
            'USER': 'postgres',
            'PASSWORD': 'postgres'
        }
    }
    ```
 5. Migate Database
 ```shell
 $ python manage.py migrate
 ```
 6. Run server
 ```shell
 $ python manage.py runserver
 ```
