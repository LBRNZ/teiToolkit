# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import os
def cleanup(filePath):
    ns_map = {
      'tei': 'http://www.tei-c.org/ns/1.0'
    }
    tree = ET.parse(filePath)
    
    # Get Body Tag
    body = tree.find('.//tei:text/tei:body', ns_map)
    
    # Iterate over div tags inside body
    for div in body:
        head = div.find('tei:head', ns_map)
        if head is not None:
            # Print all headings
            print("".join(head.itertext()))

def __init__(self):
    inputInfo = "Bitte geben sie den Dateipfad an >>>>> "
    self.filePath = input(inputInfo)
    # Remove quotes from path if existing
    self.filePath = self.filePath.replace("'", "")
    self.filePath = self.filePath.replace('"', "")
    if os.path.isfile(self.filePath):
        cleanup(self.filePath)
    else: print("Pfad ist keine Datei")