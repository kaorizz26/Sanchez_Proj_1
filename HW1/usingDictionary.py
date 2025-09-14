
# Dicitionary for numbers
num_dict = {}

row = int(input("Enter row: "))
column = int(input("Enter column: "))

# Adding values to keys
for i in range(row):
    print(f"Row {i+1}")
    
    for j in range(column):
        num_value = float(input(f"Enter number {j+1}: "))
        num_dict[(i, j)] = num_value

#Searching for the number
search_number = float(input("\nSearch number: "))

#Printing the stored values in dictionary
print("\nThe numbers are:")
for i in range(row):              
    for j in range(column):      
        print(f"{num_dict[(i, j)]}",end=' ')
    print()  


#Print the found numbers and their position
found_position = []
print(f"Number {search_number} found at",end=' ')

for i in range(row):
    for j in range(column):
        if search_number == num_dict[(i, j)]:
            position = f"Row {i}, Col {j}"
            found_position.append(position)
            
final = " and ".join(found_position)
print(final)