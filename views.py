from flask import  Flask,Blueprint, request , jsonify, render_template, redirect,url_for, flash
from app import app,db, csrf
from models import User
from models import Address
from app import login_manager
from flask_login import current_user, login_user, logout_user
from forms import LoginForm, SignupForm, AddresForm , ProfileForm

my_view = Blueprint('my_view', __name__)


@login_manager.user_loader
def load_user(id):
    """
    @login_manager.user_loader
    def load_user(user_id):
        return User.get(user_id)
    It should return None (not raise an exception)
    if the ID is not valid. (In that case, the ID will manually be removed from the session and processing will continue
    """
    return User.query.filter_by(id=id).first()
    # return  User.query.get(int(id))



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/page', methods=['GET'])
def page():

    # form = Address()
    # if Form.validate_on_submit():
    #     exitting_form = Address.query.filter_by(name = name).first()

    return render_template('page.html')


@app.route('/signup', methods=['GET','POST'])
def signup():

    if current_user.is_authenticated:
        return redirect(url_for('login'))

    form = SignupForm()
    # print(form.validate_on_submit())
    if form.validate_on_submit():
        exitting_user = User.query.filter_by(email=form.email.data).first()
        if exitting_user is None:
            user = User(
                name= form.name.data,
                last_name = form.last_name.data,
                email = form.email.data,
            )
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('login'))

        flash('A user already exists with that email address')
    
    return render_template('signup.html', form=form)


@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('page'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            flash('Invalid username')
            return redirect(url_for('signup'))
        
        elif not  user.check_password(password= form.password.data):
            flash('Invalid password ')
            return redirect(url_for('signup'))
        else:
            login_user(user)
            flash('Logged in successfully.')
            return redirect(url_for('page'))

          
      
    return render_template('login.html',form=form)     

   

@app.route('/address', methods=['GET','POST'])
def address():

    if not  current_user.is_authenticated:
        return redirect(url_for('signup'))

    form = AddresForm()
    if form.validate_on_submit():
        address = Address.query.filter_by(user_id=current_user.id).first()
        if not address:
            address = Address(
                name = form.name.data,
                user_id = current_user.id
            )
            db.session.add(addres)
            db.session.commit()
            flash('Address added')
        else:
            address.name = form.name.data
            db.session.commit()
            flash('Edit Address')
                
            
            

    return render_template('address.html', form=form)        


@app.route("/logout", methods=["GET"])
# @login_required
def logout():
    """Logout the current user."""
    user = current_user
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    return redirect(url_for('signup'))




@app.route('/profile', methods=['GET','POST']) 
def profile():

    if not  current_user.is_authenticated:
        return redirect(url_for('signup'))

    form = ProfileForm()
    if form.validate_on_submit():
        user =current_user
        print(user)
        user.name = form.name.data
        user.last_name = form.last_name.data
              
        db.session.commit()
        flash('Edit user')
    return render_template('profile.html', form=form)    











