import os
from flask import (
    Blueprint, render_template, request, redirect, url_for,
    flash, jsonify, abort
)
from app import db
from app.models import Post

main = Blueprint('main', __name__)

ADMIN_KEY = os.getenv('FLASK_ADMIN_KEY', 'admin')

@main.route('/')
def index():
    posts = Post.query.order_by(Post.created_at.desc()).limit(5).all()
    featured = posts[0] if posts else None
    if not featured:
        featured = Post(title='No content', slug='no-content', content='Add content via admin')
    return render_template('index.html', posts=posts, featured=featured, title='Home')


@main.route('/posts')
def posts():
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template('posts.html', posts=posts, title='Posts')


@main.route('/post/<slug>')
def post_detail(slug):
    post = Post.query.filter_by(slug=slug).first_or_404()
    return render_template('post_detail.html', post=post, title=post.title)


@main.route('/about')
def about():
    return render_template('about.html', title='About')


@main.route('/admin', methods=['GET', 'POST'])
def admin():
    authorized = False
    if request.method == 'POST':
        key = request.form.get('key')
        if key == ADMIN_KEY:
            authorized = True
            flash('Authorized — manage posts below')
        else:
            flash('Invalid key')
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template('admin.html', authorized=authorized, posts=posts, title='Admin')


@main.route('/admin/create', methods=['POST'])
def create_post():
    title = request.form.get('title')
    slug = request.form.get('slug')
    content = request.form.get('content')
    if not (title and slug and content):
        abort(400, 'Missing fields')
    if Post.query.filter_by(slug=slug).first():
        abort(400, 'Slug already exists')
    p = Post(title=title, slug=slug, content=content)
    db.session.add(p)
    db.session.commit()
    flash('Post created')
    return redirect(url_for('main.admin'))


@main.route('/admin/edit/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    if request.method == 'POST':
        post.title = request.form.get('title')
        post.slug = request.form.get('slug')
        post.content = request.form.get('content')
        db.session.commit()
        flash('Saved')
        return redirect(url_for('main.admin'))
    return render_template('edit_post.html', post=post, title='Edit Post')


@main.route('/admin/delete/<int:post_id>')
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash('Deleted')
    return redirect(url_for('main.admin'))


# ---- JSON API ----
@main.route('/api/posts')
def api_posts():
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return jsonify([p.to_dict() for p in posts])


@main.route('/api/posts/<int:post_id>')
def api_post(post_id):
    p = Post.query.get_or_404(post_id)
    return jsonify(p.to_dict())
