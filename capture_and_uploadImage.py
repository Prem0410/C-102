import cv2
import dropbox
import time
import random

start_time = time.time()

def take_snapshot():
    number = random.randint(0,100)
    
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        
        ret,frame = videoCaptureObject.read()
        
        img_name = "img"+str(number)+".png"
        cv2.imwrite(img_name, frame)
        start_time = time.time
        result = False
    return img_name
    print("snapshot taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()
    
def upload_file(img_name):
    access_token = "sl.A_0wQwl2tvT3K51eHh8PBLjAzjFRUhdDk1TwcYX1oGZ0cj8q3PG01bcBR8oMWciT0t87S8XYKZA2mTPhSNgVA9SCJwUtMgTZbxokrN9-IAa2X854b6YnCI3_kMUmaQTCAZSKKHM"
    file = img_name
    file_from = file
    file_to = "/testFolders/"+(img_name)
    dbx = dropbox.Dropbox(access_token)
    
    with open(file_from, 'rb') as f:
        dbx.file_upload(f.read(), file_to,mode=dropbox.file.WriteMode.overwrite)
        print("file uploaded")
        
def main():
    while(True):
        if ((time.time() - start_time) >= 5):
            name = take_snapshot()
            upload_file(name)
            
main()
        
        