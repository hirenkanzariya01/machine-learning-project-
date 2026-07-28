import sys

def GetErrorDetails(error, error_details: sys):
    _, _, tb_obj = error_details.exc_info()
    Line_number = tb_obj.tb_lineno
    File_name = tb_obj.tb_frame.f_code.co_filename

    error_message = f"Error occurred in Line Number :- {Line_number}, Error occurred in File Name :- {File_name} , Error Message {error}"

    return error_message

class CustomeException(Exception):
    def __init__(self, error, error_message: sys):
        super().__init__(error_message)
        self.error_message = GetErrorDetails(error, error_message)

    def __str__(self):
        return self.error_message
