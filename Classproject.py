import os
import shutil

#creating a function that gets a file path and split the file name from the extention
def split_extention(directory1):
   filename, extension = os.path.splitext(directory1)
   return extension.lower()[1:]

def categorize_by_extension(directory):
   category_folders = {}
   for filename in os.listdir(directory):
      filepath = os.path.join(directory, filename)
      if os.path.isfile(filepath):
         extension = split_extention(filepath)
      
         if extension:
            category_folder = os.path.join(directory, f"{extension}_files")
            if not os.path.exists(category_folder):
               os.makedirs(category_folder)
            category_folders[extension] = category_folder
         if extension:
            shutil.move(filepath, category_folders[extension])


def main_file_organizer(directory):
   """
 Creates folders within a directory using the name the folders and move moves the files to their respective folders.

 Args:
    a folder directory

 Use fuctions for all smaller processes
 create a folder
 add files to existing folder
   """
   try:
      categorize_by_extension(directory)
      print(f"Folders created and files moved with 'extension_file' format in '{directory}'.")
   except:
      pass
main_file_organizer("C:\\Users\\BBS INFO\\Desktop\\Project_Test_folder - Copy")