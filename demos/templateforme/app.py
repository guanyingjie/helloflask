from flask import Flask, render_template, Markup

app = Flask(__name__)

user = {
    'username': 'yingjie',
    'bio': '123456',
}
movie = [
    {'name': '陈情令','actor':'王一博,肖战'},
    {'name': 'Three Colours trilogy', 'year': '1993'},
    {'name': 'Forrest Gump', 'year': '1994'},
    {'name': 'Perfect Blue', 'year': '1997'},
    {'name': 'The Matrix', 'year': '1999'},
    {'name': 'Memento', 'year': '2000'},
    {'name': 'The Bucket list', 'year': '2007'},
    {'name': 'Black Swan', 'year': '2010'},
    {'name': 'Gone Girl', 'year': '2014'},
    {'name': 'CoCo', 'year': '2017'},
]
@app.route('/watchlist')
def watchlist():
    return render_template('watchlist.html', user=user, movie=movie)

@app.route('/')
def index():
    return render_template('index.html')

#设置模板全局变量

@app.context_processor
def inject_foo():
    foo="I am foo"
    return dict(foo=foo)
#just like return {foo:foo}

@app.template_global()
def bar():
    return "i am bar"

@app.template_filter()
def musicial(s):
    return s + Markup(' &#9835')

@app.template_test()
def baz(n):
    if n == 'baz':
        return True
    else:
        return False