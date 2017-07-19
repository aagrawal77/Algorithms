####### BUBBLE-SORT #######

# Open the CSV File - Pay attention to the path of the file
fileToOpen = open("/Users/sguler/Desktop/cities.csv")

# Read and assign the CSV File to citiesDoc
citiesDoc = fileToOpen.read()

# Split the citiesDoc line by line and add every line item to the citiesList
citiesList = citiesDoc.splitlines()

# Nested for loops to iterate thru the citiesList to sort and replace the cities as an ascending order
for i in range(len(citiesList)):
    for k in range(len(citiesList)-1):
        # check each item with the item next to it, and swap if out of order
        
        

# For loop to iterate and print the citiesList items
for city in citiesList:
    print(city, end=" ")
print()     # Prints an empty line

####### BINARY SEARCH #######

# Prompt user to enter a city - Pay attention the the lower/higher case letters
searchKey = input("Which city are you looking for?: ")

# Initialize variables
foundCity = ""
found = False
firstPoint = 0
lastPoint = len(citiesList)-1

# Loop thru the citiesList by updating the midPoint
while (firstPoint <= lastPoint and found == False):

    midPoint = int((firstPoint + lastPoint) / 2)

    # If the city found
    if ():
        
        

    # Else if the city is less than the citiesList midPoint in an alphabetic order
    elif ():
        

    # Else if the city is greater than the citiesList midPoint in an alphabetic order
    elif ():
        

# If the city is found, then print the city name. Else, print an error message!
if (found == True):
    print("Your city is in the city list. It is %s." % foundCity)
else:
    print("Your city is not in the city list!")
