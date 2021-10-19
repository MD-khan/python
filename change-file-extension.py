filenames = ["program.c", "profile.jpg", "sample.jpg", "a.out", "smile.jpg", "jpg.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = []
for filename in filenames:
	index = filename.index(".")
	if (filename[index:] == ".jpg"):
		allhppfiles = filename[:index] + filename[index:index+2]
		newfilenames.append(allhppfiles)
	elif (filename[index:] != ".jpg"):
		newfilenames.append(filename)
        
print(newfilenames) 
# Should be ["program.c", "profile.j", "sample.j", "a.out", "smile.j", "jpg.out"]
