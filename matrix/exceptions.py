class MatrixException(Exception):
    pass

class DimensionException(MatrixException):
    def __init__(self, message = "wrong dimensions for operation"):
        self.message = message
        super().__init__(self.message)
        
class InvalidException(MatrixException):
    def __init__(self, message = "not a valid matrix"):
        self.message = message
        super().__init__(self.message)