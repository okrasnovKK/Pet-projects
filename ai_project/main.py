# import cv2
# # import numpy as np
#
#
# #          The first lesson
# #
# #
# #
# # #
# img = cv2.imread('images/car_1.jpg')
# # #
# # img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))
# # img = cv2.GaussianBlur(img, (9, 9), 0)   ## размытие
# # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  ## преобразование цвета в ч/б
# #
# # img = cv2.Canny(img, 200, 200)  ## нахождение углов, приведение картинки в бинарный формат
# #
# # kernel = np.ones((5, 5), np.uint8)
# # img = cv2.dilate(img, kernel, iterations=1)
# #
# # img = cv2.erode(img, kernel, iterations=1)
# #
# cv2.imshow('Result', img)
# # #
# # print(img.shape)
# #
# cv2.waitKey(0)
# #
# # # cap = cv2.VideoCapture(0)
# # # cap.set(3, 500)
# # # cap.set(4, 300)
# # #
# # # while True:
# # #     success, img = cap.read()
# # #     cv2.imshow('Result', img)
# # #
# # #     if cv2.waitKey(1) & 0xFF == ord('q'):
# # #         break
#
#
# ##          The third lesson
#
# # photo = np.zeros((300, 300, 3), dtype='uint8')
# #
# # photo[100:150, 100:150] = 9, 237, 41
# #
# # cv2.rectangle(photo, (50, 50), (100, 100), (9, 237, 41), thickness=cv2.FILLED)
# #
# # cv2.line(photo, (0, photo.shape[0] //2), (photo.shape[1], photo.shape[1] // 2), (9, 237, 41), thickness=10)
# #
# # cv2.circle(photo, (photo.shape[1] // 2, photo.shape[0] // 2), 50, (9, 237, 41), thickness = cv2.FILLED)
# #
# # cv2.putText(photo, 'Result', (120, 50), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 0, 0), 1)
# #
# # cv2.imshow('Photo', photo)
# # cv2.waitKey(0)
#
#
# ##          The fourth lesson
#
# # Work with video
#
# # import cv2
# # import numpy as np
# #
# #
# # cap = cv2.VideoCapture('videos/video_1.mp4')
# #
# #
# # while True:
# #     success, img = cap.read()
# #
# #     # img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))
# #     img = cv2.GaussianBlur(img, (9, 9), 0)  ## размытие
# #     img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  ## преобразование цвета в ч/б
# #
# #     img = cv2.Canny(img, 30, 30)  ## нахождение углов, приведение картинки в бинарный формат
# #
# #     kernel = np.ones((5, 5), np.uint8)
# #     img = cv2.dilate(img, kernel, iterations=1)
# #
# #     img = cv2.erode(img, kernel, iterations=1)
# #
# #     cv2.imshow('Result', img)
# #
# #
# #     if cv2.waitKey(1) & 0xFF == ord('q'):
# #         break
#
# ## Work with image
#
# # import cv2
# # import numpy as np
# #
# # img = cv2.imread('images/image_1.jpg')
# # img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))
# # img = cv2.flip(img, -1)
#
# ##  Функция вращения картинки
# # def rotate(img_param, angle):
# #     height, width = img_param.shape[:2]
# #     point = (width // 2, height // 2)
# #
# #     mat = cv2.getRotationMatrix2D(point, angle, 1)
# #     return cv2.warpAffine(img_param, mat, (width, height))
#
# # img = rotate(img, 90)
#
#
# ##  Функция смещения картинки
# # def transform(img_param, x, y):
# #     mat = np.float32([[1, 0, x], [0, 1, y]])
# #     return cv2.warpAffine(img_param, mat, (img_param.shape[1], img_param.shape[0]))
# #
# # # img = transform(img, 30, 200)
# #
# # cv2.imshow('IMG', img)
# # cv2.waitKey(0)
#
#
# ## Нахождение краёв картинки
#
# # import cv2
# # import numpy as np
# #
# # img = cv2.imread('images/image_1.jpg')
# #
# # new_img = np.zeros(img.shape, dtype='uint8')
# #
# # # img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))
# # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# # img = cv2.GaussianBlur(img, (9, 9), 0)
# #
# # img = cv2.Canny(img, 100, 140)
# #
# # con, hir = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
# #
# # cv2.drawContours(new_img, con, -1, (230, 111, 148), 1) ## прорисовка нового изображения по контурам
# #
# # cv2.imshow('Result', new_img)
# # cv2.waitKey(0)
#
# ## The fifth lesson - color format
#
#
# # import cv2
# #
# # img = cv2.imread('images/image_1.jpg')
# #
# # img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))
# #
# # img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # convert to other format
# # img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR) # convert return
# #
# # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# #
# # r, g, b, = cv2.split(img) # разделение по слоям
# #
# # img = cv2.merge([g, b, r]) # конвертирование картинки по слоям
# #
# # cv2.imshow('Result', img)
# # cv2.waitKey(0)
#
# ## The sixth lesson - побитовые операции и маски
#
# # import cv2
# # import numpy
#
# # photo = cv2.imread('images/image_1.jpg')
# # img = numpy.zeros(photo.shape[:2], dtype='uint8')
# # img = numpy.zeros((350, 350), dtype='uint8')
# #
# # circle = cv2.circle(img.copy(), (200, 300), 120, 255, -1)
# # square = cv2.rectangle(img.copy(), (25, 25), (250, 350), 255, -1)
#
# ##      Побитовые операции
#
# # img = cv2.bitwise_and(photo, photo, mask=circle) # вывод одинаковых элементов
# # img = cv2.bitwise_or (circle, square) # полное объединение
# # img = cv2.bitwise_xor (circle, square) # исключение совпадений
# # img = cv2.bitwise_not(square) # инверсия
#
#
# # cv2.imshow('Result', img)
# # cv2.waitKey(0)
#
#
# ## The seventh lesson - распознавание лиц
# #
# # import cv2
# #
# # img = cv2.imread('images/friends_2.jpg')
# # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# #
# # faces = cv2.CascadeClassifier('faces.xml')
# #
# # results = faces.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
# #
# # for (x, y, w, h) in results:
# #     cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), thickness=3)
# #
# #
# # cv2.imshow('Result', img)
# # cv2.waitKey(0)
#
#
# ## The eighth lesson - распознавание номерных знаков и считывание данных
#
# # import cv2
# # import easyocr
# # import imutils
# # import numpy as np
# # from matplotlib import pyplot as pl
# #
# # img = cv2.imread('images/car_2.jpg')
# # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# #
# # img_filter = cv2.bilateralFilter(gray, 11, 15, 15)
# # edges = cv2.Canny(img_filter, 30, 200)
# #
# # cont = cv2.findContours(edges.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# # cont = imutils.grab_contours(cont)
# # cont = sorted(cont, key=cv2.contourArea, reverse=True)
# #
# # pos = None
# # for c in cont:
# #     approx = cv2.approxPolyDP(c, 15, True)
# #     if len(approx) == 4:
# #         pos = approx
# #         break
# #
# # mask = np.zeros(gray.shape, np.uint8)
# # new_img = cv2.drawContours(mask, [pos], 0, 255, -1)
# # bitwise_img = cv2.bitwise_and(img, img, mask=mask)
# #
# # (x, y) = np.where(mask == 255)
# # (x1, y1) = (np.min(x), np.min(y))
# # (x2, y2) = (np.max(x), np.max(y))
# # crop = gray[x1:x2, y1:y2]
# #
# # text = easyocr.Reader(['en'])
# # text = text.readtext(crop)
# # print(text)
# # res = text[0][-2]
# # final_image = cv2.putText(img, res, (x1, y2), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 2)
# # final_image = cv2.rectangle(img, (x1, x2), (y1, y2), (0, 255, 0), 2)
# #
# # pl.imshow(cv2.cvtColor(final_image, cv2.COLOR_BGR2RGB))
# # pl.show()
#
# # import cv2
# # # import numpy
# #
# # img = cv2.imread('images/image_1.jpg')
# #
# # # img = numpy.zeros(photo.shape[:2], dtype='uint8')
# # # img = numpy.zeros((350, 350), dtype='uint8')
# # #
# # # img_2 = cv2.circle(img.copy(), (200, 300), 120, 255, -1)
# # # square = cv2.rectangle(img.copy(), (25, 25), (250, 350), 255, -1)
# #
# # ##      Побитовые операции
# #
# # # img = cv2.bitwise_and(photo, photo, mask=circle) # вывод одинаковых элементов
# # # img = cv2.bitwise_or (circle, square) # полное объединение
# # # img = cv2.bitwise_xor (circle, square) # исключение совпадений
# # # img = cv2.bitwise_not(square) # инверсия
# #
# #
# # cv2.imshow('Result', img)
# # cv2.waitKey(0)
