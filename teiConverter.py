import os
import requests
# directory with files to convert to tei
directory = r'C:\Users\Marc\Documents\30 GIT\teiToolkit\inputData'

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
        'https://oxgarage2.tei-c.org/ege-webservice/Conversions/docx%3Aapplication%3Avnd.openxmlformats-officedocument.wordprocessingml.document/TEI%3Atext%3Axml',
        params=params,
        headers=headers,
        files=files,
    )
    file = open(filePath + ".zip", "wb")
    file.write(response.content)
    file.close()

# iterate over files in that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file and start conversion
    if os.path.isfile(f):
        convertFileToTEI(f)