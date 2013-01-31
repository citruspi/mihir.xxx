.. _get-started:

Getting Started
===============

*Note: You should run this in a virtualenv.*


Make a folder
------------------

Create a new directory for the site:

    $ cd ~
    $ mkdir site
    $ cd site


Download ford
------------------

From Github: 

    $ git clone http://github.com/citruspi/ford.git

From Bit Bucket:

    $ git clone http://github.com/citruspi/ford.git

*Note: It doesn't matter which repository you get it from - they're identical.*

Check that it fully downloaded:

    $ ls
    requirements.txt    config.yaml     ford.py
    docs                themes          posts

Install dependencies:

    $ pip install -r requirements.txt


Write Some Content
--------------------

For each post, make a Markdown file:

    $ touch posts/hello-world.md

Use any editor you want for editing posts:

    $ sublime posts/hello-world.md

Posts should look like this:

    title: hello world
    date: 2013-01-27
    tags: [hello, stuff]
    author: mark twain
    category: general

    And then the body of the post here.....

*Tip: Only files ending in .md are recognized as posts. Save files with other extensions in order to save them as drafts.*


Run the website
-----------------

Now that you have some content, let's see how it looks:

    $ python ford.py serve

In a web browser, open ``127.0.0.1:8000`` to see your blog in action.

Satisfied? Let's build it.


Build the website
------------------

In order to serve a static copy, we have to generate one:

    $ python ford.py drive