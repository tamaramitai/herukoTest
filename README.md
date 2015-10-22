To create a simple bottle + heroku project from scratch:

* `git init`
* `pip install bottle`
* Craft your server (can be based on [`server.py`](./server.py)).
* Add a [`requirements.txt`](./requirements.txt)) file with your project requirements.
  (heroku uses this to detect this is a python project).
* Add a [`Profile`](./Profile) with a command to launch your server.
* Add a [`runtime.txt`](./runtime.txt) to specify the require python version.
* `git add` and `git commit` your stuff.
* If this is the first time you run the heroku toolbelt on your computer, run `heroku login`.
* Use `heroku create` to create an app on your heroku account.
* `git push heroku master`.  Check the output of the command!
* `git open`, sit back and enjoy :-)


Resources:

* [Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python#introduction)
* [bottle](http://bottlepy.org/docs/dev/index.html)
