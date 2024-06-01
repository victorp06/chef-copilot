# app/crud.py

from sqlalchemy.orm import Session
from . import models, schemas

# CRUD for users
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.hashed_password + "notreallyhashed"
    db_user = models.User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_item = db.query(models.User).filter(models.User.id == user_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item

def create_user_shopping_list(db: Session, shopping_list: schemas.ShoppingListCreate, user_id: int):
    db_shopping_list = models.ShoppingList(**shopping_list.model_dump(), user_id=user_id)
    db.add(db_shopping_list)
    db.commit()
    db.refresh(db_shopping_list)
    return db_shopping_list

# CRUD operations for Item
def get_items(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Item).offset(skip).limit(limit).all()

def get_item(db: Session, item_id: int):
    return db.query(models.Item).filter(models.Item.id == item_id).first()

def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_item(db: Session, item_id: int, item: schemas.ItemCreate):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item:
        db_item.name = item.name
        db_item.quantity = item.quantity
        db_item.expiration_date = item.expiration_date
        db.commit()
        db.refresh(db_item)
    return db_item

def delete_item(db: Session, item_id: int):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item

# CRUD operations for ShoppingList
def get_shopping_lists(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.ShoppingList).offset(skip).limit(limit).all()

def get_shopping_list(db: Session, shopping_list_id: int):
    return db.query(models.ShoppingList).filter(models.ShoppingList.id == shopping_list_id).first()

def create_shopping_list(db: Session, shopping_list: schemas.ShoppingListCreate, user_id: int):
    db_shopping_list = models.ShoppingList(items=shopping_list.items)
    db.add(db_shopping_list)
    db.commit()
    db.refresh(db_shopping_list)
    return db_shopping_list

# CRUD operations for Recipe
def get_recipes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Recipe).offset(skip).limit(limit).all()

def get_recipe(db: Session, recipe_id: int):
    return db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()

def create_recipe(db: Session, recipe: schemas.RecipeCreate):
    db_recipe = models.Recipe(name=recipe.name, ingredients=recipe.ingredients)
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe

# CRUD operations for MealPlan
def get_meal_plans(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.MealPlan).offset(skip).limit(limit).all()

def get_meal_plan(db: Session, meal_plan_id: int):
    return db.query(models.MealPlan).filter(models.MealPlan.id == meal_plan_id).first()

def create_meal_plan(db: Session, meal_plan: schemas.MealPlanCreate):
    db_meal_plan = models.MealPlan(date=meal_plan.date, recipes=meal_plan.recipes)
    db.add(db_meal_plan)
    db.commit()
    db.refresh(db_meal_plan)
    return db_meal_plan
