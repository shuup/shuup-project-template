# Shuup Project Template

## Installation

1. Create Python virtualvenv
2. Just in case run `pip install -U pip setuptools wheel`
3. Run `pip install -r requirements.txt`
4. Copy .env.template to .env and create new database for your shop.
   Optionally you can modify Django settings directly to the settings file.
5. Create tables in the database by running `python manage.py migrate`
6. Initialize installation by running `python manage.py shuup_init`
7. Create superuser to access admin `python manage.py createsuperuser`
8. Run server `python manage.py runserver 0.0.0.0:8888`
9. Navigate to `127.0.0.1:8888/sa` and login
10. Conmplete Shuup onborading wizard and you should be all set.
11. Now for your own project you can just update ``git remote`` with your
    own git repository and start pushing new commits. For example
    ``git remote set-url origin git@github.com:username/shuup-project-template.git``.