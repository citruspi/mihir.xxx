import sys
from flask import Flask, render_template
from flask_flatpages import FlatPages
from flask_frozen import Freezer

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)

@app.route('/')
def index():
    return render_template('index.html', pages=pages)

@app.route('/tag/<string:tag>/')
def tag(tag):
    tagged = [p for p in pages if tag in p.meta.get('tags', [])]
    return render_template('tag.html', pages=tagged, tag=tag)

@app.route('/cat/<string:cat>/')
def cat(cat):
    filed = [p for p in pages if cat in p.meta.get('category')]
    return render_template('cat.html', pages=filed, cat=cat)


@app.route('/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)
    
@app.route('/map/')
def fourohfour():
    return render_template('map.html')

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    elif len(sys.argv) > 1 and sys.argv[1] == "serve":
        app.run(port=8000)
    else:    
        print "You seem to be missing something..."
