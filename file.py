#opening a file
fo=open("text.txt","w") #a means append w means write mode
#print name of the file
print("file name is :",fo.name)
print("closed or not: ",fo.closed)
print("mode of file :",fo.mode)

#writing in file 
fo.write("I love Python Programming\nI want to settle as a Python and Django Developer\n")
fo.write("I love Python ")
fo.write("and JavaScript")
fo.close()
# appending text to previous file
fo=open("text.txt",'a')
fo.write("\nI also like Django")
fo.close()
# Reading file in Same location
fo = open("text.txt","r+")
#Reading entire file
textfile=fo.read()
print(textfile)
fo.close()
#writing or creating file
fo=open("text2.txt","w+")
fo.write("This is sencond text file created Auto")
fo.close()


