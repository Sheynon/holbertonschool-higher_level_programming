from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Render the home page template

@app.route('/about')
def about():
    return render_template('about.html')  # Render the about page template

@app.route('/contact')
def contact():
    return render_template('contact.html')  # Render the contact page template

if __name__ == '__main__':
    app.run(debug=True, port=5000)
