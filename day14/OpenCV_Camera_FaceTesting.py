import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)   # 1024, 800, 640, 320
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  #  768, 600, 480, 240

while True:
    ret, frame = cap.read()
    if(ret == True):
        print(ret, frame)
    # 顯示影像
    cv2.imshow('Tuan', frame)
    # 按下 q 離開迴圈
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
