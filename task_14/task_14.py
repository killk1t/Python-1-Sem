class log_operation:
    def __init__(self, filename, operation):
        self.filename = filename
        self.operation = operation
    def __enter__(self):
        with open(self.filename, 'a', encoding = 'utf-8') as f:
            print(f"START: {self.operation}", file = f)
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        with open(self.filename, 'a', encoding = 'utf-8') as f:
            if exc_type == None:
                print(f"END: {self.operation}", file = f)
            else:
                print("ERROR: Data processing", file = f)
                return False
with log_operation('operation.log', 'Data processing'):
    pass
try:
    with log_operation('operation.log', 'Datadatadata'):
        raise ValueError("testing")
except ValueError:
    print('Исключение распространилось далее')