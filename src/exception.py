import sys
import logging
from src.logger import logging

'''
error_message_detail function is preparing how will the error be shown with the help of 
Custom Exception 
'''

def error_message_detail(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = 'Error occured in python script name [{0}] line number [{1}] error message [{2}]'.format(
        file_name, exc_tb.tb_lineno,str(error))

    return error_message

class CustomException(Exception):
    '''
    Custom Exception is inheriting the parent Exception class 
    super.init is overriding the init method of parent class with error message parameter
    '''
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_detail=error_detail)

    '''
    Whenever we will try to print/raise the exception, it will print the error message
    '''
    def __str__(self):  
        return self.error_message
    