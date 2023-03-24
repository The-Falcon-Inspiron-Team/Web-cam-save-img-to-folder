import cv2

cam = cv2.VideoCapture(0)  # "image/Video.mp4"

cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    imgresize = cv2.resize(frame,(50,50))

    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if cv2.waitKey(1) == ord('f'): 
        print("Escape hit, closing...")
        break
    elif cv2.waitKey(1) == ord('s'): 

        
        img_name = "PICTURE/Face_data_{}.jpg".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()