# coding: cp932
import sys
import codecs
import os
import re
import argparse

def getInfo(args):
    regexObj = re.compile(r"<[^>]*?>")
    searchPath = "C:\\Path"
    files = os.listdir(searchPath)
    custObjName = ''
    countNum = 1
    for fileName in files:
        with codecs.open(searchPath + "\\" + fileName, "r", encoding="utf_8") as diskliptObj:
            catchLabelFlag = False
            catchHoujinFlag = False
            fieldsFlag = False
            for luneNum, lineObj in enumerate(diskliptObj):
                if "<fields>" in lineObj:
                    fieldsFlag = True
                if "<valueField>" + args[1] + "</valueField>" in lineObj and fieldsFlag or "<referenceTo>" + args[1] + "</referenceTo>" in lineObj and fieldsFlag:
                    catchHoujinFlag = True
                if "<relationshipLabel>" in lineObj and catchLabelFlag == False:
                    custObjName = regexObj.sub("", lineObj.strip())
                    catchLabelFlag = True
                if catchHoujinFlag and catchLabelFlag:
                    print("通番：" + str(countNum))
                    print("ラベル名称：" + custObjName)
                    print("オブジェクトAPI名：" + fileName.replace('.object', ''))
                    print('\n')
                    catchHoujinFlag = False
                    catchLabelFlag = False
                    countNum = countNum + 1
                if "</CustomObject>" in lineObj:
                    custObjName = ''
                    tmpButtonTypeName = ''
                    break

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('cp932')
    args = sys.argv
    getInfo(args)
