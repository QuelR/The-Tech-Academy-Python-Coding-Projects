
import os

os.listdir(path = "C:\\A\\")

fName0 = "a_Hello.txt"
fName1 = "a_My.txt"
fName2 = "a_Name.txt"
fName3 = "b_isRaquel.txt"
fName4 = "b_Rulli.txt"
fName5 = "c_iAm.txt"
fName6 = "c_Learning.txt"
fName7 = "c_Python.txt"
fName8 = "c_through.txt"
fName9 = "d_TechAcademy.txt"


fPath = "C:\\A\\"



abPath = os.path.join(fPath, fName1)
dirPath = os.listdir(path = "C:\\A\\")
timePath0 = os.path.getmtime("C:\\A\\a_hello.txt")
timePath1 = os.path.getmtime("C:\\A\\a_My.txt")
timePath2 = os.path.getmtime("C:\\A\\a_Name.txt")
timePath3 = os.path.getmtime("C:\\A\\b_isRaquel.txt")
timePath4 = os.path.getmtime("C:\\A\\b_Rulli.txt")
timePath5 = os.path.getmtime("C:\\A\\c_iAm.txt")
timePath6 = os.path.getmtime("C:\\A\\c_Learning.txt")
timePath7 = os.path.getmtime("C:\\A\\c_Python.txt")
timePath8 = os.path.getmtime("C:\\A\\c_through.txt")
timePath9 = os.path.getmtime("C:\\A\\d_TechAcademy.txt")

print(abPath,dirPath,timePath0,timePath1,timePath2,timePath3,timePath4,timePath5,timePath6,timePath7,timePath8,timePath9)

