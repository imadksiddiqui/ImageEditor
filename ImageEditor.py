from PIL import Image, ImageEnhance, ImageFilter
import os

path = './images/'
editedPath = './edited/'

def merge(im1, im2):
    w = im1.size[0] + im2.size[0]
    h = max(im1.size[1], im2.size[1])
    im = Image.new("RGBA", (w, h))

    im.paste(im1)
    im.paste(im2, (im1.size[0], 0))

    return im

def make_edit(img, name):
    img.save(f'{editedPath}/{name}_edited.jpg')


request = input("What do you want to do to your image? (1. merge, 2. change mode, 3. print dimensions 4. change dimensions 5. Change contrast: ")
img_name = input("Type the filename of the image: ")
img = Image.open(path + img_name)


if request == '1':
    img1_name = input("Type the filename of the second image: ")
    img1 = Image.open(path + img1_name)
    edit = merge(img, img1)

if request == '3':
    print(img.size)


if request == '2':
    edit = img.convert("L")
    make_edit(edit, os.path.splitext(img_name)[0])

if request == '4':
    dimension = input("Enter the new dimensions: ")
    dim = dimension.split('x')
    edit = img.thumbnail((int(dim[0]), int(dim[1])))
    make_edit(edit, os.path.splitext(img_name)[0])

if request == '5':
    factor = 1.5                                          
    enhanced = ImageEnhance.Contrast(img)
    edit = enhanced.enhance(factor)
    make_edit(edit, os.path.splitext(img_name)[0])
