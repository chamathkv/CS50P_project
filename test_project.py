'''
Test cases for the Restaurant Review System
By Chamath Kalanaka Vithanawasam
v1.0
'''

import pytest
import subprocess
import os
import csv
import pandas as pd
from datetime import datetime
from io import StringIO
from project import (
    star_rater,
    restaurant_name_verifier,
    restaurant_rating_verifier,
    restaurant_description_verifier,
)

def main():
    test_star_rater()
    test_restaurant_name_verifier()
    test_restaurant_rating_verifier()
    test_restaurant_description_verifier()

def test_star_rater():
    assert star_rater(5,1) == (5, "⭐ ⭐ ⭐ ⭐ ⭐ ")
    assert star_rater(1,1) == (1, "⭐ ☆ ☆ ☆ ☆ ")
    assert star_rater(8,2) == (4, "⭐ ⭐ ⭐ ⭐ ☆ ")
    assert star_rater(12,4) == (3, "⭐ ⭐ ⭐ ☆ ☆ ")
    assert star_rater(16,8) == (2, "⭐ ⭐ ☆ ☆ ☆ ")
    assert star_rater(15,15) == (1, "⭐ ☆ ☆ ☆ ☆ ")

def test_restaurant_name_verifier():
    with pytest.raises(SystemExit) as excinfo:
        restaurant_name_verifier("TestingWithAVeryLongRestaurant")
    assert str(excinfo.value) == "Too many characters. Exiting"

    with pytest.raises(SystemExit) as excinfo:
        restaurant_name_verifier("")
    assert str(excinfo.value) == "Not enough characters. Exiting"

    assert restaurant_name_verifier("Normal_Restaurant") == 0

def test_restaurant_rating_verifier():
    with pytest.raises(SystemExit) as excinfo:
        restaurant_rating_verifier("6")
    assert str(excinfo.value) == "Rating exceeds 5. Exiting"

    with pytest.raises(SystemExit) as excinfo:
        restaurant_rating_verifier("-1")
    assert str(excinfo.value) == "Rating is less than 0. Exiting"

    assert restaurant_rating_verifier("4") == 0

def test_restaurant_description_verifier():
    with pytest.raises(SystemExit) as excinfo:
        restaurant_description_verifier("Excessively_Long_Description,Tasty,Delicious")
    assert str(excinfo.value) == "Invalid format. Exiting."

    with pytest.raises(SystemExit) as excinfo:
        restaurant_description_verifier("Crowded,Excessively_Long_Description,Delicious")
    assert str(excinfo.value) == "Invalid format. Exiting."

    with pytest.raises(SystemExit) as excinfo:
        restaurant_description_verifier("Friendly_Staff,Tasty,Excessively_Long_Description")
    assert str(excinfo.value) == "Invalid format. Exiting."

    with pytest.raises(SystemExit) as excinfo:
        restaurant_description_verifier("Friendly-Staff,Tasty,Delicious")
    assert str(excinfo.value) == "Invalid format. Exiting."

    assert restaurant_description_verifier("Good,Delicious,Friendly_Staff") == (
        "Good",
        "Delicious",
        "Friendly_Staff"
    )





