from copy import deepcopy

Direction = []

class Folder:  
    def __init__(self,name,dad=None):
        self.name = name
        self.content_folders = []
        self.content_files = []
        self.addr = None
        self.dad = dad# object fother
       
    def remove_folder(self,folder):
        self.select = None
        
        for i in self.content_folders:
            if i.get_name() ==folder:
                # print('Founded')
                self.select = i
                break
        if self.select:
            self.content_folders.remove(self.select)
            self.select = None
            # print('pak shod')
            # print(self.content_folders)
            return
        print('Folder Does Not Exist')
        
    def change_name(self,new_name):
        self.name = new_name
    def add_folder(self,folder_object):
        self.content_folders.append(folder_object)
    def  add_file(self,file_object):
        self.content_files.append(file_object)
    def get_name(self):
        return self.name
    def remove_file(self,file_name):
        self.selected_file = None
        for i in self.content_files:
            if i.get_name() == file_name:
                self.selected_file = i
        if self.selected_file:
            self.content_files.remove(self.selected_file)
            self.selected_file = None
            return
        print('File Does Not Exist')
    #return list of object files
    def return_file_objects(self):
        return self.content_files
    
    #return list of object folders
    def return_folder_objects(self):
        return self.content_folders
    def get_dad_name(self):
        return self.dad.get_name()
    def get_dad_object(self):
        return self.dad

class File:
    def __init__(self,name):
        self.name = name
        self.text = []
        self.addr = None
        
    def change_name(self,new_name):
        self.name = new_name

    def get_name(self):
        return self.name
    def change_data(self,data_):
        self.text = data_
    def get_text(self):
        return self.text
root = Folder('root')
folder_object = root#selected object folder

#creat new object from folder
def creat_new_folder(folder_name):
    if folder_name in [i.get_name() for i in folder_object.return_folder_objects()]:
        print('Folder Already Exists')
        return 
    new_folder = Folder(folder_name,dad=folder_object)
    folder_object.add_folder(new_folder)
    # print('Folder Added')# here we need remove
    # print('/'.join(Direction))


#change direction
def change_directory(folder_name):
    global folder_object
    if folder_name =='..':
        if folder_object.get_name()=='root':
            # print('we are in root') #remove here we need
            return 
        else:
            folder_object = folder_object.get_dad_object()
            Direction.pop()
            # print('/'.join(Direction))
    else:
        for object_folder in folder_object.return_folder_objects():
            if object_folder.get_name() == folder_name:
                Direction.append('/'+object_folder.get_name())
                # print(object_folder.get_name())
                folder_object = object_folder
                # print('changed directory..')
                # print('/'.join(Direction))
                return
        print('Folder Does Not Exist')
def show_pwd():
    if len(Direction) ==0:
        print('/')
        return
    print(''.join(Direction))
def show_ls():
    folder_datas = sorted(i.get_name() for i in folder_object.return_folder_objects())
    [print(f'++ {i}') for i in folder_datas]
    file_datas = [i.get_name() for i in folder_object.return_file_objects()]
    [print(i) for i in file_datas]
def creat_file(file_name_):
    for i in folder_object.return_file_objects():
        if i.get_name() == file_name_:
            print('File Already Exists')
            return
    f_ob = File(file_name_)
    folder_object.add_file(f_ob)

def edit_file(fil_name_):
    for i in folder_object.return_file_objects():
        if i.get_name() == fil_name_:
            ins = []
            while True:
                data_to_write = input()
                if data_to_write =='q!':
                    if len(ins) ==0:
                        return
                    i.change_data(ins)
                    return
                ins.append(data_to_write)
        
    print('File Does Not Exist')
def print_data_file(file_name_):
    for i in folder_object.return_file_objects():
        if i.get_name() == file_name_:
            data = i.get_text()
            if len(data) == 0:
                return
            print(*data,sep='\n')
            return
    print('File Does Not Exist')

def change_filename(source, new_filename):
    for i in folder_object.return_file_objects():
        if i.get_name() == source:
            i.change_name(new_filename)
            return

    print('File Does Not Exist')

#rmove commands
def rmdir(fo_name_):
    # global folder_object
    # print(fo_name_)
    folder_object.remove_folder(fo_name_)
def rm(fi_name_):
    folder_object.remove_file(fi_name_)


#agar kam shod bege file to poshe maghsad hast
def mv(sourse,det):
    select_source = None
    for i in folder_object.return_file_objects():
        # print(i.get_name())
        if sourse == i.get_name():
            select_source = i
            # print('shod')
            break
    if select_source == None:
        print('File Does Not Exist')
        return
    if det =='..':
        if folder_object.get_name() == 'root':
            print('Folder Does Not Exist')
            return
        else:
            dadi = folder_object.get_dad_object()
            dadi.add_file(select_source)
            folder_object.remove_file(select_source)
            return
    #find folder
    for ob in folder_object.return_folder_objects():
        if ob.get_name() == det:
            ob.add_file(select_source)#copy file from source
            folder_object.remove_file(sourse)#remove file from source
            return
    print('Folder Does Not Exist')
    return
    # if folder_object.get_name() == 'root':
    #     print('Folder Does Not Exist')
    #     return

    # ob_dad = folder_object.get_dad_object()
    
    # while True:
    #     # print(f'start')
    #     for ob in ob_dad.return_folder_objects():
    #         if ob.get_name() == det:
    #             ob.add_file(select_source)#copy file from source
    #             folder_object.remove_file(sourse)#remove file from source
    #             return
    #     if ob_dad.get_name() == "root":
    #         print('Folder Does Not Exist')
    #         return   
    #     ob_dad = ob_dad.get_dad_object()
def cp(sourse,det):
    select_source = None
    for i in folder_object.return_file_objects():
        # print(i.get_name())
        if sourse == i.get_name():
            select_source = i
            # print('shod')
            break
    if select_source == None:
        print('File Does Not Exist')
        return
    if det =='..':
        if folder_object.get_name() == 'root':
            print('Folder Does Not Exist')
            return
        else:
            dadi = folder_object.get_dad_object()
            dadi.add_file(deepcopy(select_source))
            # folder_object.remove_file(select_source)
            return
    #find folder
    for ob in folder_object.return_folder_objects():
        if ob.get_name() == det:
            ob.add_file(deepcopy(select_source))#copy file from source
            # folder_object.remove_file(sourse)#remove file from source
            return
    print('Folder Does Not Exist')
    return
    # if folder_object.get_name() == 'root':
    #     print('Folder Does Not Exist')
    #     return

    # ob_dad = folder_object.get_dad_object()
    
    # while True:
    #     # print(f'start')
    #     for ob in ob_dad.return_folder_objects():
    #         if ob.get_name() == det:
    #             ob.add_file(deepcopy(select_source))#copy file from source
    #             return
    #     if ob_dad.get_name() == "root":
    #         print('Folder Does Not Exist')
    #         return   
    #     ob_dad = ob_dad.get_dad_object()


while True:
    command = input().split()
    if command[0] =='mkdir':
        creat_new_folder(command[1])
    elif command[0] =='cd':
        change_directory(command[1])
    elif command[0] =='ls':
        show_ls()
    elif command[0] =='pwd':
        show_pwd()
    elif command[0] =='touch':
        creat_file(command[1])
    elif command[0] =='vi':
        edit_file(command[1])
    elif command[0] =='cat':
        print_data_file(command[1])
    elif command[0] =='rn':
        change_filename(command[1], command[2])
    elif command[0] =='rmdir':
        rmdir(command[1])
    elif command[0] =='rm':
        rm(command[1])
    elif command[0] =='mv':
        mv(command[1], command[2])
    elif command[0] =='cp':
        cp(command[1], command[2])
    elif command[0] =='exit':
        break
    else:
        print('Invalid Command')
