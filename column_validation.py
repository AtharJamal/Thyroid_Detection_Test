import json
def no_column_check():
    f = open("schema.json")
    content = json.load(f)
    for i in content["ColName"]:
        Length_of_DateStampinFile = content['LengthOfDateStampInFile']
        Length_Of_TimeStampInFile = content["LengthOfTimeStampInFile"]
        No_of_column = content["NumberofColumns"]
    return (Length_Of_TimeStampInFile, Length_of_DateStampinFile, No_of_column)