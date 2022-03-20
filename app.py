from flask import Flask, render_template, url_for, redirect, flash
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


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
        
    return render_template('login.html', title='Login', form=form)


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationFrom()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)



if __name__ == '__main__':
    app.run(debug=True)

