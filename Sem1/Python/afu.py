filename = raw_input("enter a filename: ")
if "." in filename:
	name, extention = filename.split(".")
	print("the extention of the file is: " +extention)
else:
	print("invalid file name format.please iinclude the file extention (eg.,filename.txt)")
