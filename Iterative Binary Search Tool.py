mailbox_arr = [278, 512, 555, 987]

print("*" * 5 + " Mail Delivery Service " + "*" * 5)
print("Welcome to the Mail Delivery Service!")
x = int(input("What mailbox number is yours? "))

# Python3 code to implement iterative Binary
# Search.

# It returns location of x in given array arr
# if present, else returns -1


def binarySearch(mailbox_arr, l, r, x):

	while l <= r:

		mid = l + (r - l) // 2

		# Check if x is present at mid
		if mailbox_arr[mid] == x:
			return mid

		# If x is greater, ignore left half
		elif mailbox_arr[mid] < x:
			l = mid + 1

		# If x is smaller, ignore right half
		else:
			r = mid - 1

	# If we reach here, then the element
	# was not present
	return -1

# Function call
result = binarySearch(mailbox_arr, 0, len(mailbox_arr)-1, x)

if result != -1:
	print("You have mail in your mailbox at index % d" % result)
else:
	print("You do not have any mail in your mailbox")