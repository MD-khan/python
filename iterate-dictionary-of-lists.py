wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for key, values in wardrobe.items():
	for value in values:
		print("{} {}".format(value, key))
		
		
		
def email_list(domains):
	emails = []
	for domain, users in domains.items():
	  for user in users:
	    emails.append(user + "@" + domain)
	return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))
