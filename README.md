# Shuup Project Template

Use this template for simple Django project with Shuup.

1. Clone to your local environment
2. Install and test Shuup without workbench
3. Attach your addons and custom business logic
4. Push to your project repository

## Installation

1. Create and activate fresh Python virtualenv
2. Run `pip install -r requirements.txt`.
3. Optionally copy .env.template to .env and setup environment variables for your project.
   You can also modify Django settings directly to the settings file or setup local settings file.
4. Initialize database by running `python manage.py migrate`
5. Initialize installation by running `python manage.py shuup_init`
6. Create superuser to access admin `python manage.py createsuperuser`
7. Run server `python manage.py runserver 0.0.0.0:8888`
8. Navigate to `127.0.0.1:8888/sa` and login
9. Complete Shuup onborading wizard and you should be all set
10. Now for your own project you can just update ``git remote`` with your
    own git repository and start pushing new commits. For example
    ``git remote set-url origin git@github.com:username/shuup-project-template.git``
