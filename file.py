from flask import Flask, render_template
 
app = Flask(__name__)
 
@app.route('/file/')
def readFile():
	text = open('file.txt', 'r+')
	content = text.read()
	text.close()
	return render_template('content.html', text=content)
 
@app.route('/sobre/')
def sobre():
	return render_template('sobre.html')



@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)