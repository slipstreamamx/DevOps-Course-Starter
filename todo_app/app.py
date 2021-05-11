from flask import Flask, render_template
from flask.globals import request
from werkzeug.utils import redirect
from todo_app.data.session_items import *

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():
    return render_template('index.html', all_items=get_items())

@app.route('/addItem', methods=['GET', 'POST'])
def addItem():
    if request.method == 'POST':
        title = request.form.get('inputItem')
        add_item(title)
        return redirect('/')
    else:
        return redirect('/')

if __name__ == '__main__':
    app.run()
