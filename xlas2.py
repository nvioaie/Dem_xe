import cv2

# Load pre-trained vehicle classifier (Haar cascade)
car_cascade = cv2.CascadeClassifier('D:/Python/haarcascade_car.xml')

# Open video file
cap = cv2.VideoCapture('D:/Python/xla/istockphoto-2162705126-640_adpp_is.mp4')

vehicle_count = 0

# Tạo cửa sổ mới với tên tùy ý
cv2.namedWindow('My Video Window', cv2.WINDOW_NORMAL)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    vehicles = car_cascade.detectMultiScale(gray, 1.1, 2)

    for (x, y, w, h) in vehicles:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    vehicle_count += len(vehicles)

    # Hiển thị lên cửa sổ mới
    cv2.imshow('My Video Window', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print(f'Tổng số phương tiện phát hiện: {vehicle_count}')
cap.release()
cv2.destroyAllWindows()