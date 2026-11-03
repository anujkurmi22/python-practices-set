'''1 . read 
2 write 
3 append
4 delete
there are the operations which we can perform on the file handling'''
# import os
# #create folder --> anuj("path\\folderName")
# name ="c:\\Users\\admin\\Desktop\\Infoviaan.PY\\anuj"
# if os.path.exists(name):
#     print("Folder already exists")
# else:
#     os.makedirs(name)
#     print("Folder created successfully")

'''file creation ==> there are 2 ways to create a file
1. open("path\\filename.ext","x") --> x for creating new file ''' 
# #file creation -- open("path\\filename.ext","x") --> x for creating new file
# fileName = "D:\\Users\\Anuj\\Documents\\babubushai\\krishnajanmastmi.txt"
# open(fileName,"x")
# print("File created successfully")

#data writing -- open("path\\filename.ext","w") --> w for writing data into file


# import os
# fileName = "c:\\Users\\admin\\Desktop\\Infoviaan.PY\\anuj\\anuj.txt"
# fl = open(fileName,"w")
# fl.write("my name is anuj")
# fl.write("\nI am from India")
# fl.write("\nI am a software engineer")
# fl.write("\n I am studying in btech")
# fl.close()
# print("Data written successfully")


#data appen\d -- open("path\\filename.ext","a") --> a for appending data into file
# fileName = "c:\\Users\\admin\\Desktop\\Infoviaan.PY\\anuj\\radhe.txt"
# fl = open(fileName,"a")
# fl.write("\n my name is anuj kurmi")
# fl.write("\n i am from india")
# fl.write("\n i am a software engineer")
# fl.write("\n i am studying in btech")
# fl.write("\n i am a student of infoviaan")
# fl.write("\n do you want to learn python")
# print("Data appended successfully")


'''data reading ==> there are 3 ways to read data from file
1. read() --> read all data from file
2. readline() --> read one line at a time from file
3. readlines() --> read all lines from file and return as list of lines
'''
# data reading -- open("path\\filename.ext","r") --> r for reading data from file
import os


# fileName = "c:\\Users\\admin\\Desktop\\Infoviaan.PY\\anuj\\radhe.txt"
# fl = open(fileName,"r")
# data = fl.read()
# print(data)
# fl.close()


'''file deletion ==> there are 2 ways to delete a file
1. os.remove("path\\filename.ext") --> remove file from directory
2. os.rmdir("path\\folderName") --> remove folder from directory
'''
# os.remove("c:\\Users\\admin\\Desktop\\Infoviaan.PY\\anuj\\radhe.txt")

# os.rmdir("c:\\Users\\admin\\Desktop\\Infoviaan.PY\\anuj")

'''file renaming ==> there are 2 ways to rename a file
1. os.rename("path\\oldfilename.ext","path\\newfilename.ext") --> rename file
2. os.rename("path\\oldfoldername","path\\newfoldername") --> rename folder'''

# os.rename("c:\\Users\\admin\\Desktop\\Infoviaan.PY\\anuj\\radhe.txt","c:\\Users\\admin\\Desktop\\Infoviaan.PY\\anuj\\radhe.txt")
# print("file rename succecssfully")

'''reading'''
# x= open("c:\\Users\\admin\\Desktop\\Infoviaan.PY\\anuj\\radhe.txt","r")
# for i in x:
#     print(i)


'''with read() ---> there are most used method to read data from file'''
# with open("c:\\Users\\admin\\Desktop\\Infoviaan.PY\\anuj\\radhe.txt","r") as f:
#     print(f.read())

'''with write()'''
# with open("c:\\Users\\admin\\Desktop\\Infoviaan.PY\\anuj\\about100.txt","w") as f:
#     f.write("my name is anuj kurmi")
#     f.write("\n i am from india")
#     f.write("\n anuj singhgour")
#     f.write("\n i am studying in btech")
#     f.write("\n i am a student of infoviaan")
#     f.write("\n do you want to learn python")
#     print("file written successfully")

'''user input() to write data into file'''
# with open("c:\\Users\\admin\\Desktop\\Infoviaan.PY\\anuj\\about100.txt","w") as f:
#     while True:
#         data = input("enter the data to write into file (type 'exit' to stop): ")
#         if data == "exit":
#             break
#         f.write(data)
#         f.write("\n")
# print("done ✔")
'''copy paste file from one location to another location'''
# src = "c:\\Users\\admin\\Desktop\\Infoviaan.PY\\anuj\\about100.txt"
# dest = "c:\\Users\\admin\\Desktop\\Infoviaan.PY\\anuj\\about100_copy2.txt"
# with open(src,"r") as f:
#     data = f.read() 


# with open(dest,"w") as f:
#     f.write(data)
# print("file copied successfully")


'''move file from one location to another location'''
# import shutil
# shutil.copy("c:\\Users\\admin\\Desktop\\Infoviaan.PY\\anuj\\about100.txt","c:\\Users\\admin\\Desktop\\Infoviaan.PY\\anuj\\about100_copy2.txt")


'''
***wlcome to my software***
enter 1 for create folder
enter 2 for delete folder
enter 3 for copy folder
enter 4 for creat folder
enter 5 for delete file
enter 6 for copy file
enter 7 for data from a file 
enter 8 for data writing into a file
enter 9 for move the file 
enter 10 for exit from the software

'''
'''
import os
import shutil


def main():
    while True:
        print("\n*** welcome to my software ***")
        print("enter 1 for create folder")
        print("enter 2 for delete folder")
        print("enter 3 for copy folder")
        print("enter 4 for create file")
        print("enter 5 for delete file")
        print("enter 6 for copy file")
        print("enter 7 for data from a file")
        print("enter 8 for data writing into a file")
        print("enter 9 for move the file")
        print("enter 10 for exit from the software")

        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number from 1 to 10.")
            continue

        try:
            if choice == 1:
                folder_name = input("Enter the folder name to create: ")
                if os.path.exists(folder_name):
                    print("Folder already exists.")
                else:
                    os.makedirs(folder_name)
                    print("Folder created successfully.")

            elif choice == 2:
                folder_name = input("Enter the folder name to delete: ")
                if os.path.exists(folder_name):
                    # Removes directory along with all its contents safely
                    shutil.rmtree(folder_name)
                    print("Folder deleted successfully.")
                else:
                    print("Folder does not exist.")

            elif choice == 3:
                src_folder = input("Enter the source folder path: ")
                dest_folder = input("Enter the destination folder path: ")
                shutil.copytree(src_folder, dest_folder)
                print("Folder copied successfully.")

            elif choice == 4:
                file_name = input("Enter the file name to create: ")
                open(file_name, "x").close()
                print("File created successfully.")

            elif choice == 5:
                file_name = input("Enter the file name to delete: ")
                if os.path.exists(file_name):
                    os.remove(file_name)
                    print("File deleted successfully.")
                else:
                    print("File does not exist.")

            elif choice == 6:
                src_file = input("Enter the source file path: ")
                dest_file = input("Enter the destination file path: ")
                shutil.copy(src_file, dest_file)
                print("File copied successfully.")

            elif choice == 7:
                file_name = input("Enter the file name to read data from: ")
                with open(file_name, "r") as f:
                    data = f.read()
                    print("\n--- File Content ---")
                    print(data)

            elif choice == 8:
                file_name = input("Enter the file name to write data into: ")
                with open(file_name, "a") as f:  # Using 'a' mode appends instead of overwriting
                    while True:
                        data = input(
                            "Enter the data to write into file (type 'exit' to stop): "
                        )
                        if data.lower() == "exit":
                            break
                        f.write(data + "\n")
                print("Data written successfully.")

            elif choice == 9:
                src_file = input("Enter the source file path: ")
                dest_file = input("Enter the destination file path: ")
                shutil.move(src_file, dest_file)
                print("File moved successfully.")

            elif choice == 10:
                print("Exiting the software.")
                break

            else:
                print("Invalid choice! Please select an option between 1 and 10.")

        except FileNotFoundError:
            print("Error: The specified file or folder was not found.")
        except FileExistsError:
            print("Error: A file or folder with that name already exists.")
        except PermissionError:
            print("Error: Permission denied for this operation.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main() '''


#file copy from one location to another location
# import os
# import shutil
# source = input("Enter source file path: ")
# dest = input("Enter destination file path: ")
# # shutil.copytree(source, dest)
# shutil.move(source, dest)
# print("file moved successfully")
