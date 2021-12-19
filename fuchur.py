# importing the modules
import requests, sys
from bs4 import BeautifulSoup

number_of_arguments = len(sys.argv)
argument_list = str(sys.argv)

#The string looks originally like this ['argument1', 'argument2', 'argument3', 'argument4']
#So we remove all chars that we dont need.
argument_list = argument_list.replace("[", "")
argument_list = argument_list.replace("]", "")
argument_list = argument_list.replace(" ", "")
argument_list = argument_list.replace("'", "")

#Now we convert the string into an array. We use the comma to separate the words
inputlist = argument_list.split(",")

#inputfile variable is position 1 from the array
url = inputlist[1]
outputfile = inputlist[2]

# making requests instance
reqs = requests.get(url)

# using the BeaitifulSoup module
soup = BeautifulSoup(reqs.text, 'html.parser')

new_file = open(outputfile, 'a')

# displaying the title
print("The following website was added to your bookmarks : ")
for title in soup.find_all('title'):
	print(title.get_text())
	entry =  title.get_text() + " - " + url + "\n"
	new_file.write(entry)
	new_file.close()
