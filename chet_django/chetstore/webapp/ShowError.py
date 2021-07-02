from datetime import datetime
from os import error
import xml.etree.ElementTree as ET

FILENAME = 'Errors.xml'

def getErrors():
    data ={
            'errorVal': [],
            'errorH': [],
        }
    try:
        xml = ET.parse(FILENAME)
        root = xml.getroot()
        errorV = root.findall('ErrorValue')
        errorHe = root.findall('ErrorHeader')
        for err in errorV:
            new_err={
                'time': err.find('time').text,
                'file': err.find('file').text,
                'line': err.find('line').text,
                'value': err.find('value').text
            }
            data['errorVal'].append(new_err)
        
        for err in errorHe:
            new_err={
                'time': err.find('time').text,
                'header': err.find('header').text                
            }
            data['errorH'].append(new_err)
        return data
    except:
        return data

def addErrorValue(value, linenumber, file):
    try:
        time = datetime.now()
        xml = ET.parse(FILENAME)
        root = xml.getroot()
        line = ET.SubElement(root, "ErrorValue")
        time_referece = ET.SubElement(line, "time")
        time_referece.text = str(time)
        n_line = ET.SubElement(line, "line")
        n_line.text = str(linenumber)
        file_n = ET.SubElement(line, "file")
        file_n.text = file
        val = ET.SubElement(line, "value")
        val.text = value
        xml.write(FILENAME, encoding="utf-8")
    except:
        print("pass")


def addError(cabecera):
    try:
        time = datetime.now()
        xml = ET.parse(FILENAME)
        root = xml.getroot()
        line = ET.SubElement(root, "ErrorHeader")
        values = ''
        for item in cabecera:
            values+= str(item) + "-"
        header = ET.SubElement(line, "header")
        header.text = values
        time_reference = ET.SubElement(line, "time")
        time_reference.text = str(time)
        xml.write(FILENAME, encoding="utf-8")
    except:
        print("pass")

