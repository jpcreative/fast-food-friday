# fast-food-friday

R&amp;D project combining AngularJS, Django Tastypie and Trigger.io 

Every Friday at [JPCreative](http://jpcreative.co.uk) we have a tradition of eating lunch together, sometimes forming a consensus on what to have proves difficult.  Until now!  Introducing the Fast Fast Friday app.

It's a simple proof on concept app for iOS and Android that allows users to sign in via twitter, suggest and vote for their preferred lunch menu. It's coded completely in Python, HTML, CSS and JavaScript.  No native code is used at all.

The back end creates a API using [Django](https://www.djangoproject.com) and [Tastypie](http://tastypieapi.org). The front-end communicates to the API through [AngularJS](http://angularjs.org/) wrapped up into a native app by [trigger.io](https://trigger.io/)

## Installation

To package iOS apps with trigger.io you'll need OSX with Xcode. I'd also suggest you install Xcode command line tools.

### Django

You'll need pip and virtualenvwrapper:
sudo easy_install pip
pip install virtualenvwrapper

```bash
$ mkvirtualenv authAppEnv
(authAppEnv)$ pip install -r requirements.txt
(authAppEnv)$ cd authApp
(authAppEnv)$ python manage.py syncdb
(authAppEnv)$ sudo python manage.py runserver YOUR-IP-HERE:80
```
That should get a local version of the API running.
The reason for using sudo and your IP with runserver will become clear when getting angular running locally.

### Angular.js

TODO

### Trigger.io

TODO