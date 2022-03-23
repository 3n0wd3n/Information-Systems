from xml.dom import minidom
import xml.etree.ElementTree as ET
# load and parse the file
xmlTree = ET.parse('firstXML.xml')
elemList = []

for elem in xmlTree.iter():
    elemList.append(elem.tag)

print(elemList)
print()

for el in elemList:
  print(el)

print()

# parse an xml file by name
mydoc = minidom.parse('firstXML.xml')
print("Name of the first child node: ", mydoc.firstChild.nodeName)

"""
mydoc.ATTRIBUTE_NODE                mydoc.getElementsByTagNameNS(
mydoc.CDATA_SECTION_NODE            mydoc.getInterface(
mydoc.COMMENT_NODE                  mydoc.getUserData(
mydoc.DOCUMENT_FRAGMENT_NODE        mydoc.hasChildNodes(
mydoc.DOCUMENT_NODE                 mydoc.implementation
mydoc.DOCUMENT_TYPE_NODE            mydoc.importNode(
mydoc.ELEMENT_NODE                  mydoc.insertBefore(
mydoc.ENTITY_NODE                   mydoc.isSameNode(
mydoc.ENTITY_REFERENCE_NODE         mydoc.isSupported(
mydoc.NOTATION_NODE                 mydoc.lastChild
mydoc.PROCESSING_INSTRUCTION_NODE   mydoc.load(
mydoc.TEXT_NODE                     mydoc.loadXML(
mydoc.abort(                        mydoc.localName
mydoc.actualEncoding                mydoc.namespaceURI
mydoc.appendChild(                  mydoc.nextSibling
mydoc.async_                        mydoc.nodeName
mydoc.attributes                    mydoc.nodeType
mydoc.childNodes                    mydoc.nodeValue
mydoc.cloneNode(                    mydoc.normalize(
mydoc.createAttribute(              mydoc.ownerDocument
mydoc.createAttributeNS(            mydoc.parentNode
mydoc.createCDATASection(           mydoc.prefix
mydoc.createComment(                mydoc.previousSibling
mydoc.createDocumentFragment(       mydoc.removeChild(
mydoc.createElement(                mydoc.renameNode(
mydoc.createElementNS(              mydoc.replaceChild(
mydoc.createProcessingInstruction(  mydoc.saveXML(
mydoc.createTextNode(               mydoc.setUserData(
mydoc.doctype                       mydoc.standalone
mydoc.documentElement               mydoc.strictErrorChecking
mydoc.documentURI                   mydoc.toprettyxml(
mydoc.encoding                      mydoc.toxml(
mydoc.errorHandler                  mydoc.unlink(
mydoc.firstChild                    mydoc.version
mydoc.getElementById(               mydoc.writexml(
mydoc.getElementsByTagName(  
"""

