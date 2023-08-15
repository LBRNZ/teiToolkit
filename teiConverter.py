import os
import requests

def convertFileToTEI(filePath):
    headers = {
        'accept': 'application/pdf',
    }

    params = {
        'properties': '<conversions><conversion index="0"><property id="oxgarage.getImages">true</property><property id="oxgarage.getOnlineImages">true</property><property id="oxgarage.lang">en</property><property id="oxgarage.textOnly">false</property><property id="pl.psnc.dl.ege.tei.profileNames">default</property></conversion></conversions>',
    }

    files = {
        'fileToConvert': open(filePath, 'rb'),
    }

    response = requests.post(
        'https://oxgarage2.tei-c.org/ege-webservice/Conversions/docx:application:vnd.openxmlformats-officedocument.wordprocessingml.document/TEI:text:xml',
        params=params,
        headers=headers,
        files=files,
    )
    file = open(filePath + ".zip", "wb")
    file.write(response.content)
    file.close()

def iterateFiles(directory):
    # iterate over files in that directory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        # checking if it is a file and start conversion
        if os.path.isfile(f):
            convertFileToTEI(f)
            
def __init__(self):
    inputInfo = "Bitte geben sie den Ordnerpfad an >>>>> "
    self.directory = input(inputInfo)
    if os.path.isdir(self.directory):
       iterateFiles(self.directory)
    else:
       print("Ordner existiert nicht")
    