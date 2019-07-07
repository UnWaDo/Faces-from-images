import face_recognition
from PIL import Image
import os
from input import args


ALLOWED_EXTENSIONS = ['jpeg', 'jpg', 'png', 'gif', 'bmp']


def count_ratio(str_ratio):
    x, y = str_ratio.split(':')
    return float(y)/float(x)


def get_filenames(path):
    filenames = []
    for file in os.listdir(path):
        if file.split('.')[-1] in ALLOWED_EXTENSIONS:
            filenames.append(file)
    return filenames


def make_rect(coords, alpha):
    ratio = count_ratio(args['ratio'])  # TODO: put to some other place to enhance time
    if alpha < 0:
        return coords

    ver_dif = coords[2] - coords[0]
    hor_dif = coords[1] - coords[3]
    ver_add = int((hor_dif*(1 + 2 * alpha)*ratio - ver_dif)/2)
    hor_add = int(alpha * hor_dif)
    new_coord = (coords[0] - ver_add, coords[1] + hor_add,
                 coords[2] + ver_add, coords[3] - hor_add)
    return new_coord


def get_face(full_image, coords, alpha=args['alpha']):
    try:
        top, right, bottom, left = make_rect(coords, alpha)
        img = full_image[top:bottom, left:right]
        return Image.fromarray(img)
    except ValueError:
        return get_face(full_image, coords, alpha - 0.1)


im_paths = get_filenames(args['source_dir'])
im_counter = 0
total_paths = len(im_paths)
faces_counter = 0


for filename in im_paths:
    im_counter += 1
    print("({}/{}) Image {} is processing: ".format(im_counter, total_paths, filename))

    image = face_recognition.load_image_file(os.path.join(args['source_dir'], filename))
    faces = face_recognition.face_locations(image)
    faces_on_image = 0

    for face in faces:
        faces_on_image += 1
        faces_counter += 1
        face_image = get_face(image, face)
        face_filename = '{}_{}.jpg'.format(filename.rsplit('.', 1)[0], faces_on_image)
        face_image.save(os.path.join(args['result_dir'], face_filename))
        print("\tFace {}: filename is {}".format(faces_on_image, face_filename))

    print("Totally {} faces on image. \n ---------------".format(faces_on_image))

print(" +++++++++++++++ \nTotally {} faces on all images.".format(im_counter))
