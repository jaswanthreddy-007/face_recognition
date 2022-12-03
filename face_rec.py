import cv2 as cv
import numpy as np
import face_recognition


imgelon = face_recognition.load_image_file('C:/Users/JaswanthReddy/Hackathon/face_recognition/Elon_Musk_2015.jpg')
imgelon = cv.cvtColor(imgelon,cv.COLOR_BGR2RGB)
imgtest = face_recognition.load_image_file('C:/Users/JaswanthReddy/Hackathon/face_recognition/taher.jpegg')
imgtest = cv.cvtColor(imgtest,cv.COLOR_BGR2RGB)

faceloc = face_recognition.face_locations(imgelon)[0]
encodeelon = face_recognition.face_encodings(imgelon)[0]
print(faceloc)

encodetest = face_recognition.face_encodings(imgtest)[0]

results = face_recognition.compare_faces([encodeelon],encodetest)
print(results)
cv.imshow('elon',imgelon)
cv.imshow('test',imgtest)
cv.waitKey(0)
cv.destroyAllWindows()
