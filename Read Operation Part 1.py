# open file and read its content
file= open('Codingal.txt','r')
print(file.read())
file.close()

#open file and read its beginning 8 characters
file= open('Codingal.txt','r')
print("\n Read in parts \n")
print(file.read(8))
file.close()

#append your name and age in the file
file=open("Codingal.txt","a")
file.write("Hi, I am Penguin, I am 2 million years old")
file.close



