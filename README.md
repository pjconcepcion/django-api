# django-api

## Models 

  **Users** - List of Users

  **Results** - List of Users Results per Lesson

  **Lesson** - List of Lessons

  **Question** - List of Question of a Lesson

  **Choice** - List of choices per Question

## Apps

  **Lesson** - Application Lesson

  **Users** - Users and User's Result

## Dependencies

  - corsheaders

  - rest_framework

  - python-dotenv

## Usage

  1. python3 manage.py migrate

  2. python3 manage.py loaddata seed.json

  3. python3 manage.py test