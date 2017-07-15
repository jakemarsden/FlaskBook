from flaskbook import app
from flaskbook.ui.ui import Page, render


@app.route('/')
@app.route('/index')
def get_index():
    return render('index.html', Page())
