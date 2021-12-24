# Python Flask / Routing
from flask import Flask
from flask import request, render_template
from markupsafe import escape

app = Flask(__name__)

# @app.route('/<page_name>')
# def hello_world(page_name):
#     html =  "Hello, World! <br/> <h1>Hello, World!</h1>"
    # html += "This is {} page".format(page_name)
    # return html

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    pets = ['cat', 'dog', 'bird', 'fish']
    pet_name = {'cat' : 'cccc', 'dog' : 'dddd'}
    return render_template("hello.html", template_name=name, pet_list=pets, pet_names=pet_name)

# @app.route('/user/<username>', methods = ['GET'])
# def show_user_profile(username):
#     return f"User {escape(username)}"

# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     return f"Post {post_id}"

# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     return f"Subpath {escape(subpath)}"

# @app.route('/login', methods = ['GET', 'POST'])
# def login():
#     if request.method == "POST":
#         return do_the_login()
#     else:
#         return show_the_login_form()

# def do_the_login():
#     return f"Do the login :: used HTTP Request is {request.method}"

# def show_the_login_form():
#     return f"Show the login form :: used HTTP Request is {request.method} <br/> and this is the login form"

if __name__ == "__main__":
    app.run()