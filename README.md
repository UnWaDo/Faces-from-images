# Faces from images

This program allows you to crop faces from different photos you have. In order to use it you should first install requirements. It can be done using the *req.txt file*.

> pip install -r req.txt

To call the program you may simply type in the path to your photos and the folder, where to put the resulting files with faces (in `.jpg` format). **These folders must exist!**

> python main.py --source <PATH/TO/PHOTOS> --result <PATH/TO/FACES>

There are also two more optional arguments you may use: `--alpha` and `--ratio`. `--ratio` Allows you to set up the ratio between the width and height in format `WW:HH`. The width and height *may be float numbers*. `--alpha` Allows to set up the size of cropped image. The square, which is obtained by using [face_recognition](github.com/ageitgey/face_recognition) library, is modified using simple geometric operations. The width becomes (1 + 2*`alpha`)\*`initial_width`, while the height is calculated from resulting width and `--ratio` argument. The default for `--ratio` is `3:4`, while the default for `--alpha` is `0.2`. If the rectangle goes outside of the image, the same operation is tried, but with decreased alpha (it is decreased by `0.1`). If the alpha becomes less than 1, the initial square is returned.

The information is also available by calling the program with `-h` attribute.

> python main.py -h

An example of the program results can be seen in folder [Faces](https://github.com/UnWaDo/Faces-from-images/tree/master/Faces) on git. Source images can be seen in folder [Images](https://github.com/UnWaDo/Faces-from-images/tree/master/Images). Source images were downloaded from [free stock photos](freerangestock.com). The quality of face recognition is fully dependent on [face_recognition](github.com/ageitgey/face_recognition), I didn't make any modifications to the part of face recognition. 
