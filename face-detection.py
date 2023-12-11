import cv2

face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

group_photo = cv2.imread('group-photo.webp')
grayscale_photo = cv2.cvtColor(group_photo, cv2.COLOR_BGR2GRAY)

# cv2.imwrite('group-photo-grayscale.webp', grayscale_photo)

faces = face_classifier.detectMultiScale(grayscale_photo, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

for face_coords in faces:
    x, y, w, h = face_coords
    cv2.rectangle(group_photo, (x, y), (x + w, y + h), (255, 0, 0))

cv2.imshow('Face Detection', group_photo)

cv2.waitKey(0)
cv2.destroyAllWindows()