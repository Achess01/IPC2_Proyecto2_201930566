import xml.etree.ElementTree as ET

def validateXML(xml_str):
    try:
        xml = ET.fromstring(xml_str)
        return True
    except:
        return False