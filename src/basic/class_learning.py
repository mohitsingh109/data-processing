class DataProcessing:
    def __init__(self, data, version="0.1"):
        self.data = data
        self.version = version
        self.__result = "None"

    def set_result(self, result):

        self.__result = result

    def get_result(self):
        return self.__result

    @staticmethod # annotation for static method
    def calculate():
        return 10 + 12

    @staticmethod
    def clean_up(data):
        print("Performing cleanup...")

def calculate():
    return 10 + 12

data_processing = DataProcessing(data=["Mohit", "Ram"], version="1.0")
print(data_processing.data)
print(data_processing.version)
print(data_processing.get_result())
data_processing.set_result("Success")
print(data_processing.get_result())

data_processing1 = DataProcessing(["123", "456"])
print(data_processing1.data)
print(data_processing1.version)

print(DataProcessing.calculate())