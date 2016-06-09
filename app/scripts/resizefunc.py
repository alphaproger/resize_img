from PIL import Image
import hashlib
import os

from conf.settings import BASE_DIR


def resize_picture(file, width, height=None):
    file = str(file)

    name = file.split('.')[0]
    extension = file.split('.')[-1]
    path = BASE_DIR + '/media/' + file

    # open file
    pct = Image.open(path)

    # set sizes
    width = max(int(width), 1)
    if not height:
        height = max(pct.size[1] * width / pct.size[0], 1)
    else:
        height = max(int(height), 1)
    size = (width, height)

    md5_hash = hashlib.md5(name)
    new_name = '{0}_{1}x{2}.{3}'.format(md5_hash.hexdigest(), width, height, extension)

    # resize image and save
    if not os.path.isfile(BASE_DIR + '/media/' + new_name):
        new_pct = pct.resize(size, Image.LANCZOS)
        new_pct.save(BASE_DIR + '/media/' + new_name)

    return new_name, height
