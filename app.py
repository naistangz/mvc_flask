from flask import Flask, render_template

# In order for us to use flask we need to create an instance of our app
# Syntax to create flask instance
app = Flask(__name__)

# Creating a method to display on our default home page
# Syntax for decorators to create a web route
@app.route('/')
def index():
    return render_template('home.html')

"""
Exercise:
1. Create a function called welcome_user
2. Create a decorator to link the page/user
3. Return 'Welcome to Python Flask { user }
"""

@app.route('/welcome_user')
def welcome_user():
    return render_template('welcome_user.html')


# index method will be called at the endpoint
# index method will display on our home page
# syntax to run our app
if __name__ == '__main__':
    # reflects changes and updates without CTRL+C to rerun the app
    app.run(debug=True)
