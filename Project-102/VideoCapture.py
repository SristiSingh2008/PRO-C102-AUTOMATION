import cv2
import dropbox
import time
import random 

start_time=time.time()
def take_snapshot():
    number=random.randint(0,100)
    #initilizing cv2 
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        img_name="img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time=time.time
        result=False
    return img_name
    print("snap shot taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token="sl.A65bedIvReJpXRSGT0Yq-russ6kpazl6gJyT64mtf9SDzN5pMGblVTa5F-0wRYHaANJUfE3p_aTNh1YoSe6O495QYmiQsMfbRe86-ppKt0OEr2hatiwSafBU7Sh_W5C-7k16CmU"
    file=img_name
    file_from=file
    file_to="/testFolder/"+(img_name)
    dbx=dropbox.Dropbox(access_token)

    with open(file_from,"rb") as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("File uploaded")

def main():
    while(True):
        if((time.time()-start_time)>=5):
            name=take_snapshot()
            upload_file(name)

main()