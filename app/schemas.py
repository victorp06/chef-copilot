# app/schemas.py

from pydantic import BaseModel
from typing import List, Optional
from datetime import date, datetime

# Schema for Item
class ItemBase(BaseModel):
    name: str
    quantity: int
    expiration_date: Optional[date] = None

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True

# Schema for Shopping List
class ShoppingListBase(BaseModel):
    items: List[Item]

class ShoppingListCreate(ShoppingListBase):
    pass

class ShoppingList(ShoppingListBase):
    id: int

    class Config:
        orm_mode = True

# Schema for Recipe
class RecipeBase(BaseModel):
    name: str
    ingredients: List[Item]
    steps: str

class RecipeCreate(RecipeBase):
    pass

class Recipe(RecipeBase):
    id: int

    class Config:
        orm_mode = True

# Schema for Meal Plan
class MealPlanBase(BaseModel):
    date: date
    recipes: List[Recipe]

class MealPlanCreate(MealPlanBase):
    pass

class MealPlan(MealPlanBase):
    id: int

    class Config:
        orm_mode = True

# Schema for user
class UserBase(BaseModel):
    email: str
    name: str
    last_name: str
    birthday: date
    

class UserCreate(UserBase):
    hashed_password: str
    joined: datetime = datetime.utcnow()

class User(UserBase):
    id: int
    is_active: bool = True
    shopping_lists: List[ShoppingList] = []

    class Config:
        orm_mode = True