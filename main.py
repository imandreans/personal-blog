from flask import Flask, redirect, url_for, render_template, make_response, request
from functools import wraps
from blogs import Blogs

app = Flask(__name__)
#function to verify the authorization of user
def auth_required(func):
    
    @wraps(func) #keeps the original metadata of the func
    # a wrapper function.
    def decorated(*args, **kwargs):
        auth = request.authorization
        # Check the authorization, username and password
        if auth and auth.username == 'username1' and auth.password == 'password':
            # Call the decorated function
            return func(*args, **kwargs)
                                                        #Status    Header                
        return make_response('Could not verify your login!', 401, {'WWW-Authenticate': 'Basic realm="Login Required!"'})
    return decorated

#create path name home
@app.route('/')
def home():
    list_blogs = Blogs().show_blogs()
    return render_template('home.html', list_blogs=list_blogs)

@app.route('/new')
@auth_required
def new():
    return render_template('new-article.html')

@app.route('/admin')
@auth_required
def admin():
    list_blogs = Blogs().show_blogs()
    return render_template('admin.html', list_blogs=list_blogs)

@app.route('/publish', methods=['POST'])
@auth_required
def publish():
    # title and content is received
    title = request.form['title']
    content = request.form['content']
    # new blog is being added to the json file
    Blogs().add_blog(title, content)
    # redirect to admin page
    return redirect(url_for('admin'))

@app.route('/article/<id>')
def view_article(id: int):
    blog = Blogs().show_blogs()[int(id)-1]
    return render_template('article.html', blog=blog)

@app.route('/delete/<id>')
def delete_article(id: int):
    Blogs().delete_blog(int(id))
    return redirect(url_for('admin'))

@app.route('/edit/<id>')
@auth_required
def edit_article(id:int):
    blog = Blogs().show_blogs()[int(id)-1]
    return render_template('edit-article.html', blog=blog) 

@app.route('/update/<id>', methods=['POST'])
@auth_required
def update_article(id: int):
    title = request.form['title']
    content = request.form['content']
    Blogs().update_blog(int(id), title, content)
    return redirect(url_for('admin'))

# def url_back()
# @app.route('/test')
# def test():
#     user = 'admin'
#     if user == 'admin':
#         #redirect a user to another route with input
#         return redirect(url_for("greeting", name='Admin'))
#     else:
#         #redirect a user to another route/link
#         return redirect(url_for("home"))



