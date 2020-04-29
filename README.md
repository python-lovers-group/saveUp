<h1 align="center">
  saveUp
</h1>

<p align="center">
  <strong>Learn how to save your money!</strong><br>
  Manage your billings with us!
</p>

<h3 align="center">
  <a href="#">Getting Started</a>
  <span> · </span>
  <a href="#">Live demo</a>
  <span> · </span>
  <a href="https://github.com/python-lovers-group">About us</a>
</h3>

**saveUp** is an simple application that will teach you to save your hard-earned money and help you track your expenses.

### Contents 
- [✅ Requirements](#%e2%9c%85-requirements)
- [🪁 Join us](#%f0%9f%aa%81-join-us)
- [📜 License](#%f0%9f%93%9c-license)



## ✅ Requirements
To start the project locally clone the repository, start a virtual environment (using pipenv, virtualenv or similar) and install the requirements from pipfile/requirements.txt. Next, run the following commands:
<ul>
  <li>./ manage.py makemigrations - add migrations </li>
  <li>./ manage.py migrate - migrating the db</li>
  <li>./ manage.py runserver - see the project at localhost</li>
</ul>
<br/>
To access the admin panel create the superuser using the command:
<ul>
  <li>./ manage.py createsuperuser</li>
</ul>
<br/>
Django creates a sqlite3 database locally. Instead of keeping the database in the repository, add a fixture so other users can fill their database with your content if necesary. Use the following commands:
<ul>
  <li>./ manage.py dumpdata > [file name].json - creates a copy of the database in json file</li>
  <li>./ manage.py loaddata [file name].json - fill the database with content from json file</li>
</ul>
For reference visit: https://coderwall.com/p/mvsoyg/django-dumpdata-and-loaddata


## 🪁 Join us
Aliquam ut erat sed nibh varius eleifend. Vestibulum molestie eros et molestie imperdiet. Integer feugiat iaculis varius. Sed posuere neque ut suscipit tempor. Vivamus quis felis eu enim hendrerit hendrerit. Etiam tincidunt tempus erat, et blandit odio. Vivamus vestibulum dui id neque pellentesque egestas nec vitae massa.

## 📜 License
**saveUp** is **MIT licensed**, as found in the [LICENSE][l] file.


[l]: ./LICENSE
