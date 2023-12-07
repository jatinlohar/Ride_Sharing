file1 = open("drivers.txt","r+")
 
print("Output of Read function is ")

driver_data = file1.read().split('\n')

print(driver_data)

file1.close()