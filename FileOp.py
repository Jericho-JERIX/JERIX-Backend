import json

def getData(filename):
    file = open(f"./data/{filename}","r+")
    data = json.loads(file.read())
    file.close()
    return data

def saveData(filename,data):
    file = open(f"./data/{filename}","r+")
    file.seek(0)
    file.write(json.dumps(data))
    file.truncate()
    file.close()