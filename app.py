from flask import Flask, render_template, url_for, redirect
from forms import LoginForm, RegistrationFrom
app = Flask(__name__)

app.config['SECRET_KEY'] = '2fd56da00602826cb7800e16af1d0ee8'


posts = [
    {
        'auther' : 'Ilyes Sellam',
        'title' : 'Blog Post 1',
        'content' : 'This is my first flask app',
        'date_posted': 'April 20, 2022'
    },
    {
        'auther' : 'Amine Ketfi',
        'title' : 'Blog Post 2',
        'content' : 'This is my first flask app me too',
        'date_posted': 'April 21, 2022'
    }
]



@app.route("/")
@app.route("/home")
def index():
    return render_template('index.html', posts = posts, title="Home")


@app.route("/about")
def about():
    return render_template('about.html', title="About")


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


@app.route("/register")
def register():
    form = RegistrationFrom()
    return render_template('register.html', title='Register', form=form)



if __name__ == '__main__':
    app.run(debug=True)

