from bottle import Bottle, run

app = Bottle()

@app.route('/hello')
def hello():
	return "Hello world!!!"

# if __name__ == '__main__':
# 	app.run()

run(app)