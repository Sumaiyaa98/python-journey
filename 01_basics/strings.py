#slicing in string
tea = 'Lemon Tea'
slice_tea = tea[0:5]
#in slicing, we give the first and index length that we want to include 
print(slice_tea) #output: Lemon


# 📋 Original list of numbers
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 🔍 Slicing the list with three values: [start:stop:step]
slice_num = num[0:9:2]
# Explanation:
# start = 0   → start from index 0 (which is 0)
# stop = 9    → go up to index 9 (but not including index 9)
# step = 2    → take every 2nd element
# So it picks: index 0, 2, 4, 6, 8 → values: [0, 2, 4, 6, 8]

# 🖨️ Print the sliced list
print(slice_num)  # Output: [0, 2, 4, 6, 8]

#strip method, to remove extra spaces
name = '   Alex  '
print(name.strip())

#replace method, to replace our text with someone else
tea_name = "Ginger Tea"
print(tea_name.replace("Ginger","Lemon"))

#format method in python
chai_type = "Lemon"
quantity = 2
order = "Order {} cups of {} chai"
print(order.format(quantity,chai_type)) #output: Order 2 cups of Lemon chai
#in this, it will automatcally add the values at the place where u use {}