from flask import Flask, render_template, request, url_for, flash, redirect
import sqlite3
from werkzeug.exceptions import abort


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

def get_job(job_id):
    conn = get_db_connection()
    job = conn.execute('SELECT * FROM jobs WHERE id = ?',
                        (job_id,)).fetchone()
    conn.close()
    if job is None:
        abort(404)
    return job

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'

@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    jobs = conn.execute('SELECT * FROM jobs').fetchall()
    conn.close()
    return render_template('index.html', posts=posts, jobs=jobs)

@app.route('/post/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
        
    return render_template('create.html')

@app.route('/new_job', methods=('GET', 'POST'))
def create_job():
    if request.method == 'POST':
        job_title = request.form['job_title']
        company = request.form['company']
        remote_q = request.form['remote_q']
        applied = request.form['applied']
        applied_date = request.form['applied_date']
        link = request.form['link']
        comments = request.form.get('comments', '')

        if not job_title:
            flash('Job Title is required!')
        
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO jobs (job_title, company, remote_q, applied, applied_date, link, comments) VALUES (?, ?, ?, ?, ?, ?, ?)',
                        (job_title, company, remote_q, applied, applied_date, link, comments))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    
    return render_template('new_job.html')

@app.route('/job/<int:job_id>')
def job(job_id):
    job = get_job(job_id)
    return render_template('job.html', job=job)



