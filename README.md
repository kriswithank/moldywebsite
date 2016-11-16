# moldyWebsite

Working on a website for a molding/manufacturing company using Django.



# Getting started.

First install the required pip modules:
 * django
 * psycopg2
 * pillow
 * markdown


The easiest way to get started is to clone this repo, open a terminal, navigate to
the project's base directory and run the command

    $ python manage.py runserver
    Performing system checks...

    System check identified no issues (0 silenced).
    August 22, 2016 - 18:55:55
    Django version 1.9.9, using settings 'moldyWebsite.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.

This will start the Django test server, simply open your browser and navigate to
http://127.0.0.1:8000/ (if it is different, use that instead).

Have fun exploring!



# Setting up PostgreSQL database.

### Setting up website_user

To create website_user with appropriate permissions and a password...

    createuser website_user -P

To grant user permissions on database and tables...

    $ psql
    kris=# GRANT ALL PRIVILEGES ON DATABASE moldywebsite TO website_user;
    kris=# \c moldywebsite
    kris=# GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO website_user;

# Documentation.

### What is this?

This is **not** a comprehensive documentation of the whole project. This is simply an overview of the general project structure.

New maintainers will probably find this useful as it describes the project at a high level without specific implementation details.

If you *are* looking documentation on a specific feature or implementation, dive into the source code and look at the docstrings and other inline documentation, there should be enough of it.

### Structure.

Within the project folder, there are many different subdirectories. Each subdirectory is a Django app.

App/Subdirectory | Role
-----------------|------
moldyWebsite     | The base app containing general project settings and the base url conf.
common           | Contains files and features that are a commonality among all apps
home             | Contains files and features specific to the home page.
faqs             | Contains files and features specific to the faqs page.

### Common.

Contains a base template that all apps extend. This base template includes a header and navigation menu and has basic styling for the body.

The navigation menu a model to represent each item in the navigation menu. The order, display text and link of these menu items can be altered in the admin site.

### Home.

Contains a template which extends the common base template, and styling specific for the home page.

### Faqs.



# Notes to myself about deployment.
I used gunicorn and nginx for deployment.

I used a gunicorn daemon for autostarting it. This daemon is located at
'/etc/systemd/system/gunicorn.service'

The nginx configuration file is located at '/etc/nginx/sites-available/moldywebsite',
to enable it to work a symbolic link is the only file in '/etc/nginx/sites-enabled/'

To check nginx config for error, run

    $ sudo nginx -t

To start the nginx server, run

    $ sudo systemctl restart nginx

To restart the gunicorn daemmon, run

    $ sudo systemctl start gunicorn
    $ sudo systemctl enable gunicorn

Whenever you make a change to the website, restart the gunicorn daemon.


# Collecting static files

When deploying, collect the static files, to do this enable the virtual environment

    $ source /home/kris/website/website_env/bin/activate

and collect the static files

    $ cd /home/kris/website/moldywebsite/
    $ ./manage.py collectstatic


# Transfering database to server

First dump the local database

    $ pg_dump database_name > db_dump.sql

where database_name is the name of the database (moldywebsite).

Then transfer the sql dump to the server

    $ scp db_dump.sql kris@krisswann.com:

This puts it in /home/kris on the server.

Now ssh into the server and drop the old db.

    kris@krisswann.com~$ dropdb moldywebsite

Create a new, empty database

    kris@krisswann.com~$ createdb moldywebsite

Populate it with the sql dump

    kris@krisswann.com:~$ psql -d moldywebsite  -f db_dump.sql

To ensure website_user has the proper permissions run the following commands

    kris@krisswann.com:~$ psql database -c "GRANT ALL ON ALL TABLES IN SCHEMA public to website_user;"
    kris@krisswann.com:~$ psql database -c "GRANT ALL ON ALL SEQUENCES IN SCHEMA public to website_user;"
    kris@krisswann.com:~$ psql database -c "GRANT ALL ON ALL FUNCTIONS IN SCHEMA public to website_user;"
