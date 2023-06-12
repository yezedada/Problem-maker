class User:
    '用户信息类'
    __m_Account = ''
    __m_Password = ''
    __m_Complete_Questions_Number = 0
    __m_Error_Questions_Number = 0
    __m_Completed_Question_ID = []
    __m_Answer = ''

    def __init__(self,Account=' ',PassWord=' '):
        self.__m_Account = Account
        self.__m_Password = PassWord
    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name,'销毁\n')

    def set_Complete_Questions_Number(self,Complete_Questions_Number):
        self.__m_Complete_Questions_Number = Complete_Questions_Number
    def get_Complete_Questions_Number(self):
        return self.__m_Complete_Questions_Number
    
    def set_Error_Questions_Number(self,Error_Questions_Number):
        self.__m_Error_Questions_Number = Error_Questions_Number
    def get_Error_Questions_Number(self):
        return self.__m_Error_Questions_Number
    
    def get_Account(self):
        return self.__m_Account
    def get_Password(self):
        return self.__m_Password
    def get_Completed_Question_ID(self):
        return self.__m_Completed_Question_ID
    def get_Answer(self):
        return self.__m_Answer
    
    def set_Account(self,Account):
        self.__m_Account = Account
    def set_Password(self,Password):
        self.__m_Password = Password
    def set_Completed_Question_ID(self,id):
        self.__m_Completed_Question_ID.append(id)
    def set_Answer(self,answer):
        self.__m_Answer = answer


