# flask-api-sample

A simple Flask API authentication example, powered by Stormpath.


## Premise

Let's say you're building an API service in Flask.  You have a great API, but
now you need to add user accounts, authentication, etc.

You could just roll your own custom authentication using SQLAlchemy, by doing
like this:

1. Define a User model.
2. Get a database server.
3. Get your user model setup on the database.
4. Install the alembic package to handle database migrations.
5. Create your users.
6. Wire up some form of API authentication using HTTP Basic Auth with Flask.
7. Scale your database relationships / authentication framework as your userbase
   grows.
8. Profit!

The alternative, using Stormpath, is to push the burden of authentication /
authorization / security / scalability onto Stormpath itself:

1. Create a Stormnpath application.
2. Make users for your application.
3. Have your developers hit your API service using HTTP Basic Auth, then pass
   the credentials onto Stormpath to authenticate / authorize / etc.
4. Profit!

Stormpath is pretty nice because not only do you get secure and scalable user
stuff handled, you can also store any user data along with the model in a
key-value store (JSON).


## Usage

The sample app you'll find in this repository implements a simple API service in
Flask. The way it works is simple:

- Developers hit your API endpoint with their username / email and password.
- The Flask code authenticates this user via Stormpath.
- Depending on whether or not the user's credentials are valid, you'll get back
  either a 401 UNAUTHORIZED, or a 200 OK.

This sample is meant to show you how to interact with the Stormpath API in a
basic manner by authenticating users.

To get started with this sample, you need a few things:

- A Stormpath account. If you don't have one, go make one!
  https://api.stormpath.com/register

- A Stormpath application named 'flask-api-sample'. **NOTE**: If you don't like
  the name, feel free to modify the source code and do whatever you want!

- You also need to create at least one user account in your application (to test
  with!).

Once you have the above stuff running, clone this project, so you have it
locally, then you can get things running!

```bash
$ git clone git@github.com:stormpath/flask-api-sample.git
$ cd flask-api-sample
$ pip install -r requirements.txt
$ python app.py # run the server
```

In another shell, you can test out the API like so:

```bash
$ curl -v 'http://localhost:5000'
$ # The above request will fail, as no credentials were supplied.

$ curl -v --user 'woot:woot' 'http://localhost:5000'
$ # The above request will fail, as the username/password are wrong.

$ curl -v --user '<username_or_email>:<password>' 'http://localhost:5000'
$ # This will work if you supply the correct credentials.
