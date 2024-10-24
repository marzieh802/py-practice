import os
import shutil

if (__name__ == "__main__"):
    path = os.getcwd()
    # print("path: ",path)

    list_dir = os.listdir()
    # print("list_dir",list_dir)

    # path_return = shutil.move("test3333.txt","/media/h3m/New Volume/Learning/py-practice")
    # print(path_return)

    try:
        os.unlink(os.getcwd()+"/test_del.py")
    except FileNotFoundError:
        print("error")

    # os.rmdir(os.getcwd()+"/test_f")

    # shutil.rmtree(os.getcwd()+"/testtt")

    # print(os.walk("/media/h3m/New Volume/Learning/py-practice"))

    # os.rename(os.getcwd() + "/TopFolder/mid-folder1",
    #           os.getcwd() + "/mid-folder1-test")

    for folder, sub_folders, files in os.walk(os.getcwd()+"/TopFolder"):
        print("folder", folder)
        for sub_folder in sub_folders:
            print("\tsubfolder", sub_folder)
        for file in files:
            print("\tfile", file)

    shutil.move(os.getcwd()+"/TopFolder/mid-folder2",
                "/media/h3m/New Volume/Learning/py-practice")
    shutil.move("/media/h3m/New Volume/Learning/py-practice/mid-folder2",
                os.getcwd()+"/TopFolder")
