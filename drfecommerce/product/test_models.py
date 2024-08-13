import pytest
from drfecommerce.product import models
pytestmark=pytest.mark.django_db

class TestCategoryModel:
    def test_str_method(self,category_factory):
        #arrange
        #Act
        obj=category_factory(name="test_cat")
        #Assert
        #(it returns true if test is passed )
        assert obj.__str__()=="test_cat"
        
    
class TestBrandModel:
   def test_str_method(self,brand_category):
       #arrange
        #Act
        obj=brand_category(name="brand_cat")
        #Assert
        #(it returns true if test is passed )
        assert obj.__str__()=="brand_cat"
        
    