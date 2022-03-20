from flask import Flask, render_template, url_for,redirect
app = Flask(__name__)


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



if __name__ == '__main__':
    app.run(debug=True)

