import sys
sys.path.append('D:\svu\Term1\ADMdatamining')

from naiveBayesCode import *

row=input('enter your row like this \n [age[1-100],chestPain[1-3],BloodPressure[100-200],bloodSugar[0-1],restElectro[1-3],HeartRate[100-200],exerciceAngina[0-1]] \n example: [43,1,140,0,1,135,1] \n your new row is:  ')
print('your result is: ')
print(predictRow(row))