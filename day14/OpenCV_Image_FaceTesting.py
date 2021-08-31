import cv2

# 人臉特徵檔
face_cascade = cv2.CascadeClassifier('./xml/haarcascade_frontalface_alt.xml')

# 讀檔
frame = cv2.imread('./image/test.jpg')

# 將 frame 顯示
cv2.imshow('My window', frame)

# 按下任意鍵離開程式
c = cv2.waitKey(0)
print(c)

cv2.destroyAllWindows()

