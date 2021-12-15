# Python_Django

# https://art-of-engineer.blogspot.com/2021/06/python-django-mysql-rest-api-tutorial.html

Lets install the necessary modules needed for our Django project.


First lets install the Django module.

>> pip install django

To create rest APIs we need to install Django rest framework.

>> pip install djangorestframework

By default, the Django project comes with a security that blocks requests coming from different domains. To disable this, lets install Django CORS headers module.

>> pip install django-cors-headers

Now lets create the Django project.

Open the command prompt in the desired folder and type the command.

>> django-admin start project <name of the project>

  
>> python manage.py runserver
  
  
http://127.0.0.1:8000/
