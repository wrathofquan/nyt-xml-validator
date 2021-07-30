import os
from lxml import etree, objectify


 # for this to work make sure: tarfiles are uncompressed, 
 # and the files 'nitf-3-3.dtd' 'xhtml-ruby-1.mod' are in working directory

def validateXML(path):
    #parser = etree.XMLParser(dtd_validation=True, no_network=True)
    dtd = etree.DTD(open('nitf-3-3.dtd', 'rb'))
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.xml'):
                fname = os.path.join(root, file)
                try:
                    tree = objectify.parse(open(fname, 'rb'))
                    #print(dtd.validate(tree))
                except etree.XMLSyntaxError as err:
                    print(err)

validateXML("/path/to/xml/files")



