import User
import questions
import sys
import MySQLdb
import random
from PyQt5.QtWidgets import QWidget, QApplication,QMessageBox
from Ui_MainWindow import Ui_Form_MainWindow
from error_list import Error_List_Ui
from PyQt5.QtCore import pyqtSignal

MySql_Address = '127.0.0.1'
MySql_Name = 'python_work'
MySql_Account = 'root'
MySql_Password = 'smz200132'
MySql_Table_User_Name = 'user'
input_Account = '张三'
input_Password = '123'
MySql_Table_Question_Name = 'questions'

Questions_ID = 0
Questions_ID_Max = 10

def MySql_Processing(Table_Name):
    #打开数据库
    try:
        db = MySQLdb.connect(MySql_Address,MySql_Account,MySql_Password,MySql_Name,charset='utf8')
    except:
        print('数据库链接错误\n')
        return False
    #使用cursor()方法
    cursor = db.cursor()
    #SQL查询语句
    sql = "SELECT * FROM " + Table_Name
    try:
        #执行语句
        cursor.execute(sql)
        #获取记录
        results = cursor.fetchall()
        #关闭数据库
        db.close()
        return results
    except:
        #关闭数据库
        db.close()
        print("指令读取失败\n")
        return False

class MainWindow(QWidget,Ui_Form_MainWindow):
    m_Sql_Data = ''
    m_Question_Index=0
    m_Question_Index_Max=10
    m_Question_ID=0
    m_Questions = {} #问题列表
    user = User.User()
    child_window = None

    m_Error_Questions = {} #错误问题列表
    m_Error_Questions_Number=0

    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent=parent)
        self.setupUi(self)
        self.Sql_Address.setText(MySql_Address)
        self.Sql_Name.setText(MySql_Name)
        self.Sql_Table_Name.setText(MySql_Table_Question_Name)
        self.Button_Last.setEnabled(False)
        self.Button_Next.setEnabled(False)
        self.Button_Answer.setEnabled(False)
        self.Button_Again_All.setEnabled(False)

        self.Button_Next.clicked.connect(self.Button_Next_Question)
        self.Button_Last.clicked.connect(self.Button_Last_Question)
        self.Button_Answer.clicked.connect(self.Button_Answer_Question)
        self.Button_Again_All.clicked.connect(self.Button_Again_All_Question)
        self.Button_Login.clicked.connect(self.Button_Login_Func)
        self.Button_Error_List.clicked.connect(self.Button_Error_List_Func)


    def User_Check(self,user):
        #在数据库取得账户数据
        data = MySql_Processing(MySql_Table_User_Name)
        if(data == False):
            return False
        else:
            for row in data:
                #print(row)
                Account = row[1]
                Password = row[2]
                if((input_Account == Account) and (input_Password == Password)):
                    user.set_Account(input_Account)
                    user.set_Password(input_Password)
                    print("账户:%s 密码:%s"%(user.get_Account(),user.get_Password()))
                    return True
                else:
                    return False

    def get_Question(self):
        self.m_Sql_Data = MySql_Processing(MySql_Table_Question_Name)
        if(self.m_Sql_Data == False):
            return False
        else:
            i = 0
            #随机题目种子 sample(range(0,len(data)), N)  N为生成N个
            max_number = len(self.m_Sql_Data)
            max_random = random.sample(range(0,max_number), Questions_ID_Max)
            for i in range(Questions_ID_Max):
                #print(max_random[i])
                for row in self.m_Sql_Data: #判断随机题目的ID
                    if(row[1] == max_random[i]):
                        self.m_Questions['question'+ str(i)] = questions.Questions(Question=row[0],ID=row[1],Answer=row[6],A=row[2],B=row[3],C=row[4],D=row[5])
                print("问题",i+1,":",self.m_Questions['question'+ str(i)].get_Question())

    def Show_Question(self):
        Index = 'question' + str(self.m_Question_Index)
        txt = self.m_Questions[Index].get_Question()+'\nA:'+self.m_Questions[Index].get_A()+'\tB:'+self.m_Questions[Index].get_B()+'\nC:'+self.m_Questions[Index].get_C()+'\tD:'+self.m_Questions[Index].get_D()
        self.Show_Questions.setPlainText(txt)

    def Save_User_Answer(self):
        Index = 'question' + str(self.m_Question_Index)
        self.user.set_Answer(self.Button_Get_Input_Answer())
        self.user.set_Completed_Question_ID(self.m_Questions[Index].get_ID())
        print('用户答案:',self.user.get_Answer())
        print('题目唯一ID:',self.m_Questions[Index].get_ID())
        print('题目下标:',Index)
        if((self.user.get_Answer() != self.m_Questions[Index].get_Answer()) and (self.user.get_Answer() != None)): #如果是错题，则存入错题列表
            error_index = 'error_question'+ str(self.m_Error_Questions_Number)
            print(error_index)
            self.m_Error_Questions[error_index] = questions.Questions(Question=self.m_Questions[Index].get_Question(),ID=self.m_Questions[Index].get_ID(),Answer=self.m_Questions[Index].get_Answer(),
                                                                    A=self.m_Questions[Index].get_A(),B=self.m_Questions[Index].get_B(),C=self.m_Questions[Index].get_C(),D=self.m_Questions[Index].get_D())
            self.m_Error_Questions_Number = self.m_Error_Questions_Number + 1
        #设置题目为已做
        self.m_Questions[Index].set_FinishOrNot(True)

    def Button_Answer_Question(self):
        Index = 'question' + str(self.m_Question_Index)
        txt = self.m_Questions[Index].get_Answer()
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

    def Button_Again_All_Question():
        pass

    #登入按钮执行功能
    def Button_Login_Func(self):
        #数据库链接
        global MySql_Address,MySql_Name,MySql_Table_Question_Name,MySql_Account,MySql_Password
        MySql_Address = self.Sql_Address.text()
        MySql_Name = self.Sql_Name.text()
        MySql_Table_Question_Name = self.Sql_Table_Name.text()
        MySql_Account = self.User_Name.text()
        MySql_Password = self.User_Password.text()
        print(MySql_Address,MySql_Name,MySql_Table_Question_Name,MySql_Account,MySql_Password)
        
        #没有在数据库得到数据
        if(self.get_Question() == False):
            QMessageBox.information(None, "信息提示框", "登入失败",QMessageBox.Yes)
        else: #得到了问题数据
            QMessageBox.information(None, "信息提示框", "登入成功",QMessageBox.Yes)
            self.Button_Last.setEnabled(True)
            self.Button_Next.setEnabled(True)
            self.Button_Answer.setEnabled(True)
            self.Button_Again_All.setEnabled(True)
    #错题列表按键 执行功能
    def Button_Error_List_Func(self):
        self.child_window = Error_List_Ui()
        self.child_window.set_Error_Questions(self.m_Error_Questions)
        self.child_window.set_Error_Questions_Number(self.m_Error_Questions_Number)
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