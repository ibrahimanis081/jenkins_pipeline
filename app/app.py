from flask import Flask, render_template

app = Flask(__name__)

# Define a route for the homepage
@app.route('/')
def home():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)

