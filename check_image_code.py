import pytesseract
from PIL import Image
#!/usr/bin/python3
# coding=UTF-8
import requests
from urllib.request import urlretrieve

# requests.get('http://192.168.9.6:8080/eedu_base/c_authImg.do')

# urlretrieve('http://192.168.9.6:8080/eedu_base/c_authImg.do', "code.jpg")
# with open('code.jpg', 'wb') as file:
#     file.write(requests.content)


def initTable(threshold=140):
 table = []
 for i in range(256):
     if i < threshold:
         table.append(0)
     else:
         table.append(1)

 return table


image = Image.open('aabb.jpg')
image = image.convert('L')
binaryImage = image.point(initTable(), '1')
binaryImage.show()
print(pytesseract.image_to_string(binaryImage, config='-psm 6'))
# vcode = pytesseract.image_to_string(image)
# print ("codew:"+vcode)
