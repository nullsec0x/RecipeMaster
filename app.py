from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    recipes = db.relationship('Recipe', backref='author', lazy=True)

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(100))
    image = db.Column(db.String(200))
    category = db.Column(db.String(50))
    area = db.Column(db.String(50))
    instructions = db.Column(db.Text)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
@login_required  
def home():
    response = requests.get('https://www.themealdb.com/api/json/v1/1/random.php')
    meal = response.json()['meals'][0] if response.json()['meals'] else None
    
    if meal:
        ingredients = []
        for i in range(1, 21):
            ingredient = meal.get(f'strIngredient{i}')
            measure = meal.get(f'strMeasure{i}')
            if ingredient and ingredient.strip():
                ingredients.append(f"{measure} {ingredient}" if measure else ingredient)
        
        recipe = {
            'name': meal['strMeal'],
            'image': meal['strMealThumb'],
            'category': meal['strCategory'],
            'area': meal['strArea'],
            'ingredients': ingredients,
            'instructions': meal['strInstructions']
        }
    else:
        recipe = None
    
    return render_template('recipes/home.html', recipe=recipe)

@app.route('/save_recipe', methods=['POST'])
@login_required  
def save_recipe():
    recipe_data = request.form
    new_recipe = Recipe(
        user_id=current_user.id,
        name=recipe_data['name'],
        image=recipe_data['image'],
        category=recipe_data['category'],
        area=recipe_data['area'],
        instructions=recipe_data['instructions']
    )
    db.session.add(new_recipe)
    db.session.commit()
    flash('Recipe saved!', 'success')
    return redirect(url_for('home'))

@app.route('/favorites')
@login_required  
def favorites():
    recipes = Recipe.query.filter_by(user_id=current_user.id).all()
    return render_template('recipes/favorites.html', recipes=recipes)

@app.route('/recipe/<int:id>')
@login_required
def view_recipe(id):
    recipe = Recipe.query.filter_by(id=id, user_id=current_user.id).first_or_404()
    return render_template('recipes/view.html', recipe=recipe)

@app.route('/delete/<int:id>', methods=['POST'])
@login_required  
def delete(id):
    Recipe.query.filter_by(id=id, user_id=current_user.id).delete()
    db.session.commit()
    flash('Recipe deleted', 'success')
    return redirect(url_for('favorites'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and user.password == request.form['password']:
            login_user(user)
            return redirect(url_for('home'))
        flash('Invalid credentials', 'danger')
    return render_template('auth/login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    if request.method == 'POST':
        if User.query.filter_by(username=request.form['username']).first():
            flash('Username already taken', 'danger')
        else:
            user = User(username=request.form['username'], password=request.form['password'])
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect(url_for('home'))
    return render_template('auth/register.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)