import MySQLdb

class MySql:
    #数据库内的字段
    __SQL_Topic = 'Topic'
    __SQL_ID = 'ID'
    __SQL_A = 'A'
    __SQL_B = 'B'
    __SQL_C = 'C'
    __SQL_D = 'D'
    __SQL_Right_Answer = 'Right_Answer'
    __SQL_FinishOrNot = 'FinishOrNot'
    __SQL_RightOrError = 'RightOrError'
    #链接数据库的参数
    MySql_Address = '127.0.0.1'
    MySql_Name = 'python_work'
    MySql_Account = 'root'
    MySql_Password = 'smz200132'
    MySql_Table_User_Name = 'user'
    MySql_Table_Question_Name = 'questions'

    def __init__(self,MySql_Address,MySql_Name,MySql_Account,MySql_Password,MySql_Table_User_Name,MySql_Table_Question_Name)->str:
        #初始化数据库链接参数
        self.MySql_Address = MySql_Address
        self.MySql_Name = MySql_Name
        self.MySql_Account = MySql_Account
        self.MySql_Password = MySql_Password
        self.MySql_Table_User_Name = MySql_Table_User_Name
        self.MySql_Table_Question_Name = MySql_Table_Question_Name

    #本文件测试用
    #def __init__(self):
    #    pass
    
    #链接数据库
    def MySql_Processing(self,SQL_Statement)->str:
        #打开数据库
        try:
            db = MySQLdb.connect(self.MySql_Address,self.MySql_Account,self.MySql_Password,self.MySql_Name,charset='utf8')
        except:
            print('数据库链接错误\n')
            return False
        #使用cursor()方法
        cursor = db.cursor()
        #SQL查询语句
        #sql = "SELECT * FROM " + Table_Name
        try:
            #执行语句
            cursor.execute(SQL_Statement)
            # 提交更改
            db.commit()
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
        
    #指定ID数据 SQL语句生成
    def SQL_SELECT_Statement_Generation_Appoint_ID(self,field,table_name,field_name,field_value):
        sql = "SELECT {field} FROM {table_name} WHERE {field_name} = '{value}'".format(field=field,table_name=table_name,field_name=field_name,value=field_value)
        return sql
    
    #获得指定题目ID的数据
    def get_Question_By_ID(self,ID):
        sql = self.SQL_SELECT_Statement_Generation_Appoint_ID(field='*',table_name=self.MySql_Table_Question_Name,field_name=self.__SQL_ID,field_value=ID)
        data = self.MySql_Processing(sql)[0]
        if(data != False):
            return data
        else:
            return False
    #获得指定题目ID的问题   返回元组
    def get_Question_Topic_By_ID(self,ID)->str:
        sql = self.SQL_SELECT_Statement_Generation_Appoint_ID(field=self.__SQL_Topic,table_name=self.MySql_Table_Question_Name,field_name=self.__SQL_ID,field_value=ID)
        data = self.MySql_Processing(sql)[0]
        if(data != False):
            return data[0]
        else:
            return False
        
    #获得指定题目ID的A选项结果
    def get_Question_A_By_ID(self,ID)->str:
        sql = self.SQL_SELECT_Statement_Generation_Appoint_ID(field=self.__SQL_A,table_name=self.MySql_Table_Question_Name,field_name=self.__SQL_ID,field_value=ID)
        data = self.MySql_Processing(sql)[0]
        if(data != False):
            return data[0]
        else:
            return False
        
    #获得指定题目ID的B选项结果
    def get_Question_B_By_ID(self,ID)->str:
        sql = self.SQL_SELECT_Statement_Generation_Appoint_ID(field=self.__SQL_B,table_name=self.MySql_Table_Question_Name,field_name=self.__SQL_ID,field_value=ID)
        data = self.MySql_Processing(sql)[0]
        if(data != False):
            return data[0]
        else:
            return False
        #获得指定题目ID的C选项结果
    def get_Question_C_By_ID(self,ID)->str:
        sql = self.SQL_SELECT_Statement_Generation_Appoint_ID(field=self.__SQL_C,table_name=self.MySql_Table_Question_Name,field_name=self.__SQL_ID,field_value=ID)
        data = self.MySql_Processing(sql)[0]
        if(data != False):
            return data[0]
        else:
            return False
    #获得指定题目ID的D选项结果
    def get_Question_D_By_ID(self,ID)->str:
        sql = self.SQL_SELECT_Statement_Generation_Appoint_ID(field=self.__SQL_D,table_name=self.MySql_Table_Question_Name,field_name=self.__SQL_ID,field_value=ID)
        data = self.MySql_Processing(sql)[0]
        if(data != False):
            return data[0]
        else:
            return False
    #获得指定题目ID的正确结果
    def get_Question_Right_Answer_By_ID(self,ID)->str:
        sql = self.SQL_SELECT_Statement_Generation_Appoint_ID(field=self.__SQL_Right_Answer,table_name=self.MySql_Table_Question_Name,field_name=self.__SQL_ID,field_value=ID)
        data = self.MySql_Processing(sql)[0]
        if(data != False):
            return data[0]
        else:
            return False
    #通道指定题目ID的查看有没有做过该题  返回0为没有完成
    def get_Question_FinishOrNot_By_ID(self,ID)->str:
        sql = self.SQL_SELECT_Statement_Generation_Appoint_ID(field=self.__SQL_FinishOrNot,table_name=self.MySql_Table_Question_Name,field_name=self.__SQL_ID,field_value=ID)
        data = self.MySql_Processing(sql)[0]
        if(data != False):
            return data[0]
        else:
            return False
    #通道指定题目ID的查看该题有没有做错 返回0为做错了
    def get_Question_RightOrError_By_ID(self,ID)->str:
        sql = self.SQL_SELECT_Statement_Generation_Appoint_ID(field=self.__SQL_RightOrError,table_name=self.MySql_Table_Question_Name,field_name=self.__SQL_ID,field_value=ID)
        data = self.MySql_Processing(sql)[0]
        if(data != False):
            return data[0]
        else:
            return False
        
    #获得所有错题的ID号
    def get_Question_Error_ID(self)->None:
        sql = "SELECT ID FROM questions WHERE RightOrError = 0 and FinishOrNot = 1"
        #sql = self.SQL_SELECT_Statement_Generation_Appoint_ID(field=self.__SQL_ID,table_name=self.MySql_Table_Question_Name,field_name=self.__SQL_RightOrError,field_value='0')
        data = self.MySql_Processing(sql)
        # 提取结果中的 ID 值
        ids = [row[0] for row in data]
        if(ids != False):
            return ids
        else:
            return False

    #获得所有错题的数量
    def get_Question_Error_Number(self)->None:
        sql = "SELECT COUNT(*) AS count FROM questions WHERE FinishOrNot = 1 AND RightOrError = 0;"
        #sql = self.SQL_SELECT_Statement_Generation_Appoint_ID(field='COUNT(*)',table_name=self.MySql_Table_Question_Name,field_name=self.__SQL_RightOrError,field_value='1')
        data = self.MySql_Processing(sql)[0]
        if(data != False):
            return data[0]
        else:
            return False
        
    #获得所有已做题的ID号
    def get_Question_Finish_ID(self)->None:
        #SELECT ID FROM your_table_name WHERE RightOrError = 1;
        sql = self.SQL_SELECT_Statement_Generation_Appoint_ID(field=self.__SQL_ID,table_name=self.MySql_Table_Question_Name,field_name=self.__SQL_FinishOrNot,field_value='1')
        data = self.MySql_Processing(sql)
        # 提取结果中的 ID 值
        ids = [row[0] for row in data]
        if(ids != False):
            return ids
        else:
            return False
    #获得已做题的数量
    def get_Question_Finish_Number(self)->None:
        #SELECT COUNT(*) FROM your_table_name WHERE RightOrError = 1;
        sql = self.SQL_SELECT_Statement_Generation_Appoint_ID(field='COUNT(*) AS count',table_name=self.MySql_Table_Question_Name,field_name=self.__SQL_FinishOrNot,field_value='1')
        data = self.MySql_Processing(sql)[0]
        if(data != False):
            return data[0]
        else:
            return False
        
    #获得数据库中题目的ID
    def get_Question_ID(self)->None:
        sql = "SELECT id FROM questions"
        data = self.MySql_Processing(sql)
        # 提取结果中的 ID 值
        ids = [row[0] for row in data]
        if(ids != False):
            return ids
        else:
            return False

    #同过题目ID，设置该题是否做过的SQL语句生成
    def SQL_UPDATE_Statement_Generation_Appoint_ID(self,table_name,target_field_name,Target_Value,field_name,field_name_value)->str:
        sql = "UPDATE {table_name} SET {target_field_name} = '{Target_Value}' WHERE {field_name} = '{field_name_value}'".format(table_name=table_name,target_field_name=target_field_name,Target_Value=Target_Value,field_name=field_name,field_name_value=field_name_value)
        return sql
    
    #设置指定题目ID是否做过 1为做了，0为未做
    def set_Question_FinishOrNot_By_ID(self,FinishOrNot,ID)->bool:
        sql = self.SQL_UPDATE_Statement_Generation_Appoint_ID(table_name=self.MySql_Table_Question_Name,target_field_name=self.__SQL_FinishOrNot,Target_Value=FinishOrNot,field_name=self.__SQL_ID,field_name_value=ID)
        self.MySql_Processing(sql)

    #设置指定题目ID是否为错题  1为错题，0为正确
    def set_Question_RightOrError_By_ID(self,RightOrError,ID)->bool:
        sql = self.SQL_UPDATE_Statement_Generation_Appoint_ID(table_name=self.MySql_Table_Question_Name,target_field_name=self.__SQL_RightOrError,Target_Value=RightOrError,field_name=self.__SQL_ID,field_name_value=ID)
        self.MySql_Processing(sql)

    #重置题库
    def reset_Question(self)->None:
        sql = "UPDATE {table_name} SET {target_field_name} = '{Target_Value}'".format(table_name=self.MySql_Table_Question_Name,target_field_name=self.__SQL_FinishOrNot,Target_Value='0')
        self.MySql_Processing(sql)
        sql = "UPDATE {table_name} SET {target_field_name} = '{Target_Value}'".format(table_name=self.MySql_Table_Question_Name,target_field_name=self.__SQL_RightOrError,Target_Value='0')
        self.MySql_Processing(sql)



if __name__ == "__main__":
    sql = MySql()
    #sql.set_Question_RightOrError_By_ID(RightOrError=1,ID=20)

    data = sql.get_Question_Finish_Number()
    if(data!=False):
        print(data)
    pass