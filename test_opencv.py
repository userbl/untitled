import cv2
#
# print(dir(cv2))
#
# face_patterns = cv2.CascadeClassifier(
#     '/usr/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')
#
# sample_image = cv2.imread('abc2.jpg')
#
# if sample_image.ndim == 3:
#     gray = cv2.cvtColor(sample_image, cv2.COLOR_BGR2GRAY)
# else:
#     gray = sample_image  # if语句：如果img维度为3，说明不是灰度图，先转化为灰度图gray，如果不为3，也就是2，原图就是灰度图
#
# faces = face_patterns.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100))
#
# for (x, y, w, h) in faces:
#     print("find")
#     cv2.rectangle(sample_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
#
# cv2.imwrite('201612_detected.png', sample_image);


def detectFaces(image_name):
    img = cv2.imread(image_name)
    face_cascade = cv2.CascadeClassifier("/usr/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml")
    if img.ndim == 3:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        gray = img #if语句：如果img维度为3，说明不是灰度图，先转化为灰度图gray，如果不为3，也就是2，原图就是灰度图

    faces = face_cascade.detectMultiScale(gray, 1.2, 5)#1.3和5是特征的最小、最大检测窗口，它改变检测结果也会改变
    result = []

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imwrite('201612_detected.png', img);

    for (x,y,width,height) in faces:
        result.append((x,y,x+width,y+height))
    return result


detect_faces = detectFaces("abc2.jpg")
for a in detect_faces :
    print(a)
