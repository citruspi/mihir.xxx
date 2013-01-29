import sys
import yaml
import markdown
from flask import Flask,render_template
from flask_flatpages import FlatPages
from flask_frozen import Freezer

config = yaml.load(open('config.yaml'))

DEBUG = True
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'posts'

app = Flask(__name__,
            static_folder='themes/'+config['theme']+'/static',
            template_folder='themes/'+config['theme']+'/templates')
app.config.from_object(__name__)
posts = FlatPages(app)
freezer = Freezer(app)

@app.template_filter('markdown')
def md(s):
    return markdown.markdown(s, extensions=['extra'])

@app.route('/')
def index():
    return render_template('index.html', posts=posts, config=config)

@app.route('/tag/<string:tag>/')
def tag(tag):
    tagged = [p for p in posts if tag in p.meta.get('tags', [])]
    return render_template('tag.html', posts=tagged, tag=tag, config=config)

@app.route('/cat/<string:cat>/')
def cat(cat):
    filed = [p for p in posts if cat in p.meta.get('category')]
    return render_template('cat.html', posts=filed, cat=cat, config=config)

@app.route('/author/<string:author>/')
def author(author):
    authored = [p for p in posts if author in p.meta.get('author')]
    return render_template('author.html', posts=authored, author=author, config=config)

@app.route('/<path:path>/')
def post(path):
    post = posts.get_or_404(path)
    return render_template('page.html', post=post, config=config)

@app.route('/404/')
def fourohfour():
    return render_template('404.html', config=config)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', config=config)

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    elif len(sys.argv) > 1 and sys.argv[1] == "serve":
        app.run(port=8000)
    else:    
        print "You seem to be missing something..."