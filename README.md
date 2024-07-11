SETTING UP THE BACKEND

# Journal
# Clone the app and set it up in your local environment.
# Create a development environment 
# For those in Ubuntu,you can set it up using the following commands 

python -m venv journal_env
source journal_env/bin/activate

# Install the dependencies by running 

pip install -r requirements.txt

# You can install and use PostMan to test the api endpoints

SETTING UP THE DATABASE

# Install the following packages to help out with the setup and running database
sudo apt-get install -y build-essential libssl-dev libffi-dev python3-dev python3-pip
sudo apt-get install -y pkg-config libmysqlclient-dev


# Make sure mysqlclient is installed and if not,run the following command

pip install mysqlclient


# Create the Mysql db using the command 

sudo mysql -u root -p


# In the shell,run the following commands 

CREATE DATABASE journal_db; #Input The Name of your db \
CREATE USER 'journal_user'@'localhost' IDENTIFIED BY 'your_password'; #This Is Where You Input Your Name and Password \
GRANT ALL PRIVILEGES ON journal_db.* TO 'journal_user'@'localhost'; \
FLUSH PRIVILEGES; \
EXIT; \


# In your settings there is this code block

DATABASES = { \
    'default': { \
        'ENGINE': 'django.db.backends.mysql', \
        'NAME': 'journal_db', #Change To The Name Of Your Db \
        'USER': 'journal_user', #Change To The name you used in the creation of the db \
        'PASSWORD': 'your_password', #Change To The Password you used in the creation of the db \
        'HOST': 'localhost', \
        'PORT': '3306', \
    } \
 \}

# Apply the migrations

python3 manage.py migrate



# ENDPOINT DOCUMENTATION \

# path("journalpost/", views.JournalPostListCreate.as_view(), name="note-list") \
Method: GET, POST \
Description: \
GET: Retrieve a list of all journal entries created by the authenticated user. \
POST: Create a new journal entry. \
Permissions: Requires authentication. \

# path("journalpost/delete/<int:pk>/", views.JournalPostDelete.as_view(), name="delete-note") \
Method: DELETE \
Description: Delete a specific journal entry by its primary key (pk). \
Permissions: Requires authentication. \

# path('journalpost/<int:pk>/', views.JournalPostRetrieveUpdateDestroy.as_view(), name='retrieve-update-destroy-journal') \
Method: GET, PUT, DELETE \
Description: \
GET: Retrieve a specific journal entry by its primary key (pk). \
PUT: Update a specific journal entry. \
DELETE: Delete a specific journal entry. \
Permissions: Requires authentication. \

# path('journals/summary/', views.JournalPostSummaryView.as_view(), name='summary-journal') \
Method: GET \
Description: Retrieve a summary of journal entries for a given period (daily, weekly, monthly). \
Permissions: Requires authentication. \
Query Parameters: period (optional, defaults to 'daily') \

# path("categories/", views.CategoryListCreate.as_view(), name="category-list-create") \
Method: GET, POST \
Description: \
GET: Retrieve a list of all categories. \
POST: Create a new category. \
Permissions: Requires authentication. \


# USER MANAGEMENT ENGPOINTS

# path("api/user/register/", CreateUserView.as_view(), name="register") \
Method: POST \
Description: Register a new user. \
Permissions: Open to all (no authentication required). \

# path("api/user/profile/", UserProfileView.as_view(), name="profile") \
Method: GET, PUT \
Description: \
GET: Retrieve the profile information of the authenticated user. \
PUT: Update the profile information of the authenticated user, including username and password. \
Permissions: Requires authentication.

# path("api/token/", TokenObtainPairView.as_view(), name="get_token") \
Method: POST \
Description: Obtain JWT token for user authentication. \
Permissions: Open to all (no authentication required). \

# path("api/token/refresh/", TokenRefreshView.as_view(), name="refresh") \
Method: POST \
Description: Refresh the JWT token. \
Permissions: Open to all (no authentication required). \

# path("api-auth/", include("rest_framework.urls")) \
Description: Default login and logout views for the browsable API. \
Permissions: Open to all (no authentication required). \



 ****** HAPPY PROGRAMMING ******
