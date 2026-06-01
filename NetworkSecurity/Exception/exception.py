import sys
from NetworkSecurity.Custom_logging import logger

class NetworkSecurityException(Exception):
    def __init__(self, error_message: str, error_detail: sys):
        super().__init__(error_message)
        self.error_message = self.get_detailed_error_message(error_message=error_message, error_detail=error_detail)
        
    @staticmethod
    def get_detailed_error_message(error_message: str, error_detail: sys) -> str:
        _, _, exc_tb = error_detail.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
        detailed_error_message = f"Error occurred in script: {file_name} at line number: {line_number}. Error message: {error_message}"
        return detailed_error_message
    
    def __str__(self):
        return self.error_message


# if __name__ == "__main__":
#     try:
#         logger.logging.info("Testing NetworkSecurityException...")
#         a = 1 / 0
        
#     except Exception as e:
#         network_security_exception = NetworkSecurityException(error_message=str(e), error_detail=sys)
#         print(network_security_exception)