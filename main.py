# coding=utf-8
# This is a sample Python script.from typing import List, Union, Any from typing import Set


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    # Question 1
    student_ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
    # Sort the list and find the min and max age
    sorted_stud_ages = sorted(student_ages)  # used sorted method to sort the age list
    print "The sorted ages list is: ", sorted_stud_ages

    # Add the min age and the max age again to the list
    student_min_age = min(student_ages)
    student_max_age = max(student_ages)
    student_ages.append(student_min_age)  # post using min, max methods to find the minimum and maximum age from list, appending the values to list
    student_ages.append(student_max_age)
    sorted_stud_ages = sorted(student_ages)
    print "New list that includes minimum and maximum age: ", sorted_stud_ages


    # Find the median age (one middle item or two middle items divided by two)
    student_ages_len = len(sorted_stud_ages)
    middle = (student_ages_len-1) // 2   # in order to find the median made use of length of list to note the middle index
    if middle % 2:
        print "Median from the age list is: ", sorted_stud_ages[middle] # if the middle index is even number, meaning that is the median
    else:
        print "Median from the age list is: ",(sorted_stud_ages[middle] + sorted_stud_ages[middle + 1]) / 2.0 # if the middle index is odd, meaning find the average of middle 2 numbers

    # Find the average age
    student_Average_age = sum(student_ages) / student_ages_len  # Used sum method to find the total of students ages and divided with students list length
    print "Average of the list of ages is: ", student_Average_age

    # Find the range of ages
    Range_ages = student_max_age - student_min_age #Calculated range of age list by finding the difference between minimum and maximum of students age
    print "Range of the ages: ", Range_ages

    #Question 2
    dog_dict = {}  #Created an empty dictionary named dog
    dog_dict = {"name": "Leo",
                "color": "White",
                "breed": "German Shepard",
                "legs": 4, "age": 8}  #Added key value pairs into dog dictionary
    student_dict ={"first_name":"John",
                   "last_name":"Green",
                   "gender":"Male", "age":35,
                   "marital_status":"Married",
                   "skills":[ "Inventive"],
                   "country":"India",
                   "city":"Bangalore",
                   "address":"Chetpet"} #created student dictionary with key, value pairs
    print "Length of student dictionary is: ",len(student_dict)  # student dictionary length is found using len() method
    print "Student skills: ",student_dict["skills"]   #Value of student skills
    print "Type of Student skills: ", type(student_dict["skills"]) #Type of student skills
    student_dict["skills"] += ["Creativity", "Communication", "Leadership"]  #As student skills key is configured as type list, adding multiple values into the skills list

    print "Student dictionary keys: ", student_dict.keys()
    print "Student dictionary values: ", student_dict.values() # Retrieved dictionary key and values individually as lists

    # Question 3
    brothers_tuple = ("Badra", "Madan", "Hemanth", "Nani")
    sisters_tuple = ("Sandhya", "Chinni", "Chinnu", "Swarni") # Created tuples of brothers and sisters
    siblings_tuple = brothers_tuple + sisters_tuple # Joined 2 tuples into siblings
    print "Siblings : ", siblings_tuple
    print "Total number of siblings: ", len(siblings_tuple) # Found the number of siblings
    siblings_tuple = siblings_tuple + ("Amma", "Nanna")
    family_members_tuple = siblings_tuple # Modified sibling tuple and added to family tuple
    print "Family members: ", family_members_tuple

    # Question 4
    it_companies_set = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
    A_set = {19, 22, 24, 20, 25, 26}
    B_set = {19, 22, 20, 25, 26, 24, 28, 27}
    age_list = [22, 19, 24, 25, 26, 24, 25, 24]
    print "length of it_companies: ", len(it_companies_set)  # length of the set is found using len()
    it_companies_set.add("twitter")  # Added one value into set using add()
    print 'IT companies: ', it_companies_set
    additional_companies_set={'Accenture', 'Infosys', 'TCS'}
    it_companies_set.update(additional_companies_set)  # Inserted multiple it companies with additional values
    print 'IT companies post adding multiple companies at once: ', it_companies_set
    it_companies_set.remove('TCS')  # Using remove(), removing 1 IT company
    it_companies_set.discard('TCS')
    #If the item to remove does not exist, remove() will raise an error.
    #If the item to remove does not exist, discard() will NOT raise an error.
    print "post removing TCS, it_companies tuple: ", it_companies_set
    print "A join B: ", A_set.union(B_set)   # To get items in both A and B
    print "A intersection B: ", A_set.intersection(B_set)  # to get items similar in both A and B
    print "Is A subset B: ", A_set.issubset(B_set)  # To find if A is subset of B, as A is subset it is true
    print "Are A and B disjoint sets: ", A_set.isdisjoint(B_set)  # To find if A and B are disjoint sets
    print "B join A: ", B_set.union(A_set)
    print "Symmetric difference between A and B: ", A_set.symmetric_difference(B_set)
    del A_set
    del B_set
    del it_companies_set
    age_set = set(age_list)  # Converting age list to set
    print 'age_set', age_set
    print "difference between length of age_set and age_list: ", len(age_list)-len(age_set)
    print "comparing the length of age_set and age_list: ", len(age_list) == len(age_set) #comparing length using == operator


    # Question 5
    import math  # imported math in order to use pi
    radius_circle = 30
    area_of_circle = math.pi*radius_circle**2  # assigning to area to variable
    circumference_of_circle = math.pi*radius_circle # calculating circumference and assigning to variable
    print ("The area of the circle with radius " + str(radius_circle) + " is: " + str(area_of_circle))
    in_radius_circle = float(input("Input the radius of the circle : ")) #user should input radius of circle
    print ("The area of the circle with radius " + str(in_radius_circle) + " is: " + str(math.pi*in_radius_circle**2))

    # Question 6
    sentence_str = 'I am a teacher and I love to inspire and teach people'
    words_set = set() # Initialized a set
    words_set = sentence_str.split(" ") # Split the given sentence and stored in set
    print words_set
    unique_list = []  #Initialized a list
    for words in words_set:  # Looping through each word in the words set
        if words not in unique_list: # Check if the word doesn't exist in list
            unique_list.append(words)  # if words doesn't exist in the list add it to the list
    print "total unique words in the given sentence: ", len(unique_list)
    print "total unique words in the given sentence: ", unique_list



    # Question 7
    print '\t Name\t Age\t Country\t City\n Asabench \t 250 \t Finland \t Helsinki'  # \t represents tab space and \n represents new line

    # Question 8
    radius = 10
    area = 3.14 * radius ** 2
    print "The area of a circle with radius {0} is {1} meters square.”".format(radius, int(area))

    # Question 9
    import math
    num_of_students = input("Input the number of students: ")  # Fetched the number of students from user
    student_wgt_list_lbs = []   # Initialized list to store student weights in lbs
    for student_weight in range(0, num_of_students):
        student_wgt_list_lbs.append(input("Input weight of student :" +str(student_weight+1)))  # For each student asking user to input weights
    print 'Student weights given by user in pounds: ', student_wgt_list_lbs
    student_wgt_list_kgs = []  # Initialized another list to store student weights in kgs
    for student_weight_lbs in range(0, num_of_students):
        student_wgt_list_kgs.append(float(student_wgt_list_lbs[student_weight_lbs]/2.2046)) # For each student weight in lbs, converting them to kgs and storing in another list
    #print student_wgt_list_kgs
    temp = []
    for i in student_wgt_list_kgs:
        float(i)
        temp.append(float(round(i, 2)))
    print 'Student weights converted to Kilograms: ', temp




# See PyCharm help at https://www.jetbrains.com/help/pycharm/

