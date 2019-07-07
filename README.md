# Faces from images

This program allows you to crop faces from different photos you have. In order to use it you should first install requirements. It can be done using the req.txt file.

$ pip install -r req.txt

To call the program you may simply type in the path to your photos and the folder, where to put the resulting files with faces (in .jpg format). These folders must exist!

$ python main.py --source <PATH/TO/PHOTOS> --result <PATH/TO/FACES>

There are also two more optional arguments you may use: --alpha and --ratio. --ratio Allows you to set up the ratio between the width and height in format WW:HH. The width and height may be float numbers. --alpha Allows to set up the size of cropped image. The square, which is obtained by using github.com/ageitgey/face_recognition(face_recognition) library, is modified using simple geometric operations. The width becomes (1 + 2*alpha)*initial_width, while the height is calculated from resulting width and --ratio argument. The default for --ratio is 3:4, while the default for --alpha is 0.2. If the rectangle goes outside of the image, the same operation is tried, but with decreased alpha (- 0.1). If the alpha becomes less than 1, the initial square is returned.
