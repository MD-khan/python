def skip_elements(elements):
	# Initialize variables
	new_list = []
	i = 0

	# Iterate through the list
	for element in range(0, len(elements), 2):
		# Does this element belong in the resulting list?
		if elements != []:
			# Add this element to the resulting list
			new_list.append(elements[i])
		# Increment i
		i += 2

	return new_list
  
  print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
