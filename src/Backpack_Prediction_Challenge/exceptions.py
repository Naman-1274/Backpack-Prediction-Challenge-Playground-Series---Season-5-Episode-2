import sys

def error_details(error, error_details: sys):
    _, _, exc_tb = sys.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    error_message = f"Error: {error} in {filename} at line {exc_tb.tb_lineno}"
    
    return error_message

class exception_handler(Exception):
    def __init__(self,error_message,error_details:sys.exc_info):
        super().__init__(error_message)
        self.error_message = error_details(error_message,error_details=error_details)
        
    def __str__(self):
        return self.error_message

# try:
#     1 / 0
# except Exception as e:
#     raise exception_handler(e, error_details)

    
