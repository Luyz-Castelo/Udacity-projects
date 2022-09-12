import os

def rename_files():
  file_list = os.listdir(r'C:\Udacity projects\Rename_Files\files')
  saved_path = os.getcwd()
  os.chdir(r'C:\Udacity projects\Rename_Files\files')
  for file_name in file_list:
    os.rename(file_name, ''.join([i for i in file_name if not i.isdigit()]))
  os.chdir(saved_path)
  
rename_files()