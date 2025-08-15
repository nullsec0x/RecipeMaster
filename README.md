# RecipeMaster

This is a Flask-based web application that allows users to discover random recipes, save their favorite ones, and view details about them. The application integrates with an external API for recipe data and uses Flask-SQLAlchemy for user and recipe management.

## Table of Contents
- [Features](#features)
- [Screenshots](#screenshots)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Creator](#creator)

## Features

- **Random Recipe Generation**: Discover new recipes with a single click.
- **User Authentication**: Secure user registration and login system.
- **Save Favorite Recipes**: Users can save their preferred recipes to their personal collection.
- **View Saved Recipes**: Access a dedicated section to browse all saved recipes.
- **Detailed Recipe View**: View comprehensive details for each recipe, including ingredients and instructions.
- **Delete Saved Recipes**: Remove recipes from the favorites list.

## Screenshots

### Main Page

![Main Page](https://i.postimg.cc/t43dy2rc/Screenshot-20250815-025931.png)

### Liked Recipes

![Liked Recipes](https://i.postimg.cc/t4QdLLzP/Screenshot-20250815-025937.png)

### Details of Liked Recipes

![Details of Liked Recipes](https://i.postimg.cc/wTsc46Dg/Screenshot-20250815-025945.png)

## Installation

To set up and run this project locally, follow these steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/nullsec0x/RecipeMaster.git
   cd RecipeMaster
   ```

2. **Create a virtual environment** (recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:

   ```bash
   python app.py
   ```

   The application will run on `http://127.0.0.1:5000/`.

## Usage

1. **Register/Login**: Upon first access, you will be prompted to register a new account or log in if you already have one.
2. **Discover Recipes**: On the home page, click the "Get Random Recipe" button to fetch a new recipe.
3. **Save Recipes**: If you like a recipe, click the "Save" button to add it to your favorites.
4. **View Favorites**: Navigate to the "Favorites" section to see all your saved recipes.
5. **View Details**: Click on any saved recipe to view its full ingredients and instructions.
6. **Delete Recipes**: From the "Favorites" section, you can delete recipes you no longer wish to keep.

## Technologies Used

- **Flask**: Web framework for Python.
- **Flask-SQLAlchemy**: ORM for interacting with the SQLite database.
- **Flask-Login**: User session management.
- **requests**: HTTP library for making API calls to TheMealDB.
- **SQLite**: Lightweight, file-based database.

## Creator

This project was created by Nullsec0x.


