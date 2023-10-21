# RESTAURANT REVIEW SYSTEM
## Video Demo: https://youtu.be/X4dwL1BA6bQ
## Description
### Introduction
The following 'Restaurant Review System' project has been made for the CS50P final project submission. The general requirement that it fulfils is that of allowing members of the public to get an overall idea of the quality of a restaurant that they intend to visit by inspecting reviews placed about the restaurant by other users. The people who access the system are able to enter their own personal opinions about a restaurant as well.

The input collected from a single user when they wish to enter information include the name of the restaurant, the rating that they want to give it (which can range from 0 to 5, 0 being the worst rating and 5 being the best rating), and three descriptions about the restaurant where each description does not exceed 20 characters. These points will be described in more detail below.

If the user decides to search for a specific restaurant's overall rating, they may do so, and will also be able to see the most commonly used descriptions to explain the restaurant experience.

The users can also view the top three highest-rated restaurants based on the data that has been added and also view the worst three restaurants as well. Over here, the user is able to choose whether to save their findings on a PDF document.

#### Main Menu
Users will be greeted with the following main menu.

```
===============================================
 WELCOME TO THE RESTAURANT REVIEW APPLICATION
===============================================
+------------+--------------------------------+
|   Shortcut | Description                    |
+============+================================+
|          1 | Enter new review               |
+------------+--------------------------------+
|          2 | View overall restaurant review |
+------------+--------------------------------+
|          3 | View top 3 restaurants         |
+------------+--------------------------------+
|          4 | View worst 3 restaurants       |
+------------+--------------------------------+
|          5 | Exit                           |
+------------+--------------------------------+
Enter desired menu option:
```

The 'Shortcut' column indicates the shortcut that needs to be entered to travel to a separate menu, and the 'Description' column explain what each shortcut navigates into. Each description is explained in more detail below.

#### 'Enter new review' (Shortcut key: 1)
This menu will allow the user to enter a new review for a restaurant. There are three inputs that the user needs to enter.

1) Name of the restaurant

This input is limited to 20 characters.

2) Rating

This input has to be in the range 0-5

3) Three descriptions

This is where the user can enter three descriptions about the restaurant. These three will need to be separated by a comma (,). The user cannot enter spaces in the descriptions. If they want to enter a combination of words, they can use an underscore (_) instead of a space ( ). For example, use "Friendly_Staff" instead of "Friendly Staff". An example of a successful entry is given below:
```
Excellent,Impeccable,Friendly_Staff
```

Once this data has been entered, it will be stored in a CSV file named review_db.csv. If such a file is not available, it will be created.

#### 'View overall restaurant review' (Shortcut key: 2)
This section will allow the user to view the overall restaurant review for a selected restaurant. The user will first be prompted to enter the name of the restaurant. Once this data is entered, the user can view the average rating of the restaurant, the number of reviews that have been entered for that particular restaurant, and the three most frequently used descriptions for that particular restaurant. The output will also show how often these descriptions have been used.

The output will display a 'star' rating for the restaurant based on the average rating it has received. This is displayed as emoji stars. For example, if a restaurant has an average rating of 4, it should get a star rating of four stars, which will be displayed as follows:

```
⭐ ⭐ ⭐ ⭐ ☆
```

#### 'View top 3 restaurants' (Shortcut key: 3)
Choosing this option will display the three highest-rated restaurants. It will also display the time the data was fetched from the database. The time was added to show exactly when the data was collected from a db. Fetching this data uses the Pandas library.

After this data is fetched, the user has the choice to either get a PDF of the information or to exit the system. If they choose to get a PDF, a PDF will be generated giving the same data. It will also show the time the PDF was generated and the time the data was fetched from the DB. This feature was added so that the user knows how long of a time difference there was between fetching the data and actually getting a PDF of it.

#### 'View worst 3 restaurants' (Shortcut key: 4)
Choosing this option will display the three worst-rated restaurants. The format and the PDF option are similar to viewing the top 3 restaurants, which is explained in the section above.

#### 'Exit' (Shortcut key: 5)
This shortcut will simply exit the system.

### Libraries/Modules
The following libraries/modules were used for this system. The requirements.txt file provides the list of libraries that need to be installed.

#### In-built libraries
* os
* sys
* re
* csv
* math
* datetime

#### Libraries to install
* tabulate
```
pip install tabulate
```
* pandas
```
pip install pandas
```
* fpdf
```
pip install fpdf
```

## Functions in code
There is a total of 14 functions used in this code. They are explained below.

### csv_file_exists():
Simple code to check whether the CSV file that saves the reviews already exists or not. It returns a boolean expression based on the availability of the CSV file.

### main():
This is the main function.

### main_menu():
Main menu from which the user can navigate to all the services provided.

### new_review_menu():
Menu to enter a new restaurant, a rating, and three descriptions about it. Each entry that is input will be verified by a separate function.

### restaurant_name_verifier():
A simple check to identify whether the restaurant name exceeds 20 characters.

### restaurant_rating_verifier():
A simple check to identify whether the ratings exceeds 5 or is less than 0.

### restaurant_description_verifier():
A simple check to identify whether the each restaurant description exceeds 20 characters or is empty (0 characters).

### overall_review_menu():
This menu will be used to get the average review for a selected restaurant based on the stored data. The name of the restaurant, the number of reviews entered, the average rating, the star rating, and the most frequently used descriptions for the restaurant will be printed in the terminal via this function.

### star_rater():
Used to return the star rating in the form of emojis. This function takes in the sum of all the ratings and the number of ratings entered.

### top_three_menu():
Menu used to check on the top three highest rated restaurants. Will display the top three restaurants, their ratings, and their star ratings. It will also show the time the data was collected form the DB.

### worst_three_menu():
Menu used to check on the worst rated restaurants. Will display the worst three restaurants, their ratings, and their star ratings. It will also show the time the data was collected form the DB.

### pdf_print():
Used to give a PDF of the results. The PDF will highlight the time the data was collected from the DB and the time the data was added to the PDF.

### data_processing():
Used to process the data from the DB and to get the top or worst rated restaurants, depending on what value the ascending_decending_order parameter holds

### def date_time_display():
Used to fetch the current date and time readings.

## Test cases
Most of the functions were tested using PyTest. PyTest can be installed by entering the following command in the terminal:
```
pip install pytest
```

The test cases used are explained below.

### main():
This is the main function that is used to run the test cases.

### test_star_rater():
Used to test all the possibilities for the star_rater() function.

### test_restaurant_name_verifier():
Used to check whether the restaurant_name_verifier() function works properly.

### test_restaurant_rating_verifier():
Used to check whether the restaurant_rating_verifier() function works properly.

### test_restaurant_description_verifier():
Used to check whether the restaurant_description_verifier() function works properly.
