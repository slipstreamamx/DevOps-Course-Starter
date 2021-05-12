from flask import Flask, render_template, redirect,request
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

@app.route('/complete', methods=['POST'])
def completeItem():
    c_id = request.form.get('btn-complete')
    item = get_item(c_id)
    item['status'] = 'Completed'
    save_item(item)
    return redirect('/')

@app.route('/remove', methods=['POST'])
def removeItem():
    r_id = request.form.get('btn-remove')
    item = get_item(r_id)
    remove_item(item)
    return redirect('/')


if __name__ == '__main__':
    app.run()
