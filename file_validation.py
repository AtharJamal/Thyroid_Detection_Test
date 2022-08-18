import json
import os,re,pandas as pd
import shutil
from column_validation import no_column_check
from logger import Application_logger

class validation_tests:

    def __init__(self):
        self.log=Application_logger()
        self.folder = os.listdir("Training_Batch_Files_Athar/")
        self.correct_file_path=("Correct_Files/")
        self.wrong_file_path=("Wrong_Files/")

    def file_name_test(self):
        regex = "['\bhypothyroid']+[\w]+[\d]+[\w]+[\d]+[\.csv]"
        self.log.logger_entry("log_new","Starting number of columns check"+"\n")
        for files in self.folder:
            if re.match(regex,files):
                self.log.logger_entry("log_new",f"It's a match for {files}"+"\n")
                self.log.logger_entry("log_new",f"Moving {files} in Correct_Files Directory"+"\n")
                shutil.move("Training_Batch_Files_Athar/"+files, self.correct_file_path)
            else:
                self.log.logger_entry("log_new",f"File name for {files} not as per standard"+"\n")
                self.log.logger_entry("log_new",f"Moving {files} in Wrong_Files Directory" + "\n")
                shutil.move("Training_Batch_Files_Athar/"+files, self.wrong_file_path)

    def column_length_checks(self):
        self.log.logger_entry("log_new","About to perform columns check"+"\n")
        for files in os.listdir("Correct_Files"):
            path_correct_files=(self.correct_file_path+"/"+files)
            df=pd.read_csv(path_correct_files)
            col_check_obj=no_column_check()
            if (len(df.columns)==col_check_obj[2]):
                self.log.logger_entry("log_new",f"{files} : have {len(df.columns)} columns and is acceptable"+"\n")
                if(len(files.split("_")[1])==col_check_obj[1]):
                    self.log.logger_entry("log_new",f"{files} : have length of 7 for datestamp and is acceptable"+"\n")
                    if ((len((files.split("_")[2]).split(".csv")[0]))==col_check_obj[0]):
                        self.log.logger_entry("log_new",f"{files} : have length of 13 for timestamp and is acceptable" + "\n")
                    else:
                        self.log.logger_entry("log_new",f"{files} : does not have the length of 13 for timestamp and is not acceptable" + "\n")
                        shutil.move(path_correct_files, self.wrong_file_path)
                else:
                    self.log.logger_entry("log_new",f"{files} : does not have the length of 7 for datestamp and is not acceptable" + "\n")
                    shutil.move(path_correct_files,self.wrong_file_path)
            else:
                self.log.logger_entry("log_new",f"{files} : have {len(df.columns)} columns and is not acceptable"+"\n")
                shutil.move(path_correct_files,self.wrong_file_path)
                self.log.logger_entry("log_new",f"{files} moved to Wrong_Files Directory"+"\n")

    def column_name_checks(self):
        with open("schema.json","r") as f:
            data=json.load(f)
            col_name=data["ColName"]
        for files in os.listdir(self.correct_file_path):
            path=self.correct_file_path +"/"+ files
            df = pd.read_csv(path)
            for key in col_name:
                for column in df.columns:
                    if (column == key):
                        break
                    else:
                        print("Test_else")
                        # self.log.logger_entry("log_new",f"{column} of {files} is not in schema"+"\n")
                        # shutil.move(path,self.wrong_file_path)
                        # self.log.logger_entry("log_new", f"{files} moved to wrong folder" + "\n")
                        # break

            self.log.logger_entry("log_new", f"{files} passed column name check" + "\n")

            # col=no_column_check()
            # print(len(df.columns))
            # if (len(df.columns)==col[2]):
            #     print(files)
            # else:
            #     pass






# col_val_obj=column_validation.no_column_check()
# print(col_val_obj[0])


if __name__ == '__main__':
    v=validation_tests()
    (v.column_name_checks())

