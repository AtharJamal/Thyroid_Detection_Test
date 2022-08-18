import datetime
class Application_logger:
    def __init__(self):
        pass

    def logger_entry(self,file,message):
        self.file = file
        self.message = message


        with open(self.file,"a+") as f:
            f.write((datetime.datetime.now().strftime("%H:%M:%S"))+" - "+(datetime.datetime.now().strftime("%d/%m/%Y"))+"\t"+self.message)
