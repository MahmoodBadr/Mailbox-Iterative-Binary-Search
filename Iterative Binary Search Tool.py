'''
Author: Mahmood Badr
Date: July 21, 2022
Title: Mailbox Iterative Binary Search
'''

mailbox_arr = [278, 512, 555, 987]

print("*" * 5 + " Mail Delivery Service " + "*" * 5)
print("Welcome to the Mail Delivery Service!")

# Acquiring user input
mailbox_num = int(input("What mailbox number is yours? "))

def iterative_mailbox_binary_search(mailbox_arr, l, r, mailbox_num):

	while l <= r:

		mid = l + (r - l) // 2

		# Determining if the mailbox number is at mid
		if mailbox_arr[mid] == mailbox_num:
			return mid

		# Should the mailbox number be greater, then the left half is ignored
		elif mailbox_arr[mid] < mailbox_num:
			l = mid + 1

		# Should the mailbox number be lesser, then the right half is ignored
		else:
			r = mid - 1

	# Should the mailbox number be neither, then there is no mail (no number present in array)
	return -1

# Executing the iterative binary search function
result = iterative_mailbox_binary_search(mailbox_arr, 0, len(mailbox_arr)-1, mailbox_num)

# Presenting results to user
if result != -1:
	print("You have mail in your mailbox at index% d" % result)
else:
	print("You do not have any mail in your mailbox")