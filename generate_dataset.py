import os
import cv2
import time
import uuid

IMAGE_PATH = 'CollectedImages'

labels = ['Hello','Yes','No','Thanks','ILoveYou','Please','GoodBye','Sorry']

no_of_images = 20

for label in labels:
    image_path = os.path.join(IMAGE_PATH,label)
    os.makedirs(image_path,exist_ok=True)
    cap = cv2.VideoCapture(0)
    print(f'Collecting Images for {label}')
    time.sleep(5)    
    for img_num in range(no_of_images):
        ret,frame = cap.read()
        # image_name = os.path.join(IMAGE_PATH,label,label+'.'+f'{str(uuid.uuid1())}.jpg')
        image_name = os.path.join(IMAGE_PATH,label,label+'_'+f'{img_num}.jpg')
        cv2.imwrite(image_name,frame)
        cv2.imshow(f'frame: {label}',frame)
        time.sleep(2)
        
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break;
    cap.release()