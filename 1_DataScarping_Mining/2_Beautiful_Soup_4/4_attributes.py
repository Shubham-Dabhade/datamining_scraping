from bs4 import BeautifulSoup

###------ Attributes ------###
html = "<b class='abc' id='xyz'>Hello World</b>"
soup = BeautifulSoup(html,'html.parser')
tag = soup.b

#print(tag['id']) #provides the value of id attribute
#print(tag['class']) #provides the value of class attribute(returns a list)
tag['id'] = 'newId' #changing the value of attributes

print(tag.attrs) #provides a dictionary of all attributes of the tag


