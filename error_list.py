import sys
from PyQt5.QtWidgets import QWidget
from Ui_UiMain_work_1_2 import Ui_Form
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import *
from Sql import MySql

class Error_List_Ui(QWidget,Ui_Form):
    close_Signal = pyqtSignal(str)
    m_Error_Questions = [] #错误问题列表
    m_Error_Questions_Number=0 #总的问题数
    m_Choose_Index = None #选择的“问题”的字典键值
    sql = None #type:MySql

    def __init__(self,parent=None,sql=None):
        super(Error_List_Ui,self).__init__(parent=parent)
        self.setupUi(self)
        self.B_return.clicked.connect(self.Button_Return_Func)
        self.listWidget.itemClicked.connect(self.Questions_Choose)
        self.B_last.clicked.connect(self.Button_Last_Func)
        self.B_next.clicked.connect(self.Button_Next_Func)
        self.B_rm.clicked.connect(self.Button_Delete_Func)
        self.B_answer.clicked.connect(self.Button_Show_Answer)

        #获得数据库连接
        self.sql = sql
        #获得数据库中的错题
        self.set_Error_Questions()
        self.set_Error_Questions_Number()

    def Button_Return_Func(self):
        self.close_Signal.emit('close')

    #设置sql连接(由上个界面传递)
    def set_SQL_VALUE(self,sql)->MySql:
        self.sql = sql

    #设置错误问题字典
    def set_Error_Questions(self):
        
        #print(self.sql.get_Question_Error_ID())
        #获得所有的错题ID号
        self.m_Error_Questions = self.sql.get_Question_Error_ID()
        if(self.m_Error_Questions == False):
            self.m_Error_Questions=[]
        #打印一下获得的键值
        print('问题键值:',self.m_Error_Questions)
    #设置错题数量
    def set_Error_Questions_Number(self):
        self.m_Error_Questions_Number = self.sql.get_Question_Error_Number()
        print('错题数量:',self.m_Error_Questions_Number)

    #获得错题数量
    def get_Error_Questions_Number(self):
        return self.m_Error_Questions_Number
    
    #循环添加问题到listWidget列表
    def Show_Error_Questions(self):
        i = 0
        while i < self.m_Error_Questions_Number:
            self.listWidget.addItem(str(self.m_Error_Questions[i]))
            print('错题:',self.sql.get_Question_Topic_By_ID(self.m_Error_Questions[i]))
            i = i+1

    #在listWidget列表中获得选择的问题的下标
    def Questions_Choose(self,item):
        #self.textEdit.setPlainText(item.text())
        #print('选择了:',item.text())
        print('选中了第',self.listWidget.currentRow(),'项')
        self.m_Choose_Index = self.listWidget.currentRow()
        self.Show_Question()

    def Show_Question(self):
        #index = 'error_question' + str(self.m_Choose_Index)
        self.textEdit.setPlainText(self.sql.get_Question_Topic_By_ID(self.m_Error_Questions[self.m_Choose_Index]))
        self.label_A.setText(self.sql.get_Question_A_By_ID(self.m_Error_Questions[self.m_Choose_Index]))
        self.label_B.setText(self.sql.get_Question_B_By_ID(self.m_Error_Questions[self.m_Choose_Index]))
        self.label_C.setText(self.sql.get_Question_C_By_ID(self.m_Error_Questions[self.m_Choose_Index]))
        self.label_D.setText(self.sql.get_Question_D_By_ID(self.m_Error_Questions[self.m_Choose_Index]))

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
        #保存到数据库中
        print("删除ID:",self.m_Error_Questions[self.m_Choose_Index])
        self.sql.set_Question_RightOrError_By_ID(RightOrError=1,ID=self.m_Error_Questions[self.m_Choose_Index])
        #设置需要删除的 错题下标
        del self.m_Error_Questions[self.m_Choose_Index]
        self.listWidget.takeItem(self.m_Choose_Index)
        #问题总数-1
        self.m_Error_Questions_Number = self.m_Error_Questions_Number - 1
        #选择的问题的下标置为空，防止误操作
        self.m_Choose_Index=None

    def Button_Show_Answer(self):
        if(self.m_Choose_Index != None):
            #获得当前选择的问题的下标，并且追加到问题框
            txt = '\n' + self.sql.get_Question_Right_Answer_By_ID(self.m_Error_Questions[self.m_Choose_Index])
            self.textEdit.moveCursor(QTextCursor.End)
            self.textEdit.insertPlainText(txt)

