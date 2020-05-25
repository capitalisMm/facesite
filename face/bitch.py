import face_recognition
from PIL import Image, ImageDraw
from tqdm import tqdm
import pickle
import math
from face_recognition import face_distance


def load_encodings():
    # load pickled encodings
    with open('/home/tony/PycharmProjects/facesite/face/dataset_faces.dat', 'rb') as f:
        return pickle.load(f)


def load_names():
    # load pickled names
    with open('/home/tony/PycharmProjects/facesite/face/dataset_names.dat', 'rb') as g:
        return pickle.load(g)


def magic(image, encodings, names):
    # final variables
    TOLERANCE = .6

    # temporary names array
    save_name = []

    # unknown image
    # unknown_image = face_recognition.load_image_file('/home/tony/Desktop/programming/try_again/test_image.jpg')
    unknown_image = face_recognition.load_image_file(image)

    # find all faces and face encodings in unknown image
    face_locations = face_recognition.face_locations(unknown_image)
    face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

    # convert image to PIL format
    pil_image = Image.fromarray(unknown_image)
    # create draw instance
    draw = ImageDraw.Draw(pil_image)

    # loop through each face found in unknown image
    for (top, right, bottom, left), face_encoding in tqdm(zip(face_locations, face_encodings)):
        # see if face is a match
        matches = face_recognition.compare_faces(encodings, face_encoding, TOLERANCE)

        name = "unknown"

        if True in matches:
            first_match_index = matches.index(True)
            name = names[first_match_index]
            # add name to save names array
            save_name.append(name)

        # draw a box around face
        draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))

        # draw label
        text_width, text_height = draw.textsize(name)
        draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 255), outline=(0, 0, 255))
        draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255))

    del draw
    file_name = ""
    save_name.sort()

    # loop through save names and create file name
    for i in range(len(save_name)):
        if i == 0:
            file_name = file_name + "" + save_name[i]
        else:
            file_name = file_name + " and " + save_name[i]

    file_name = file_name + ".jpg"
    pil_image.save('/home/tony/PycharmProjects/facesite/media/ml_pics/' + file_name, "JPEG")

    return file_name


def face_accuracy(image, encodings):
    # load images for use
    unknown_image = face_recognition.load_image_file(image)
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

    # find distance between encodings and image
    distance = face_distance(encodings, unknown_encoding)

    # find closest one
    print(distance)
    close = distance.min()

    face_match_threshold = .6

    if close > face_match_threshold:
        r = (1.0 - face_match_threshold)
        linear_val = (1.0 - close) / (r * 2.0)
        return linear_val
    else:
        r = face_match_threshold
        linear_val = 1.0 - (close / (r * 2.0))
        return linear_val + ((1.0 - linear_val) * math.pow((linear_val - 0.5) * 2, 0.2))


def face_close_match(image, encodings, names):
    # load images for use
    unknown_image = face_recognition.load_image_file(image)
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

    # find distance between encodings and image
    distance = face_distance(encodings, unknown_encoding)

    # find index of max
    print(distance)
    ind = distance.argmin()

    # name of the max
    # names.sort()
    name = names[ind]

    source = name + '/' + name + '_face-1.jpg'

    for n in range(len(names)):
        print(names[n]),

    return source