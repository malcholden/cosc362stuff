print("Hello World")

List = ["Junk", "in", "my", "trunk"]

for item in List:
	print("this is junk: ", item)
	print("STill in loop")

print("not in loop")

for i in range(len(List)):
	print("The {}th thing in the list is: {}!".format(i,List[i]))


