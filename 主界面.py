import User
import sys
import random
from PyQt5.QtWidgets import QWidget, QApplication,QMessageBox
from Ui_MainWindow import Ui_Form_MainWindow
from error_list import Error_List_Ui
from PyQt5.QtCore import pyqtSignal
from Sql import MySql

class MainWindow(QWidget,Ui_Form_MainWindow):
    m_Question_Index=0
    m_Question_Index_Max=10
    m_Question_ID=0
    m_Questions = {} #问题列表
    user = User.User()
    child_window = None
    #数据库对象
    sql = None

    m_Error_Questions = {} #错误问题列表
    m_Error_Questions_Number=0

    def __init__(self,parent=None):
        #初始化窗口
        super(MainWindow,self).__init__(parent=parent)
        self.setupUi(self)
        self.Sql_Address.setText('127.0.0.1')
        self.Sql_Name.setText('python_work')
        self.Sql_Table_Name.setText('questions')
        self.Button_Last.setEnabled(False)
        self.Button_Next.setEnabled(False)
        self.Button_Answer.setEnabled(False)
        self.Button_Again_All.setEnabled(False)
        #初始化信号槽
        self.Button_Next.clicked.connect(self.Button_Next_Question)
        self.Button_Last.clicked.connect(self.Button_Last_Question)
        self.Button_Answer.clicked.connect(self.Button_Answer_Question)
        self.Button_Again_All.clicked.connect(self.Button_Again_All_Question)
        self.Button_Login.clicked.connect(self.Button_Login_Func)
        self.Button_Error_List.clicked.connect(self.Button_Error_List_Func)

    def get_Question(self):
        #读取所有的题目ID
        m_Sql_Data = self.sql.get_Question_ID()
        if(m_Sql_Data == False):
            return False
        else:
            i = 0
            #随机题目种子 sample(range(0,len(data)), N)  N为生成N个
            max_number = len(m_Sql_Data)
            max_random = random.sample(range(0,max_number), self.m_Question_Index_Max)
            for i in range(self.m_Question_Index_Max):
                for row in m_Sql_Data: #判断随机题目的ID
                    if(row == max_random[i]):
                        #将随机出来的题目ID保存到字典中
                        self.m_Questions['question'+ str(i)] = row
                #测试是否读取出来
                print("问题",i+1,":",self.sql.get_Question_Topic_By_ID(self.m_Questions['question'+ str(i)]))

    def Show_Question(self):
        Index = 'question' + str(self.m_Question_Index)
        txt = self.sql.get_Question_Topic_By_ID(ID=self.m_Questions[Index]) + '\n' + self.sql.get_Question_A_By_ID(ID=self.m_Questions[Index]) + '\t' + self.sql.get_Question_B_By_ID(ID=self.m_Questions[Index]) + '\n' + self.sql.get_Question_C_By_ID(ID=self.m_Questions[Index]) \
            + '\t' + self.sql.get_Question_D_By_ID(ID=self.m_Questions[Index])
        self.Show_Questions.setPlainText(txt)

    def Save_User_Answer(self):
        Index = 'question' + str(self.m_Question_Index)
        user_Input_Answer = self.Button_Get_Input_Answer()

        #测试用
        print('用户答案:',user_Input_Answer)
        print('题目唯一ID:',self.m_Questions[Index])
        print('题目下标:',Index)

        #如果用户答案跟正确答案一致，则设置用户作对该题
        if(user_Input_Answer == self.sql.get_Question_Right_Answer_By_ID(ID=self.m_Questions[Index])):
            #设置题目作对
            self.sql.set_Question_RightOrError_By_ID(RightOrError=1,ID=self.m_Questions[Index])
        #设置题目为已做
        self.sql.set_Question_FinishOrNot_By_ID(FinishOrNot=1,ID=self.m_Questions[Index])

    def Button_Answer_Question(self):
        Index = 'question' + str(self.m_Question_Index)
        txt = self.sql.get_Question_Right_Answer_By_ID(ID=self.m_Questions[Index])
        self.Show_Answer.setPlainText(txt)

    def Button_Get_Input_Answer(self):
        if(self.Button_A.isChecked()):
            #self.Button_A.setCheckable(False);
            #self.Button_A.setCheckable(True);
            return 'A'
        if(self.Button_B.isChecked()):
            #self.Button_B.setCheckable(False);
            #self.Button_B.setCheckable(True);
            return 'B'
        if(self.Button_C.isChecked()):
            #self.Button_C.setCheckable(False);
            #self.Button_C.setCheckable(True);
            return 'C'
        if(self.Button_D.isChecked()):
            #self.Button_D.setCheckable(False);
            #self.Button_D.setCheckable(True);
            return 'D'

    def Button_Next_Question(self):
        self.Show_Question()
        self.Save_User_Answer()
        if(self.m_Question_Index < self.m_Question_Index_Max-1):
            self.m_Question_Index = self.m_Question_Index + 1

    def Button_Last_Question(self):
        self.Show_Question()
        self.Save_User_Answer()
        if(self.m_Question_Index > 0):
            self.m_Question_Index = self.m_Question_Index - 1

    def Button_Again_All_Question(self):
        if(QMessageBox.information(self, "信息提示框", "是否重置所有题",QMessageBox.Yes,QMessageBox.No) == QMessageBox.Yes):
            print("重置成功")
            self.sql.reset_Question()
        else:
            print("取消重置")

    #登入按钮执行功能
    def Button_Login_Func(self):
        #数据库链接
        #global MySql_Address,MySql_Name,MySql_Table_Question_Name,MySql_Account,MySql_Password
        MySql_Address = self.Sql_Address.text()
        MySql_Name = self.Sql_Name.text()
        MySql_Table_Question_Name = self.Sql_Table_Name.text()
        MySql_Account = self.User_Name.text()
        MySql_Password = self.User_Password.text()
        print(MySql_Address,MySql_Name,MySql_Table_Question_Name,MySql_Account,MySql_Password)
        #创建数据库操作对象
        self.sql = MySql(MySql_Address=MySql_Address,MySql_Name=MySql_Name,MySql_Account=MySql_Account,MySql_Password=MySql_Password,MySql_Table_User_Name=None,MySql_Table_Question_Name=MySql_Table_Question_Name)

        #没有在数据库得到数据
        if(self.get_Question() == False):
            QMessageBox.information(None, "信息提示框", "登入失败",QMessageBox.Yes)
        else: #得到了问题数据
            QMessageBox.information(None, "信息提示框", "登入成功",QMessageBox.Yes)
            self.Button_Last.setEnabled(True)
            self.Button_Next.setEnabled(True)
            self.Button_Answer.setEnabled(True)
            self.Button_Again_All.setEnabled(True)
            self.m_Question_Index = 0
            self.Show_Question()


    #错题列表按键 执行功能
    def Button_Error_List_Func(self):
        if(self.sql != None):
            self.child_window = Error_List_Ui(sql=self.sql)
            self.child_window.Show_Error_Questions()
            self.setVisible(False)
            #链接子窗口的关闭按钮信号
            self.child_window.close_Signal.connect(self.Child_Close_Func)
            self.child_window.show()

    #错题子窗口返回并注销功能
    def Child_Close_Func(self,cmd):
        if(cmd == 'close'):
            self.child_window.close()
            self.child_window = None
            self.setVisible(True)


if __name__ == "__main__":
    #固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    #初始化
    myWin = MainWindow()
    #将窗口控件显示在屏幕上
    myWin.show()
    #程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())