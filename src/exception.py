import sys
from src.logger import logging

def error_message_detail(error:str,error_detail:sys):
    '''
    Returns in detail message of the custom error.
    '''
    _,_,error_tb = error_detail.exc_info()
    file_name = error_tb.tb_frame.f_code.co_filename
    line_no = error_tb.tb_frame.f_lineno
    error_message = "Error occured in python script name {0} line number {1}: {2}".format(
        file_name,
        line_no,
        error
    )
    return error_message

class CustomException(Exception):
    def __init__(self, message:str, error:sys):
        super().__init__(message)
        self.error_message = error_message_detail(message, error)

    def __str__(self):
        return self.error_message
    
def cause_error():
    return 10 / 0

if __name__ == "__main__":
    try:
        cause_error()
    except Exception as e:
        logging.info("Divided by zero")
        raise CustomException(e,sys)