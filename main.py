from xml.dom import minidom

# https: // www.studytonight.com/python-howtos/how-to-read-xml-file-in-python

# parse an xml file by name
file = minidom.parse('firstXML.xml')

# use getElementsByTagName() to get tag
books = file.getElementsByTagName('books')
print(books[0])

# one specific item attribute
# print('model #2 attribute:')
# print(books[1].attributes['name'].value)

# all item attributes
#print('\nAll attributes:')
# for elem in books:
#  print(elem.attributes['name'].value)

# one specific item's data
# print('\nmodel #2 data:')
# print(books[1].firstChild.data)
# print(books[1].childNodes[0].data)

# all items data
#print('\nAll model data:')
# for elem in books:
#  print(elem.firstChild.data)
