from PIL import Image
import hashlib

from conf.settings import BASE_DIR


def resize_picture(file, width, height=None):
    file = str(file)

    name = file.split('.')[0]
    extension = file.split('.')[-1]
    path = BASE_DIR + '/media/' + file
    md5_hash = hashlib.md5(name)

    # open file
    pct = Image.open(path)

    # set sizes
    width = int(width)
    if not height:
        height = pct.size[1] * width / pct.size[0]
    else:
        height = int(height)
    size = (width, height)

    new_name = '{0}_{1}x{2}.{3}'.format(md5_hash.hexdigest(), width, height, extension)

    # resize image and save
    new_pct = pct.resize(size, Image.LANCZOS)
    new_pct.save(BASE_DIR + '/media/' + new_name)

    return new_name, height
