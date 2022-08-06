# Class Face Detect
import face_recognition
import imageio
import cv2
import numpy as np


class faceDetect:

  def __init__ (self, user_image, user_label):

    face_1 = face_recognition.load_image_file(user_image)
    face_1_encoding = face_recognition.face_encodings(face_1)[0]

    self.known_face_encodings = [face_1_encoding]

    self.known_face_names = [user_label]

  def predict(self, pred_user_image):

    file_name = pred_user_image

    unknown_image = face_recognition.load_image_file(file_name)
    unknown_image_to_draw = cv2.imread(file_name)

    face_locations = face_recognition.face_locations(unknown_image)
    face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

    for (top,right, bottom, left), face_encoding in zip(face_locations, face_encodings):

      matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)

      name = "Unknown"

      face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
      best_match_index = np.argmin(face_distances)
      
      if matches[best_match_index]:
        
        name = self.known_face_names[best_match_index]
      cv2.rectangle(unknown_image_to_draw, (left, top), (right, bottom),(0,255,0),3)
      cv2.putText(unknown_image_to_draw,name, (left, top-20), cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2, cv2.LINE_AA)
  
    return cv2.imwrite("/content/pred_image.png", unknown_image_to_draw)


if __name__ == "__main__":
  tr = "/home/srijan/face_recognition/target_image.png"
  pd = "/home/srijan/face_recognition/upload_image.png"

  fr = faceDetect(tr, 'modi')

  fr.predict(pd)