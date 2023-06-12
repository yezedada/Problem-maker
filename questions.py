class Questions:
    __m_Question = ' ' #问题
    __m_Answer = ' ' #答案
    __m_A = ' ' 
    __m_B = ' ' 
    __m_C = ' ' 
    __m_D = ' ' 
    __m_ID = ' '
    m_FinishOrNot = False #true做了，False未做
    number = 0 #问题总数
    def __init__(self,Question=' ',ID=' ',Answer=' ',A=' ',B=' ',C=' ',D=' '):
        self.__m_Question = Question
        self.__m_Answer = Answer
        self.__m_A = A
        self.__m_B = B
        self.__m_C = C
        self.__m_D = D
        self.__m_ID = ID
        Questions.number += 1

    def get_Question(self):
        return self.__m_Question
    def get_Answer(self):
        return self.__m_Answer
    def get_A(self):
        return self.__m_A
    def get_B(self):
        return self.__m_B
    def get_C(self):
        return self.__m_C
    def get_D(self):
        return self.__m_D
    def get_ID(self):
        return self.__m_ID
    
    def set_Question(self,Question):
        self.__m_Question = Question
    def set_Answer(self,Answer):
        self.__m_Answer = Answer
    def set_FinishOrNot(self,FinishOrNot):
        self.m_FinishOrNot = FinishOrNot


