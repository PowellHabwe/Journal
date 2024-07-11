SETTING UP THE BACKEND

# Journal
# Clone the app and set it up in your local environment.
# Create a development environment 
# For those in Ubuntu,you can set it up using the following commands 

# python -m venv journal_env
# source journal_env/bin/activate

# Install the dependencies by running pip install -r requirements.txt

# You can install and use PostMan to test the api endpoints

SETTING UP THE DATABASE

# Install the following packages to help out with the database
sudo apt-get install -y build-essential libssl-dev libffi-dev python3-dev python3-pip
sudo apt-get install -y pkg-config libmysqlclient-dev


# Make sure mysqlclient is installed and if not,run the following command

pip install mysqlclient


# Create the Mysql db using the command 

sudo mysql -u root -p


# In the shell,run the following commands 

CREATE DATABASE journal_db;
CREATE USER 'journal_user'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON journal_db.* TO 'journal_user'@'localhost';
FLUSH PRIVILEGES;
EXIT;


# In your settings,add this to the database section

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'journal_db',
        'USER': 'journal_user', --The name you used in the creation of the db
        'PASSWORD': 'your_password', --The Password you used in the creation of the db
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# Apply the migrations

python manage.py migrate


 ****** HAPPY PROGRAMMING ******
