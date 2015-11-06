Directly logging in a user in Django tests
##########################################

:date: 2010-09-28 01:50
:slug: tech/17-directly-logging-in-a-user-in-django-tests

The `examples for Django testing`_ point you towards hardcoding a
username and password for a user to impersonate in tests, and
the API of the test client encourages this too.

.. _examples for Django testing: http://docs.djangoproject.com/en/dev/topics/testing/#django.test.client.Client.login

However, Django has a nice pluggable authentication system that
means you can easily use something such as OpenID instead of
passwords.

Putting the passwords in your tests ties you to having the password
support enabled, and while you could do this for just the tests, it's
completely out of the scope of most tests (I'm not talking about any
tests for the actual login process here.)

When I saw this while reviewing code recently I worked with Zygmunt_
to write a Client subclass that didn't have this restriction. With this
subclass you can just choose a User object, and have that client login
as that user, without them having to have a password at all. Doing
this decoples your tests from the implementation of the authentication
system, and makes them target the code you want to test more precisely.

.. _Zygmunt: https://launchpad.net/~zkrynicki

Here's the code::

  from django.conf import settings
  from django.contrib.auth import login
  from django.http import HttpRequest
  from django.test.client import Client


  class TestClient(Client):
  
      def login_user(self, user):
          """
          Login as specified user, does not depend on auth backend (hopefully)
  
          This is based on Client.login() with a small hack that does not
          require the call to authenticate()
          """
          if not 'django.contrib.sessions' in settings.INSTALLED_APPS:
              raise AssertionError("Unable to login without django.contrib.sessions in INSTALLED_APPS")
          user.backend = "%s.%s" % ("django.contrib.auth.backends",
                                    "ModelBackend")
          engine = import_module(settings.SESSION_ENGINE)
  
          # Create a fake request to store login details.
          request = HttpRequest()
          if self.session:
              request.session = self.session
          else:
              request.session = engine.SessionStore()
          login(request, user)
  
          # Set the cookie to represent the session.
          session_cookie = settings.SESSION_COOKIE_NAME
          self.cookies[session_cookie] = request.session.session_key
          cookie_data = {
              'max-age': None,
              'path': '/',
              'domain': settings.SESSION_COOKIE_DOMAIN,
              'secure': settings.SESSION_COOKIE_SECURE or None,
              'expires': None,
          }
          self.cookies[session_cookie].update(cookie_data)
  
          # Save the session values.
          request.session.save()

Then you can use it in your tests like this::

  from django.contrib.auth.models import User


  client = TestClient()
  user = User(username="eve")
  user.save()
  client.login_user(user)


Then any requests you make with that client will be authenticated as the user that
was created.

`Ticket submitted`_ with Django to have this available for everyone in future.

.. _Ticket submitted: http://code.djangoproject.com/ticket/14350
