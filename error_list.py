import sys
from PyQt5.QtWidgets import QWidget
from Ui_UiMain_work_1_2 import Ui_Form
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import *

class Error_List_Ui(QWidget,Ui_Form):
    close_Signal = pyqtSignal(str)
    m_Error_Questions = {} #错误问题列表
    m_Error_Questions_Number=0 #总的问题数
    m_Choose_Index = 0 #选择的“问题”的字典键值

    def __init__(self,parent=None):
        super(Error_List_Ui,self).__init__(parent=parent)
        self.setupUi(self)
        self.B_return.clicked.connect(self.Button_Return_Func)
        self.listWidget.itemClicked.connect(self.Questions_Choose)
        self.B_last.clicked.connect(self.Button_Last_Func)
        self.B_next.clicked.connect(self.Button_Next_Func)
        self.B_rm.clicked.connect(self.Button_Delete_Func)
        self.B_answer.clicked.connect(self.Button_Show_Answer)

    def Button_Return_Func(self):
        self.close_Signal.emit('close')

    #设置错误问题字典
    def set_Error_Questions(self,Error_Questions):
        self.m_Error_Questions.update(Error_Questions)
        #打印一下获得的键值
        print('问题键值:',list(self.m_Error_Questions.keys()))
    def get_Error_Questions(self):
        return self.m_Error_Questions
    
    def set_Error_Questions_Number(self,Error_Questions_Number):
        self.m_Error_Questions_Number = Error_Questions_Number
        print('错题数量:',self.m_Error_Questions_Number)
    def get_Error_Questions_Number(self):
        return self.m_Error_Questions_Number
    
    #循环添加问题到listWidget列表
    def Show_Error_Questions(self):
        i = 0
        while i < self.m_Error_Questions_Number:
            self.listWidget.addItem(str(self.m_Error_Questions['error_question'+str(i)].get_ID()))
            print('错题:',self.m_Error_Questions['error_question'+str(i)].get_Question())
            i = i+1

    #在listWidget列表中获得选择的问题的下标
    def Questions_Choose(self,item):
        #self.textEdit.setPlainText(item.text())
        #print('选择了:',item.text())
        print('选中了第',self.listWidget.currentRow(),'项')
        self.m_Choose_Index = self.listWidget.currentRow()
        self.Show_Question()

    def Show_Question(self):
        index = 'error_question' + str(self.m_Choose_Index)
        self.textEdit.setPlainText(self.m_Error_Questions[index].get_Question())
        self.label_A.setText(self.m_Error_Questions[index].get_A())
        self.label_B.setText(self.m_Error_Questions[index].get_B())
        self.label_C.setText(self.m_Error_Questions[index].get_C())
        self.label_D.setText(self.m_Error_Questions[index].get_D())

    def Button_Last_Func(self):
        if(self.m_Choose_Index != None):
            if(self.m_Choose_Index > 0 ):
                self.m_Choose_Index = self.m_Choose_Index - 1
                self.Show_Question()

    def Button_Next_Func(self):
        if(self.m_Choose_Index != None):
            if(self.m_Choose_Index < self.m_Error_Questions_Number-1):
                self.m_Choose_Index = self.m_Choose_Index + 1
                self.Show_Question()

    def Button_Delete_Func(self):
        if(self.m_Choose_Index == None):
            return
        #设置需要删除的 错题下标
        index = 'error_question' + str(self.m_Choose_Index)
        del self.m_Error_Questions[index]
        self.listWidget.takeItem(self.m_Choose_Index)

        #在问题字典中删除选择的键值对
        i = self.m_Choose_Index
        while i < self.m_Error_Questions_Number-1:
            temp = 'error_question'+str(i)
            print(temp)
            temp1 = 'error_question'+str(i+1)
            print(temp1)
            #要删除的键值的后面的键值循环替换前面
            self.m_Error_Questions[temp] = self.m_Error_Questions.pop(temp1)
            i=i+1
        #问题总数-1
        self.m_Error_Questions_Number = self.m_Error_Questions_Number - 1
        #选择的问题的下标置为空，防止误操作
        self.m_Choose_Index=None

    def Button_Show_Answer(self):
        if(self.m_Choose_Index != None):
            #获得当前选择的问题的下标，并且追加到问题框
            index = 'error_question' + str(self.m_Choose_Index)
            txt = '\n' + self.m_Error_Questions[index].get_Answer()
            self.textEdit.moveCursor(QTextCursor.End)
            self.textEdit.insertPlainText(txt)

