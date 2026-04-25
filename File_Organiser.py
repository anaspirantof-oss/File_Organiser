import os, shutil
var = '\\'

def check(filepath, file_ext):

    if os.path.exists(f"{filepath}{var}{file_ext}"): return True
    else : 
        os.mkdir(f"{filepath}{var}{file_ext}")
        return True


def ftype(file):
        file_ext = "." + file.split(sep=".")[-1].lower()
        match file_ext :
            case ".jpg"|".jpeg"|".png"|".gif"|".bmp"|".svg"|".webp"|".ico"|".psd" : return "Image"
            case ".pdf"|".doc"|".docx"|".txt"|".rtf"|".xls"|".xlsx"|".csv"|".ppt"|".pptx"|".epub" : return "Document"
            case ".mp3"|".wav"|".aac"|".flac"|".m4a"|".wma" : return "Audio"
            case ".mp4"|".mkv"|".mov"|".avi"|".wmv"|".flv" : return "Video"
            case ".py"|".cpp"|".c"|".java"|".js"|".html"|".css"|".sql"|".json"|".xml" : return "Program"
            case ".zip"|".rar"|".7z"|".tar"|".gz" : return "Zip"
            case ".exe"|".msi"|".bat"|".sh"|".dll"|".sys"|".ini"|".log"|"lnk" : return "Executable"
            case ".image"|".document"|".audio"|".video"|".program"|".zip"|".executable"|".folder"|".sysfolder" : return "SysFolder"
            case _ : return "Folder"

def working(folderpath):
    files = os.listdir(folderpath)
    for i in files :
        ftypen = ftype(i)
        if not ftypen == "SysFolder" :
            if check(f"{folderpath}",ftypen) is True :
                shutil.move(f"{folderpath}{var}{i}",f"{folderpath}{var}{ftypen}")
            else : print("Permissions Required !!! ")

def main():
    print("This is File Organiser 1.0")
    while True:
        input("Press Enter To Start...")

        folderpath = input("Enter the Directory Path (Leave For Current Directory) : ")
        

        if folderpath :

            if os.path.exists(folderpath):

                if not os.access(folderpath, os.W_OK):
                    print(f"Sorry I Dont Have The Permissions To Write in The Directory {folderpath}.")

                Items = os.listdir(folderpath)

                for i in Items:
                    if not os.access(folderpath+var+i, os.W_OK):
                        print("Sorry I Dont Have The Permissions To Write In This File")
                        
                working(folderpath)
                print("Successful !")
                if input("End?? (enter y)").lower() == 'y':
                    print("Ok Bye! :)")
                    break
            else:
                print("Directory Doesnt Exists ! ")
                input("Press Enter To Continue. ")
        else:
            folderpath = os.curdir()

            if not os.access(folderpath, os.W_OK):
                print(f"Sorry I Dont Have The Permissions To Write in The Directory {folderpath}.")

            Items = os.listdir(folderpath)

            for i in Items:
                if not os.access(folderpath+var+i, os.W_OK):
                    print("Sorry I Dont Have The Permissions To Write In This File")

            working(folderpath)
            print("Successful !")
            if input("End?? (enter y)").lower() == 'y':break

main()


