## Lists
shoppingList = ["Apples", "Bananas", "Oranges"]
print(shoppingList[0])
numbers = [1, 1.5, "Two"]
print(numbers)
print("Length: " + str(len(numbers)))
numbers.append("2.5")
print(numbers)
numbers.pop(3)
print(numbers)
print("Two" in numbers)
print("2.5" in numbers)

## Dictionaries
pres = {"Current": "Trump", "Previous": "Obama"}
print(pres)
nums = {1: "One", 2: "To", 3: "Three"}
print(nums)
print("Key 1: "+ nums[1])
nums[2] = "Two"
print(nums)
print(nums.keys())
print("1" in nums.keys())
pres.update({"Current": "Biden", "Previous": "Trump"})
print(pres)
nums.pop(3)
print(nums)
