from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    text= """
    <h1>hello world</h1>
    """
    return render_template('jinja2.html', text=text)

if __name__ == '__main__':
    app.run()