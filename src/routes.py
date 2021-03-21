from src import app, db, APP_PATH
from flask import render_template, url_for, abort, request, redirect, flash, session, jsonify
from flask_login import login_user, logout_user, current_user
# from src.models import User, Product, Order, load_user
from src.models import User
from src.forms import RegistrationForm, ReviewForm, LoginForm, EditProductForm, CheckoutForm, PublishProductForm, UnpublishProductForm, DeleteProductForm, AllProductsForm, AddCartForm
from werkzeug.utils import secure_filename
import os
import time
from random import seed, randint, choice

def addtocart(form):
    product_id = form.product_id.data
    quantity = int(form.quantity.data)
    if "Shoppingcart" not in session:
        session["Shoppingcart"] = dict()
    if product_id in session ["Shoppingcart"]:
        session["Shoppingcart"][product_id] = str(int(session["Shoppingcart"][product_id]) + quantity)
    else:
        session["Shoppingcart"][product_id] = str(quantity)
    session.modified = True
    flash("Added product to basket.", category='good')

@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    form = AddCartForm()
    if form.validate_on_submit():
        addtocart(form)

    seed(int(round(time.time() * 1000)))
    # possible_choices = []
    # product_data = Product.query.filter_by(active=True)
    # for product in product_data:
    #     possible_choices.append(product.id)
    # chosen = choice(possible_choices)
    # product = Product.query.get_or_404(chosen)
    # return render_template('home.html', title='Home', product_data=product, addcartform=form)
    return render_template('home.html', form=form)

# @app.route("/about")
# def about():
#     return render_template('about.html', title='About')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if (form.validate_on_submit()):
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(password=form.password.data):
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash("Login unsuccessful! Invalid username or password.", category='bad')
    return render_template('login.html', title='Sign In', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if (form.validate_on_submit()):
        user = User(username=form.username.data, email=form.email.data, password=form.password.data, admin=False)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template('register.html', title='Register', form=form)

@app.route("/accountDetails")
def accountDetails():
    return render_template('accountDetails.html', title='accountDetials')

@app.route("/confirm")
def confirm():
    return render_template('confirm.html', title='Confirm')


# @app.route("/basket")
# def basket():
#     if "Shoppingcart" not in session:
#         session["Shoppingcart"] = dict()
#     products = list()
#     quantitys = list()
#     total = 0
#     for id in session['Shoppingcart']:
#         product = Product.query.get(id)
#         if product != None:
#             products.append(product)
#             quantitys.append(session['Shoppingcart'][id])
#             total += float(session['Shoppingcart'][id]) * float(product.basePrice)
#
#     return render_template('basket.html', title='Shopping Basket', products=products, quantitys=quantitys, total=total)



# @app.route("/checkout", methods=['GET', 'POST'])
# def checkout():
#     form = CheckoutForm()
#     if (form.validate_on_submit() and current_user.is_authenticated):
#         if "Shoppingcart" not in session:
#             session['Shoppingcart'] = dict()
#         session['Orders'] = dict()
#         session['Orders']['List'] = []
#         for id in session['Shoppingcart']:
#             order = Order(userid=int(current_user.id), transactionid=int(current_user.transactionid), productid=int(id), quantity=int(session['Shoppingcart'][id]))
#             session['Orders']['List'].append(order.to_dict())
#         return redirect(url_for('review_checkout'))
#     return render_template('checkout.html', form=form, title='Checkout')

# @app.route("/products", methods=['GET'])
# @app.route("/products/page/<int:pagenum>", methods=['GET'])
# def products(pagenum = 1):
#
#
#     form = AllProductsForm()
#     recordNo = 10
#     #Product.query.count()
#
#     if 'Sort' in request.args:
#         sortingcriteria = request.args['Sort']
#     else:
#         sortingcriteria = "None"
#     if 'Perpage' in request.args:
#         recordNo = int(request.args['Perpage'].split()[-1])
#     page = request.args.get('page', pagenum, type=int)
#     products = None
#     if (sortingcriteria == "Name"):
#         if (current_user.is_authenticated and current_user.admin):
#             products = Product.query.order_by(Product.name)
#             products = products.paginate(page=page, per_page=recordNo)
#         else:
#             products = Product.query.filter_by(active=True).order_by(Product.name)
#             products = products.paginate(page=page, per_page=recordNo)
#         return render_template('products.html', title='All Products by Name', products=products, form=form, sortingcriteria=sortingcriteria, perpage=recordNo)
#     elif (sortingcriteria == "Stock"):
#         if (current_user.is_authenticated and current_user.admin):
#             products = Product.query.order_by(Product.totalStock)
#             products = products.paginate(page=page, per_page=recordNo)
#         else:
#             products = Product.query.filter_by(active=True).order_by(Product.totalStock)
#             products = products.paginate(page=page, per_page=recordNo)
#         return render_template('products.html', title='All Products by Stock', products=products, form=form, sortingcriteria=sortingcriteria, perpage=recordNo)
#     elif (sortingcriteria == "Lowest Price"):
#         if (current_user.is_authenticated and current_user.admin):
#             products = Product.query.order_by(Product.basePrice)
#             products = products.paginate(page=page, per_page=recordNo)
#         else:
#             products = Product.query.filter_by(active=True).order_by(Product.basePrice)
#             products = products.paginate(page=page, per_page=recordNo)
#         return render_template('products.html', title='All Products by Price Ascending', products=products, form=form, sortingcriteria=sortingcriteria, perpage=recordNo)
#     elif (sortingcriteria == "Highest Price"):
#         if (current_user.is_authenticated and current_user.admin):
#             products = Product.query.order_by(Product.basePrice.desc())
#             products = products.paginate(page=page, per_page=recordNo)
#         else:
#             products = Product.query.filter_by(active=True).order_by(Product.basePrice.desc())
#             products = products.paginate(page=page, per_page=recordNo)
#         return render_template('products.html', title='All Products by Price Descending', products=products, form=form, sortingcriteria=sortingcriteria, perpage=recordNo)
#     else:
#         if (current_user.is_authenticated and current_user.admin):
#             products = Product.query.paginate(page=page, per_page=recordNo)
#         else:
#             products = Product.query.filter_by(active=True).paginate(page=page, per_page=recordNo)
#         return render_template('products.html', title='All Products', products=products, form=form, sortingcriteria=sortingcriteria, perpage=recordNo)

# @app.route("/product/<int:id>", methods=['GET', 'POST'])
# def product(id):
#     addcartform = AddCartForm()
#     if addcartform.submit.data and addcartform.validate():
#         addtocart(addcartform)
#
#     product = Product.query.get_or_404(id)
#     form = None
#     if current_user.is_authenticated:
#         form = UnpublishProductForm() if product.active else PublishProductForm()
#         if (form.publishbutton.data and form.validate()):
#             product.active = not product.active
#             # update the form
#             form = UnpublishProductForm() if product.active else PublishProductForm()
#             db.session.commit()
#     return render_template('product.html', title=product.name, product=product, form=form, addcartform=addcartform)

SUPPORTED_IMG_TYPES = {"png", "bmp", "svg"}

def get_file_ext(filename):
    return filename.rsplit('.', 1)[1].lower() if '.' in filename else '';

def image_ext_error():
    flash("Invalid image file format! Supported file types: " + str(SUPPORTED_IMG_TYPES).strip()[1:-1], category='bad')

# @app.route('/media/<filename>')
# def media_upload(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# @app.route("/product/<int:id>/edit", methods=['GET', 'POST'])
# def edit_product(id):
#     if (not current_user.is_authenticated or not current_user.admin):
#         # Trigger a 403 forbidden error
#         abort(403)
#     product = Product.query.get_or_404(id)
#     form = EditProductForm(name=product.name, description=product.desc, price=product.basePrice)
#     if (request.method == 'POST'):
#         filename = product.coverImage
#         if (('image' in request.files and request.files['image'] != None)):
#             file = request.files['image']
#             if (get_file_ext(file.filename) not in SUPPORTED_IMG_TYPES):
#                 image_ext_error()
#             else:
#                 filename = secure_filename(file.filename)
#                 oldpath = os.path.join(APP_PATH, app.config['UPLOAD_FOLDER'] + "/" + product.coverImage)
#                 newpath = os.path.join(APP_PATH, app.config['UPLOAD_FOLDER'] + "/" + filename)
#                 if (product.coverImage != "default.bmp" and os.path.exists(oldpath)):
#                     # Delete the original image file
#                     os.remove(oldpath)
#                 # Save the image file
#                 file.save(newpath)
#         if (form.validate_on_submit()):
#             # Save the changes to the database
#             product.name = form.name.data
#             product.desc = form.description.data
#             product.basePrice = form.price.data
#             product.coverImage = filename
#             db.session.commit()
#             return redirect(url_for('product', id=product.id))
#         else:
#             flash("One or more input fields are not valid.", category='bad')
#     return render_template('edit_product.html', title="Editing '" + product.name + "'", product=product, form=form)

# @app.route("/product/create", methods=['GET', 'POST'])
# def create_product():
#     if (not current_user.is_authenticated or not current_user.admin):
#         # Trigger a 403 forbidden error
#         abort(403)
#     form = EditProductForm()
#     product = Product(active=False, name="", desc="", coverImage="default.png", basePrice=0.0, totalStock=0)
#     if (request.method == 'POST'):
#         if ('image' not in request.files or request.files['image'] == None or request.files['image'] == ''):
#             flash("A product image file must be specified.", category='bad')
#         else:
#             file = request.files['image']
#             if (file != None and get_file_ext(file.filename) not in SUPPORTED_IMG_TYPES):
#                 image_ext_error()
#             elif (form.validate_on_submit()):
#                 filename = secure_filename(file.filename)
#                 # Upload the image file
#                 file.save(os.path.join(APP_PATH, app.config['UPLOAD_FOLDER'] + "/" + filename))
#                 # Save the changes to the database
#                 product.name = form.name.data
#                 product.desc = form.description.data
#                 product.basePrice = form.price.data
#                 product.coverImage = filename
#                 product.active = False
#                 db.session.add(product)
#                 db.session.commit()
#                 return redirect(url_for('product', id=product.id))
#             else:
#                 flash("One or more input fields are not valid.", category='bad')
#     return render_template('edit_product.html', title="Create Product Entry", product=product, form=form)

# @app.route("/product/<int:id>/delete", methods=['GET', 'POST'])
# def delete_product(id):
#     if (not current_user.is_authenticated or not current_user.admin):
#         # Trigger a 403 forbidden error
#         abort(403)
#     product = Product.query.get_or_404(id)
#     form = DeleteProductForm()
#     if (form.validate_on_submit()):
#         if (form.submit.data):
#             Product.query.filter_by(id=product.id).delete()
#             db.session.commit()
#             return redirect(url_for('products'))
#         return redirect(url_for('product', id=product.id))
#     return render_template('delete_product.html', title="Delete Product", product=product, form=form)

# @app.route('/review_checkout', methods=['GET', 'POST'])
# def review_checkout():
#     form = ReviewForm()
#     products = list()
#     quantitys = list()
#     total = 0
#     if ('Shoppingcart' not in session):
#         session['Shoppingcart'] = dict()
#     for id in session['Shoppingcart']:
#         product = Product.query.get(id)
#         if product != None:
#             products.append(product)
#             quantitys.append(session['Shoppingcart'][id])
#             total += float(session['Shoppingcart'][id]) * float(product.basePrice)
#     if (form.validate_on_submit()):
#         for order_dict in session['Orders']['List']:
#             order = Order(userid=int(order_dict["userid"]), transactionid=int(int(order_dict["transactionid"])), productid=int(int(order_dict["productid"])), quantity=int(int(order_dict["quantity"])))
#             db.session.add(order)
#         session['Orders'] = dict()
#         session['Shoppingcart'] = dict()
#         current_user.transactionid += 1
#         db.session.commit()
#         return redirect(url_for('confirm'))
#
#     return render_template('review_checkout.html', form=form, products=products, quantitys=quantitys, total=total)

# @app.route('/removefromcart/<int:id>')
# def removefromcart(id):
#     session['Shoppingcart'].pop(str(id), None)
#     flash("Removed product from basket.", category='good')
#     return redirect(url_for('basket'))
