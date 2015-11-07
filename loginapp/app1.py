from flask import Flask,render_template,redirect,url_for,request
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World!'

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template

# route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'Admin' or request.form['password'] != 'Admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=7000)

