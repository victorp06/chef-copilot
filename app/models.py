# app/models.py

from sqlalchemy import Boolean, Column, Integer, String, Date, Table, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

recipe_ingredient = Table(
    'recipe_ingredient', Base.metadata,
    Column('recipe_id', Integer, ForeignKey('recipes.id')),
    Column('ingredient_id', Integer, ForeignKey('items.id'))
)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    last_name = Column(String)
    birthday = Column(Date)
    joined = Column(Date)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    shopping_lists = relationship("ShoppingList", secondary="user_shopping_list_association")


class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    quantity = Column(Integer, default=0)
    expiration_date = Column(Date, nullable=True)

class ShoppingList(Base):
    __tablename__ = 'shopping_lists'
    id = Column(Integer, primary_key=True, index=True)
    items = relationship("Item", secondary="shopping_list_item")

class Recipe(Base):
    __tablename__ = 'recipes'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    ingredients = relationship("Item", secondary=recipe_ingredient)

class MealPlan(Base):
    __tablename__ = 'meal_plans'
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    recipes = relationship("Recipe", secondary="meal_plan_recipe")
