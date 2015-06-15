### This is a Bottle app served with Gunicorn or uWSGI.

For some reason when I use the following snippet with Gunicorn it works and reports data to the UI:

```
from bottle import Bottle, run

app = Bottle()

@app.route('/hello')
def hello():
	return "Hello world!!!"

if __name__ == '__main__':
	app.run()
```

When I run the app with uWSGI, I need to revise the code to the following in order for it to run and report data to the UI.

```
from bottle import Bottle, run

app = Bottle()

@app.route('/hello')
def hello():
	return "Hello world!!!"

run(app)
```

