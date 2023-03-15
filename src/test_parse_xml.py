import xml.etree.ElementTree as ET


def main():
    print()

    sampleXmlFilePath = 'C:\\IVI\\Prog\\Inputs\\sample.xml'
    print('parsing XML file:')
    print(sampleXmlFilePath)

    tree = ET.parse(sampleXmlFilePath)
    rootElement = tree.getroot()

    parseXmlRec(rootElement)
    print()


def parseXmlRec(element):
    print()
    print('name: ' + element.tag)
    if not str.isspace(element.text):
        print('text: ' + element.text)
    if element.attrib.__len__() > 0:
        print('attributes: ' + str(element.attrib))        
    for childElement in element:
        parseXmlRec(childElement)


main()
