from data import *
from welcome import *
from linkedlist import LinkedList

print_welcome()

# Write code to insert cafe location into a data structure (LinkedList) here. The data is in data.py
def insert_cafe_location():   
    cafe_list = LinkedList()
    for neighborhood in location:
        cafe_list.insert_beginning(neighborhood)
    return cafe_list


# Write code to insert restaurant data into a data structure (LinkedList of LinkedLists) here. The data is in data.py
def insert_cafe_data():
    cafe_data_list = LinkedList()
    for neighborhood in location:
        cafe_sublist = LinkedList()
        for cafe in cafe_data:
            if cafe[0] == neighborhood:
                cafe_sublist.insert_beginning(cafe)
        cafe_data_list.insert_beginning(cafe_sublist)
    return cafe_data_list


my_location_list = insert_cafe_location()
my_cafe_list = insert_cafe_data()


selected_location = ""

# Write code for user interaction here
while len(selected_location) == 0:
    user_input = str(input(
        "\nWhat area of Charlotte would you like to search for cafes in?\n")).lower()
    
    # Search for user_input in food types data structure here
    matching_locations = []
    location_list_head = my_location_list.get_head_node()

    while location_list_head is not None:
        if str(location_list_head.get_value()).lower().startswith(user_input):
            print('Found matching value')
            matching_locations.append(location_list_head.get_value())
        location_list_head = location_list_head.get_next_node()

    # print list of matching food types
    for cafe in matching_locations:
        print(cafe)

    # Check if only one cafe was found, ask user if they would like to select this cafe
    if len(matching_locations) == 1:
        select_type = str(input(
            "\nThe only matching location for the specified input is " + matching_locations[0] + ". \nDo you want to look at cafes in " +
            matching_locations[0] + "? Enter y for yes and n for no\n")).lower()

        # After finding location write code for retrieving cafe data here
        if select_type == 'y':
            selected_location = matching_locations[0]
            print("Selected Cafe Location: " + selected_location)
            cafe_list_head = my_cafe_list.get_head_node()
            while cafe_list_head.get_next_node() is not None:
                sublist_head = cafe_list_head.get_value().get_head_node()
                if sublist_head.get_value()[0] == selected_location:
                    while sublist_head.get_next_node() is not None:
                        print("--------------------------")
                        print("Name: " + sublist_head.get_value()[1])
                        print("Price: " + sublist_head.get_value()[2] + "/5")
                        print("Rating: " + sublist_head.get_value()[3] + "/5")
                        print("Address: " + sublist_head.get_value()[4])
                        print("--------------------------\n")
                        sublist_head = sublist_head.get_next_node()
                cafe_list_head = cafe_list_head.get_next_node()

            # Ask user if they would like to search for other cafes
            repeat_loop = str(input("\nDo you want to find other cafes? Enter y for yes and n for no.\n")).lower()
            if repeat_loop == 'y':
                selected_location = ""