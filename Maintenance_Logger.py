#Ask the user to enter components that require maintenance and Store the components in a list.

components = []
print("Enter components that require maintenance. [Enter x to exit] : ")
item_number = 1
item = input(str(item_number) + ". ").title()
while item.lower() != "x":
     components.append(item)
     item_number = item_number + 1
     item = input(str(item_number) + ". ").title()
   

#show the full list to the user
print("\nAll components entered:")
for i,c in enumerate(components,start=1):
    print(f"{i}. {c}")

#Ask the user if maintenance has been done for any one component
maintenance = input("\nHas maintenance been done for any component? yes/no: ").lower()
maintained = []

#if yes,ask for the name of the component and Remove that component from the list.

if maintenance == "yes":      
   print("Enter the component(s) that have been maintained. [Enter x to exit] ")
   comp_number = 1
   while True:
        maintained_components = input(f"{comp_number}. ").title()
        if maintained_components.lower() == "x":
            print("All entries have been maintained")
            break
        if maintained_components in components:
            components.remove(maintained_components)
            maintained.append(maintained_components)
        elif maintained_components in maintained:
            print(f"{maintained_components} has already been removed.")
        else:
            print("component not found in list")
        comp_number = comp_number + 1
#Display a success message and the updated list.
print("\nList Updated Succesfully")
if maintained:
    print("\nThe Maintained components are :")
    for i,c in enumerate(maintained,start = 1):
        print(f"{i}.{c}")
else:
        print("\nThere are no maintained components.")
print("\nComponent(s) that still require maintenance:")
for i,c in enumerate(components,start = 1):
    print(f"{i}.{c}")            

#Save the final component list to a file named maintenance_log.txt.
#Also write a line stating which component was serviced, if any.
with open("Maintenance_Log.txt","w") as file:
    if maintained:
        file.write("The following components were serviced:")
        for i,c in enumerate(maintained, start=1):
            file.write(f"\n{i}.{c}\n")
    else:
        file.write("There were no serviced components\n")
    if components:
        file.write("\nThe following components were not serviced:\n")
        for i,c in enumerate(components, start=1):
            file.write(f"{i}.{c}\n")
    else:
        file.write("\nAll components were serviced")
#Finally, show the absolute path to the file (so the user knows where to find it).
import os
print("File saved as :",os.path.abspath("Maintenance_Log.txt"))