fulll_mailbox_list = [278, 512, 555, 987]

print("*" * 5 + " Mail Delivery Service " + "*" *5)
print("Welcome to the Mail Delivery Service!")
desired_flavour = input("What flavour would you lik? ")

def flavour_search(icecream_flavours_list, desired_flavour):
	for i in range(len(icecream_flavours_list)):
		if icecream_flavours_list[i] == desired_flavour:
			return True
			print("We do have that flavour!")
	return False