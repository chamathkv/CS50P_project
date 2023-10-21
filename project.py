'''
╦═╗┌─┐┌─┐┌┬┐┌─┐┬ ┬┬─┐┌─┐┌┐┌┌┬┐  ┬─┐┌─┐┬  ┬┬┌─┐┬ ┬  ┌─┐┬ ┬┌─┐┌┬┐┌─┐┌┬┐
╠╦╝├┤ └─┐ │ ├─┤│ │├┬┘├─┤│││ │   ├┬┘├┤ └┐┌┘│├┤ │││  └─┐└┬┘└─┐ │ ├┤ │││
╩╚═└─┘└─┘ ┴ ┴ ┴└─┘┴└─┴ ┴┘└┘ ┴   ┴└─└─┘ └┘ ┴└─┘└┴┘  └─┘ ┴ └─┘ ┴ └─┘┴ ┴
By Chamath Kalanaka Vithanawasam
from Colombo, Sri Lanka
v1.0
'''

from tabulate import tabulate
import os
import sys
import re
import csv
from collections import Counter
import math
import pandas as pd
from fpdf import FPDF
import datetime
import warnings

#Used to filter out Deprecation and User Warnings that come up when using FPDF
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=UserWarning)

#Prepare a dict for the restaurant review entry.
review_dict = {
    "Name": "",
    "Rating": "",
    "Description 1": "",
    "Description 2": "",
    "Description 3": ""
}

#A CSV file to store the restaurant reviews in.
review_csv_filename = "reviews.csv"

#Function to check if the CSV file exists.
def csv_file_exists():
    return os.path.isfile(review_csv_filename)

def main():
    main_menu()

#Main menu from which the user can navigate to all the services provided
def main_menu():
    os.system('clear')
    main_menu_table = [["1","Enter new review"],["2","View overall restaurant review"],["3","View top 3 restaurants"],["4","View worst 3 restaurants"],["5","Exit"]]
    main_menu_headers = ["Shortcut", "Description"]
    print("="*47, "\n", "WELCOME TO THE RESTAURANT REVIEW APPLICATION")
    print("="*47)
    print(tabulate(main_menu_table, main_menu_headers, tablefmt="grid"))

    main_menu_choice = input("Enter desired menu option: ")

    if main_menu_choice == "1":
        new_review_menu()
    elif main_menu_choice == "2":
        overall_review_menu()
    elif main_menu_choice == "3":
        top_three_menu()
    elif main_menu_choice == "4":
        worst_three_menu()
    elif main_menu_choice == "5":
        os.system('clear')
        sys.exit()
    else:
        os.system('clear')
        print("Invalid choice. Exiting.")

#Menu to enter a new restaurant, a rating, and three descriptions about it
def new_review_menu():
    os.system('clear')
    print("="*46, "\n", " "*16, "NEW REVIEW")
    print("="*46)

    restaurant_name = input("Enter the name of the restaurant you want to review (max 20 characters): ")
    restaurant_name_verifier(restaurant_name)
    restaurant_rating = input("Please rate the product on a scale from 1 to 5, using up to one decimal place if needed: ")
    restaurant_rating_verifier(restaurant_rating)
    restaurant_description = input("Enter three word combinations to describe your experience, "
                                   "with each word followed by a comma.\n"
                                   "Use an underscore (_) if you want to use a combination of words.\n"
                                   "Example: Delicious,Pleasant,Good_Location\n"
                                   "(max 20 characters per word combination): ")
    restaurant_description_word = restaurant_description_verifier(restaurant_description)

    review_dict["Name"] = restaurant_name
    review_dict["Rating"] = restaurant_rating
    review_dict["Description 1"] = restaurant_description_word[0]
    review_dict["Description 2"] = restaurant_description_word[1]
    review_dict["Description 3"] = restaurant_description_word[2]

    if csv_file_exists():
        # Append the data to the existing CSV file
        with open(review_csv_filename, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=review_dict.keys())
            writer.writerow(review_dict)

    else:
        with open(review_csv_filename, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=review_dict.keys())
            writer.writeheader()  # Write the header row
            writer.writerow(review_dict)  # Write the data row

    print("Your review has been stored. Thank you!")

#A simple check to identify whether the restaurant name exceeds 20 characters
def restaurant_name_verifier(restaurant_name):
    if len(restaurant_name) > 20:
        sys.exit("Too many characters. Exiting")
    elif len(restaurant_name) == 0:
        sys.exit("Not enough characters. Exiting")
    else:
        return 0

#A simple check to identify whether the ratings exceeds 5 or is less than 0
def restaurant_rating_verifier(restaurant_rating):

    if int(restaurant_rating) > 5:
        sys.exit("Rating exceeds 5. Exiting")
    elif int(restaurant_rating) < 0:
        sys.exit("Rating is less than 0. Exiting")
    else:
        return 0

#A simple check to identify whether the each restaurant description exceeds 20 characters or is empty (0 characters)
def restaurant_description_verifier(restaurant_description):
    pattern = r'^([\w_]{1,20}),([\w_]{1,20}),([\w_]{1,20})$'

    match = re.match(pattern, restaurant_description)

    if match:
        word1, word2, word3 = match.groups()
        return word1, word2, word3
    else:
        sys.exit("Invalid format. Exiting.")

#This menu will be used to get the average review for a selected restaurant based on the stored data
def overall_review_menu():
    #Initialize an empty list to store descriptions
    descriptions = []
    #To store the sum of all the ratings
    ratings_sum = 0
    #To count the number of reviews
    review_count = 0
    #A flag to check if the restaurant was found
    restaurant_found = False
    #A list to keep the descriptions in
    description_list = []
    overall_restaurants_heading = "VIEW OVERALL RESTAURANT REVIEW"

    os.system('clear')

    print("="*46, "\n", " "*int(len(overall_restaurants_heading)/4), overall_restaurants_heading)
    print("="*46)
    overall_review_restaurant_name = input("Enter the name of the restaurant you want the overall review of: ")

    #Get all the descriptions for a particular restaurant into one list and get the sum of the ratings
    with open(review_csv_filename, mode="r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Name"] == overall_review_restaurant_name:
                for i in range(1, 4):
                    description_list = row[f"Description {i}"]
                    descriptions.append(description_list)
                ratings_sum += int(row["Rating"])
                review_count += 1
                restaurant_found = True #set to true if the restaurant is found
        descriptions.append(description_list) #descriptions will now have a list of all the words used to describe the restaurant

    if not restaurant_found:
        raise ValueError("Restaurant not found")

    rounded_up_avg_rating, stars = star_rater(ratings_sum, review_count)

    print(f"\nRestaurant name: {overall_review_restaurant_name}\n")
    print(f"Average rating: {rounded_up_avg_rating}\n")
    print(f"Star rating:\n")

    print(stars)

    word_counts = Counter(descriptions) # Count the occurrences of each word
    most_common_words = word_counts.most_common(3) # Get the three most common words

    print(f"\nNumber of reviews entered: {review_count}\n")
    print(f"This restaurant has been frequently described as:")
    # Print the results
    for word, count in most_common_words:
        print(f"◈ {word} (mentioned {count} times)")

#Used to return the star rating in the form of emojis
def star_rater(ratings_sum, review_count):
    rounded_up_avg_rating = round(ratings_sum/review_count)
    stars_earned = "⭐ "*rounded_up_avg_rating
    unearned_stars = "☆ "*(5-rounded_up_avg_rating)
    stars = stars_earned + unearned_stars
    return rounded_up_avg_rating, stars

#Menu used to check on the top three highest rated restaurants
def top_three_menu():
    os.system('clear')
    top_3_restaurants_heading = "VIEW TOP 3 RESTAURANTS"
    print("="*46, "\n", " "*int(len(top_3_restaurants_heading)/2), top_3_restaurants_heading)
    print("="*46)

    #Call on data_processing() funtion to use Pandas library to get the top rated restaurants and their average ratings
    #Function will return the time the data was processed and the top 3 restaurants, which can be used if the user wants to get a PDF of the results
    request_time_date, top_3_ratings = data_processing(True)

    pdf_option = input("Would you like to get a PDF of this data? (y/n):")

    if pdf_option == "y":
        pdf_print(top_3_restaurants_heading, request_time_date, top_3_ratings, "top")
    elif pdf_option == "n":
        os.system('clear')
        sys.exit("Thank you for using this service. Exiting.")
    else:
        sys.exit("Invalid input.")

#Menu used to check on the top three worst rated restaurants
def worst_three_menu():
    os.system('clear')
    worst_3_restaurants_heading = "VIEW WORST 3 RESTAURANTS"
    print("="*46, "\n", " "*int(len(worst_3_restaurants_heading)/2), worst_3_restaurants_heading)
    print("="*46)

    #Call on data_processing() funtion to use Pandas library to get the worst rated restaurants and their average ratings
    #Function will return the time the data was processed and the top 3 restaurants, which can be used if the user wants to get a PDF of the results
    request_time_date, worst_3_ratings = data_processing(False)

    pdf_option = input("Would you like to get a PDF of this data? (y/n):")

    if pdf_option == "y":
        pdf_print(worst_3_restaurants_heading, request_time_date, worst_3_ratings, "worst")
    elif pdf_option == "n":
        os.system('clear')
        sys.exit("Thank you for using this service. Exiting.")
    else:
        sys.exit("Invalid input.")

#Used to give a PDF of the results
def pdf_print(heading, request_time_date, top_or_worst_3_ratings, top_or_worst):

    pdf = FPDF()

    pdf.add_page()
    pdf.set_font('Times', "", 12)
    pdf.cell(0, 10, heading, 0, 1, "C")

    pdf.set_font('Times', "", 10)
    pdf.cell(0, 10, ("="*96), 0, 1)
    pdf.cell(0, 10, "Name" + (" "*10) + "Rating" + (" "*10) + "Stars" + (" "*10), 0, 1)
    pdf.cell(0, 10, ("="*96), 0, 1)

    for name, rating in top_or_worst_3_ratings:
        formatted_name = name.ljust(20)
        formatted_rating = f"{rating:.0f}".ljust(10)
        #formatted_stars = star_rater(rating, 1)[1]
        pdf.cell(0, 10, formatted_name + " " + formatted_rating + " " + (int(formatted_rating)*"*"), 0, 1)
        #print(f"{formatted_name}{formatted_rating}{formatted_stars}")

    #PDF will display the time the data was fetched from the CSV, and the time the data was printed on the PDF
    pdf.set_y(-40)
    pdf.set_font('Arial', "I", 9)
    pdf.cell(0, 10, "Time and date this information was requested: " + str(request_time_date.hour) + ":" + str(request_time_date.minute) + " on " + str(request_time_date.day) + " " + str(request_time_date.strftime('%B')) + ", " + str(request_time_date.year), 0, 1, "R")
    current_time = datetime.datetime.now()
    pdf.cell(0, 10, "Time and date this information was printed:" + str(current_time.hour) + ":" + str(current_time.minute) + " on " + str(current_time.day) + " " + str(current_time.strftime('%B')) + ", " + str(current_time.year), 0, 1, "R")

    #PDF's document title will highlight the time the data was fetched from the CSV file
    if top_or_worst == "top":
        pdf.output("top3restaurants" + "_" + str(request_time_date.year) + "_" +  str(request_time_date.month) + "_" +  str(request_time_date.day) + "_" +  str(request_time_date.hour) + "_" +  str(request_time_date.minute) + ".pdf", dest = "F")
    elif top_or_worst == "worst":
        pdf.output("worst3restaurants" + "_" +  str(request_time_date.year) + "_" +  str(request_time_date.month) + "_" +  str(request_time_date.day) + "_" +  str(request_time_date.hour) + "_" +  str(request_time_date.minute) + ".pdf", dest = "F")

    print("PDF successfully saved to this folder. Exiting.")

#Used to process the data from the CSV file and to get the top or worst rated restaurants, depending on what value the ascending_decending_order parameter holds
def data_processing(ascending_decending_order):

    print()
    current_time = date_time_display()

    full_dataset = pd.read_csv(review_csv_filename)

    unique_restaurant_avg_rating = full_dataset.groupby("Name")["Rating"].mean() #to get the average rating for each unique restaurant
    #print(f"CCC: {unique_restaurant_avg_rating}")
    #print(type(unique_restaurant_names))

    sorted_ratings = sorted(unique_restaurant_avg_rating.items(), key=lambda x: x[1], reverse=ascending_decending_order) #sort the average ratings in decending order
    top_or_worst_3_ratings = sorted_ratings[:3] #get the top 3 ratings into one list
    #print(top_3_ratings)
    print("\nName                Rating    Stars")
    print("="*46)
    for name, rating in top_or_worst_3_ratings:
        formatted_name = name.ljust(20)
        formatted_rating = f"{rating:.0f}".ljust(10)
        formatted_stars = star_rater(rating, 1)[1]
        print(f"{formatted_name}{formatted_rating}{formatted_stars}")

    print("")

    return current_time, top_or_worst_3_ratings

#Used to fetch the current date and time readings
def date_time_display():
    current_time = datetime.datetime.now()
    print(f"Time and date this information was requested: {current_time.hour}:{current_time.minute} on {current_time.day} {current_time.strftime('%B')}, {current_time.year}")
    return current_time

if __name__ == "__main__":
    main()
