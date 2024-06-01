# app/main.py

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from . import crud, models, schemas
from .database import SessionLocal, engine

# Create the database tables
models.Base.metadata.create_all(bind=engine)

# Initialize the FastAPI app
app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/shopping_lists/", response_model=schemas.ShoppingList)
def create_shopping_list_for_user(
    user_id: int, shopping_list: schemas.ShoppingListCreate, db: Session = Depends(get_db)):
    return crud.create_user_shopping_list(db=db, item=item, user_id=user_id)

# Create a new item
@app.post("/items/", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item)

# Read a list of items
@app.get("/items/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items

# Read a specific item by ID
@app.get("/items/{item_id}", response_model=schemas.Item)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

# Update an item by ID
@app.put("/items/{item_id}", response_model=schemas.Item)
def update_item(item_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)):
    db_item = crud.update_item(db, item_id=item_id, item=item)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

# Delete an item by ID
@app.delete("/items/{item_id}", response_model=schemas.Item)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.delete_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

# Create a new shopping list
@app.post("/shopping_lists/", response_model=schemas.ShoppingList)
def create_shopping_list(shopping_list: schemas.ShoppingListCreate, db: Session = Depends(get_db)):
    return crud.create_shopping_list(db=db, shopping_list=shopping_list)

# Read all shopping lists
@app.get("/shopping_lists/", response_model=List[schemas.ShoppingList])
def read_shopping_lists(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    shopping_lists = crud.get_shopping_lists(db, skip=skip, limit=limit)
    return shopping_lists

# Read a specific shopping list by ID
@app.get("/shopping_lists/{shopping_list_id}", response_model=schemas.ShoppingList)
def read_shopping_list(shopping_list_id: int, db: Session = Depends(get_db)):
    db_shopping_list = crud.get_shopping_list(db, shopping_list_id=shopping_list_id)
    if db_shopping_list is None:
        raise HTTPException(status_code=404, detail="Shopping List not found")
    return db_shopping_list

# Create a new recipe
@app.post("/recipes/", response_model=schemas.Recipe)
def create_recipe(recipe: schemas.RecipeCreate, db: Session = Depends(get_db)):
    return crud.create_recipe(db=db, recipe=recipe)

# Read all recipes
@app.get("/recipes/", response_model=List[schemas.Recipe])
def read_recipes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    recipes = crud.get_recipes(db, skip=skip, limit=limit)
    return recipes

# Read a specific recipe by ID
@app.get("/recipes/{recipe_id}", response_model=schemas.Recipe)
def read_recipe(recipe_id: int, db: Session = Depends(get_db)):
    db_recipe = crud.get_recipe(db, recipe_id=recipe_id)
    if db_recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return db_recipe

# Create a new meal plan
@app.post("/meal_plans/", response_model=schemas.MealPlan)
def create_meal_plan(meal_plan: schemas.MealPlanCreate, db: Session = Depends(get_db)):
    return crud.create_meal_plan(db=db, meal_plan=meal_plan)

# Read all meal plans
@app.get("/meal_plans/", response_model=List[schemas.MealPlan])
def read_meal_plans(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    meal_plans = crud.get_meal_plans(db, skip=skip, limit=limit)
    return meal_plans

# Read a specific meal plan by ID
@app.get("/meal_plans/{meal_plan_id}", response_model=schemas.MealPlan)
def read_meal_plan(meal_plan_id: int, db: Session = Depends(get_db)):
    db_meal_plan = crud.get_meal_plan(db, meal_plan_id=meal_plan_id)
    if db_meal_plan is None:
        raise HTTPException(status_code=404, detail="Meal Plan not found")
    return db_meal_plan
