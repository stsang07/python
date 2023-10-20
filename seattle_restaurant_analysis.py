# Seattle Restaurants Analysis 
import matplotlib.pyplot as plt
import pandas as pd
import random 

# Define the path to Seattle Restaurant csv data set
dataset_path = "data_sources/Restaurants_Seattle.csv"

# Read the CSV file into a pandas DataFrame
seattle_restaurants_data = pd.read_csv(dataset_path)

# Check the data type of each column
print(seattle_restaurants_data.dtypes)

# Convert all cases to lowercase
print(seattle_restaurants_data.columns.tolist())

# Which neighborhood in Seattle has the highest density of restaurants? 
# Count the occurences of restaurants by Area and sort by DESC 

grouped_count = seattle_restaurants_data.groupby('Area')['Name'].count().sort_values(ascending=False)
top_10_neighborhoods = grouped_count.head(10)

# Loop to prompt user to enter input 3 times until it's valid
for attempts in range(3):
    user_desired_area = input("Enter where you want to eat: ")

    # Filter the DataFrame to the user's inputted area
    filtered_restaurants = seattle_restaurants_data[seattle_restaurants_data['Area'] == user_desired_area]

    if user_desired_area in seattle_restaurants_data['Area'].unique():
        random_restaurant = filtered_restaurants.sample()
        restaurant_name = random_restaurant['Name'].iloc[0]
        restaurant_category = random_restaurant['Category'].iloc[0]
        print("Suggested restaurant: " + restaurant_name + ", Category: " + restaurant_category)
        break 
    else:
        print("Attempt invalid after 3 tries.")
        print("There is no restaurant in " + user_desired_area + ". Please try another neighborhood")
        print("These are the available neighborhoods: ")
        print(seattle_restaurants_data['Area'].unique())


# Loop to prompt user to enter input until it's valid. Unlimited tries.
while True:
    user_desired_area = input("Enter where you want to eat: ").lower()

    # Filter the DataFrame to the user's inputted area
    filtered_restaurants = seattle_restaurants_data[seattle_restaurants_data['Area'] == user_desired_area]

    if user_desired_area in seattle_restaurants_data['Area'].unique():
        user_desired_rating = input("What star rating and above do you want? (Ex. 3.5) ")

        # Further filter the Area list to user's inputted star rating 
        filtered_restaurants = filtered_restaurants[filtered_restaurants['Star'] >= float(user_desired_rating)]

        if not filtered_restaurants.empty: # if filtered list is not empty, then return a random restaurant 
            random_restaurant = filtered_restaurants.sample()
            restaurant_name = random_restaurant['Name'].iloc[0]
            restaurant_rating = random_restaurant['Star'].iloc[0]
            restaurant_category = random_restaurant['Category'].iloc[0]
            print("Suggested restaurant: " + restaurant_name + ", Star Rating: " + str(restaurant_rating) + ", Category: " + restaurant_category)
            break 
        else: 
            print("There are no restaurants in " + user_desired_area + " with" + str(user_desired_rating) + " stars.")
            print("Please try another area or enter a new star rating.")

    else:
        print("There are no restaurants in " + user_desired_area + ". Please try another neighborhood")
        print("These are the available neighborhoods: ")
        print(seattle_restaurants_data['Area'].unique())


# Plot the data using a vertical bar chart
plt.figure(figsize=(10, 6))
plt.bar(top_10_neighborhoods.index, top_10_neighborhoods.values)
plt.xticks(rotation=45)
plt.xlabel('Neighborhood')
plt.ylabel('Number of Restaurants')
plt.title('Top 10 Neighborhoods with Highest Density of Restaurants in Seattle')
plt.show()


# Or create a sorted_group_count variable first then sort
sorted_group_count = grouped_count.sort_values(ascending=False)
print(grouped_count.head(10))


# Sort the DataFrame by the 'Star' column in descending order
sorted_df = seattle_restaurants_data.sort_values('Star', ascending=False)

# print(sorted_df.head(10))

# Get the top 10 restaurants with the highest star rating 
top_10_restaurant = sorted_df.head(10)

print(top_10_restaurant)

# Display the first 100 rows of the DataFrame
print(seattle_restaurants_data.head(100))

# Filter the DataFrame for restaurants where Category = 'Korean'
chinatown_restaurants = seattle_restaurants_data[
    (seattle_restaurants_data['Area'] == 'Chinatown') |
    (seattle_restaurants_data['Area'] == 'Chinatown International District')
]
print(chinatown_restaurants) 
