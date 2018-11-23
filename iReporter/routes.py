from flask import jsonify
from flask import render_template, url_for, flash, redirect, request, abort
from iReporter import app
from iReporter.forms import RegistrationForm, LoginForm, PostForm, UpdateAccountForm


posts = [
    {
        'author': 'JabMN',
        'title': 'Issue Title 1',
        'content': 'First post content',
        'date_posted': 'November 16 2018'
    },
    {
        'author': 'test_user',
        'title': 'Issue Title 1',
        'content': 'Second post content',
        'date_posted': 'November 16 2018'
    }
]
users = [
    {
        'username': 'JabMN',
        'email': 'cenajab@gmail.com',
        'password': 'password'
    },
    {
        'username': 'test_user',
        'email': 'test_user@demo.com',
        'password': 'password'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}! ? (Not operational)', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'user@ireporter.com' and form.password.data == 'password':
            flash('This provision is not yet operational! ? (Logged in)', 'success')
            return redirect(url_for('account'))
        else:
            flash('This provision is not yet operational! ? (Wrong username or password)', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/account", methods=['GET', 'POST'])
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        flash(f'Account Update for {form.username.data}! ? (Not operational)', 'success')
        return redirect(url_for('home'))
    elif request.method == 'GET':
        form.username.data = 'JabMN'
        form.email.data = 'jabmn@ireport.com'
        return render_template('account.html', title='Account', form=form)


@app.route("/logout")
def logout():
    return redirect(url_for('home'))

@app.route("/issue")
def issue():
    return render_template('issue.html')

@app.route("/post/new", methods=['GET', 'POST'])
def report_issue():
    form = PostForm()
    if form.validate_on_submit():
        flash('This fuction is not yet available!', 'success')
        return redirect(url_for('home'))
    return render_template('report_issue.html', title='New Post',
                           form=form, legend='New Post')

@app.route("/user_issues")
def user_issues():
    return render_template('user_issues.html')

@app.route("/reported_issues")
def reported_issues():
    return render_template('reported_issues.html', posts=posts)