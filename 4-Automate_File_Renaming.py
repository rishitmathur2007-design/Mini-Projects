import os
# Path to the folder containing the files
folder_path =input("Enter folder path:")
folder_path=folder_path.replace("\"","")
print(folder_path)
folder_path.replace('\\','/')
if not os.path.exists(folder_path):
    print("Error:Folder Not found")
    exit()
pattern=input("Enter Pattern(eg-'File_,image_'):")
file=os.listdir(folder_path)
count=1
for filename in file:
    old_path=os.path.join(folder_path,filename)
    if os.path.isfile(old_path):
        extension=os.path.splitext(filename)[1]
        new_filename=f"{pattern}_{count}{extension}"
        new_path=os.path.join(folder_path,new_filename)
        os.rename(old_path,new_path)
        print(f"Rename:{filename}-->>{new_filename}")
        count+=1
    print("All Files has been Renamed!!")
