
num_list = []

#For input of row and column
row = int(input("Enter row: "))
column = int(input("Enter column: "))


# Creating 2d array list based on row and column
for i in range(row): # For row
    print(f"\nRow {i+1}:")
    inner_list = [] # List for inner  part
    
    for j in range(column): # For column
        num = float(input(f"Enter number {j+1}: "))
        inner_list.append(num) 
    
    num_list.append(inner_list)


#Searching for num
search_num = float(input("\nSearch: "))


#Print the num_list
print("\nThe numbers are:")
for i in range(len(num_list)):
    
    for j in range(len(num_list[i])):
        print(f"{num_list[i][j]:.1f}", end=' ')
        
    print()


# Searching for number in num_list
found_position = []
for i in range(len(num_list)):
    
    for j in range(len(num_list[i])):
        if search_num == num_list[i][j]:
            position = f"Row {i}, Col {j}"
            found_position.append(position)
            

#Printing the position of the number in row and col
print(f"\nNumber {search_num} found at", end=' ')
final = " and ".join(found_position)
print(final)