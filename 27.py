from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h1>Welcome!</h1>
        <form action="/login" method="post">
            <input type="text" name="username" placeholder="Enter your name">
            <input type="submit" value="Login">
        </form>
    '''


@app.route('/welcome/<username>')
def welcome(username):
    return f'Welcome {username}!'

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', 'Guest')
    else:
        username = request.args.get('username', 'Guest')
    return redirect(url_for('welcome', username=username))

if __name__ == '__main__':
    app.run(debug=True)