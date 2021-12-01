# User-Login using Google O-Auth and custom login 🧑🏼‍💻

Set up by running these commands:
- pip3 install -r requirements.txt (Installing dependencies)
- python -m venv .venv (make .venv folder)
- source .venv/bin/activate (activate virtual env, normally done automatically by IDE)
- python manage.py migrate
- python manage.py createsuperuser (set superuser)

** Important **
- Login to the admin panel
- Under Sites add domain name and display name as - 127.0.0.1:8000
- Under "Social Applications" paste the below credentials
- Provider - Google
- Client id - 139111117065-umfppllolivahespq1h9g9qjc6kn7o6r.apps.googleusercontent.com
- Secret key - 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

Allow users to set up their account
- By registering on website
- Login via Gmail account
- Password reset using Email if registered via Gmail

Tech-Stack used ⚙
 - Django
 - SQLlite3
 - Ajax
 - Python
 - Javascript
 - HTML, CSS, BOOTSTRAP(front-end)
 - django-allauth for integrating Google oauth2
