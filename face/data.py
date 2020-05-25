import face_recognition
import os
from tqdm import tqdm
import pickle

encodings = []
names = []

# train directory
train_dir = os.listdir('/home/tony/PycharmProjects/facesite/media/train_dir/')

# loop through each person
for person in tqdm(train_dir):
    pix = os.listdir("/home/tony/PycharmProjects/facesite/media/train_dir/" + person)
    # loop through each training image for current person
    for person_img in pix:
        face = face_recognition.load_image_file("/home/tony/PycharmProjects/facesite/media/train_dir/"
                                                + person + "/" + person_img)
        face_bounding_boxes = face_recognition.face_locations(face)

        # if only one face
        if len(face_bounding_boxes) == 1:
            face_enc = face_recognition.face_encodings(face)[0]
            # add face encoding
            encodings.append(face_enc)
            names.append(person)

        else:
            print(person + "/" + person_img + " was skipped and can't be used for training")

with open('dataset_faces.dat', 'wb') as f:
    pickle.dump(encodings, f)

with open('dataset_names.dat', 'wb') as g:
    pickle.dump(names, g)
