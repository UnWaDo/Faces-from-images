import argparse


parser = argparse.ArgumentParser(description='Cropping faces from images.')
parser.add_argument('--source', required=True, metavar='PATH/TO/DIR',
                    help='A path to folder where photos are situated.', dest='source_dir')
parser.add_argument('--result', required=True, metavar='PATH/TO/DIR',
                    help='A path to folder where to put faces.', dest='result_dir')
parser.add_argument('--ratio', metavar='W:H', default='3:4',
                    help='The ratio between width and height. Default is set to 3:4.', dest='ratio')
parser.add_argument('--alpha', metavar='0.x', default=0.2, type=float,
                    help='The multiplier to increase the area of the photo. Default is set to 0.2'
                         'If the final borders are outside of the picture, this multiplier will be decreased up to 1, '
                         'after which square will be used.', dest='alpha')
parser.add_argument('-r', action='store_true', help=argparse.SUPPRESS)  # TODO: recursively go to folders
args = vars(parser.parse_args())

