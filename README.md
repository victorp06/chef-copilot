# Chef-copilot

Chef-copilot is a Python-based web application designed to assist users in managing their grocery shopping, tracking kitchen inventory, and planning meals. It helps users select products that fit their fitness goals considering calories, sugar, fats, and other nutritional information.

## Features

- Manage grocery shopping lists
- Track items in fridge and storage
- Get notifications when running low on critical items
- Select products based on fitness goals
- Propose daily or weekly meals based on kitchen inventory

## Installation

To get started with Chef-copilot, follow the instructions below to set up the project on your local machine.

### Prerequisites

- Python 3.8+
- pip
- PostgreSQL (or any preferred database)
- Git

### Clone the Repository

```
git clone https://github.com/yourusername/chef-copilot.git
cd chef-copilot```

### Create a Virtual Environment
```
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

### Install Dependencies
```
pip install -r requirements.txt```

### Set Up the Database
- Create a new database in PostgreSQL (or your preferred database).
- Update the database configuration in app/database.py:

```SQLALCHEMY_DATABASE_URL = "postgresql://username:password@localhost/dbname"```

### Create the database tables:
```alembic upgrade head```

### Running the Application

To run the application, execute the following command:

```./run.sh```
The application will be available at http://localhost:8000.

## API Endpoints

### User Management
- Create User: POST /users/
- Get Users: GET /users/
- Get User by ID: GET /users/{user_id}

### Shopping Lists
- Create Shopping List: POST /shopping-lists/
- Get Shopping Lists: GET /shopping-lists/

### Add Item to Shopping List: POST /shopping-lists/{shopping_list_id}/items
- Remove Item from Shopping List: DELETE /shopping-lists/{shopping_list_id}/items/{item_id}
- Items
- Create Item: POST /items/
- Get Items: GET /items/
- Update Item: PUT /items/{item_id}
- Delete Item: DELETE /items/{item_id}

### Recipes
- Create Recipe: POST /recipes/
- Get Recipes: GET /recipes/
- Add Ingredient to Recipe: POST /recipes/{recipe_id}/ingredients
- Remove Ingredient from Recipe: DELETE /recipes/{recipe_id}/ingredients/{item_id}

### Meal Plans
- Create Meal Plan: POST /meal-plans/
- Get Meal Plans: GET /meal-plans/
- Add Recipe to Meal Plan: POST /meal-plans/{meal_plan_id}/recipes
- Remove Recipe from Meal Plan: DELETE /meal-plans/{meal_plan_id}/recipes/{recipe_id}

##Project Structure

chef-copilot/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   ├── crud.py
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── shopping_list.py
│   │   ├── item.py
│   │   ├── recipe.py
│   │   ├── meal_plan.py
│   └── utils/
│       ├── __init__.py
│       ├── security.py
│       ├── notifications.py
│
├── alembic/
│   ├── env.py
│   ├── script.py.mako
│   └── versions/
│
├── requirements.txt
├── run.sh
├── README.md
└── .env

Happy coding! If you have any questions, feel free to open an issue or contact me via LinkedIn.
