import cv2
'''
偵測人臉「內」的眼睛
'''
# 人臉特徵檔
face_cascade = cv2.CascadeClassifier('./xml/haarcascade_frontalface_alt.xml')
# 眼睛特徵檔
eyes_cascade = cv2.CascadeClassifier('./xml/haarcascade_eye.xml')

# 讀檔
frame = cv2.imread('./image/test.jpg')

# 將彩色圖片(RGB)進行灰階(Gray)處理
gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

# face 的座標範圍
faces = face_cascade.detectMultiScale(
    gray,  # 待檢測圖片
    scaleFactor=1.1,  # 檢測粒度(越小越精準(速度慢), 越大越模糊(速度快))
    minNeighbors=5,  # 每個目標至少檢測到幾次成功，才被認定是 face
    minSize=(30, 30),  # 設定數據最小搜尋的尺寸
    flags=cv2.CASCADE_SCALE_IMAGE
)
print(faces)

# 在 face 周圍畫上矩形框
for (x, y, w, h) in faces:
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)  # (0, 0, 255) BGR 顏色, 2 表示框線的寬度

    # 進行眼部偵測
    roi_gray = gray[y:y+h, x:x+w]  # 人臉區域(灰階)
    roi_color = frame[y:y+h, x:x+w]  # 人臉區域(彩色)

    eyes = eyes_cascade.detectMultiScale(
        roi_gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)


# 將 frame 顯示
cv2.imshow('My window', frame)

# 按下任意鍵離開程式
c = cv2.waitKey(0)
print(c)

cv2.destroyAllWindows()

