import idkbro 

path = input("Enter File Path: ")
FolderName = input("Enter Folder Name: ")
path= (path.replace("\\","/")+"/"+FolderName+"/")                #merges path and foldername and converts to library readable type
print("Path for the Folder =>", path )

idkbro.convdel(path, FolderName)   