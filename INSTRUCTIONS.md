<h1 align="center">
  Instructions on specific usages
</h1>

<h3>saveUP API - local setup</h3> 
To start the project locally clone the repository, start a virtual environment (using pipenv, virtualenv or similar) and install the requirements from pipfile/requirements.txt. Next, run the following commands:
<ul>
<li>./ manage.py makemigrations - add migrations</li>
<li>./ manage.py migrate - migrating the db</li>
<li>./ manage.py runserver - see the project at localhost</li>
</ul>
To access the admin panel create the superuser using the command:
<ul>
<li>./ manage.py createsuperuser</li>
</ul>

<h3>Simulationg authentication</h3> 
In order to access private data in the db user is required to pass a token in the request's header. In order to simulate this install a chrome extension: mod header (see: https://chrome.google.com/webstore/detail/modheader/) or similar.
Next, follow the steps:
<ul>
<li>Go to user/create to create a new user</li>
<li>Go to user/token to get an authentication token</li>
<li>In mod header extension create a new Request Header</li>
<li>In the field name choose Authentication</li>
<li>In the field Value pass the following: Token &#60;your_token_key&#62; (important: notice the whitespace betweend the Token and key!)</li>
<li>Make a request</li>
</ul>
Now all your requests will include the header values.

<h3>Local db copy - for collaborators and contributors</h3> 
Django creates sqlite3 database locally. Instead of keeping the database in the repository, add a fixture so other users can fill their database with your content if necesary. Use the following commands:
<ul>
<li>./ manage.py dumpdata > [file name].json - creates a copy of the database in json file</li>
<li>./ manage.py loaddata [file name].json - fill the database with content from json file</li>
</ul>
For reference visit: https://coderwall.com/p/mvsoyg/django-dumpdata-and-loaddata