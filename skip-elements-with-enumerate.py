def skip_elements(elements):
	# code goes here
	result = []
	#index = 0
	for index, element in enumerate(elements):
		index = index + 2
		#skiping the odd number
		if index % 2 == 0:
			result.append(element)
	return result
print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
