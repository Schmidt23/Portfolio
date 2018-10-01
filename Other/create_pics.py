# ! encoding=utf-8

"""Create a given number of pictures increasing in size by 1 MB. File format can be changed from TIFF but only TIFF works
as intended atm since there is no compression. (Somehow now) Pretty Accurate at least 'til 100 MB'"""

from PIL import Image, ImageDraw, ImageFont
import random
import math
import os
import sys
import getopt


def create_pic(name, w, h, fm, ind, pth):
    # creates file with number pixel == size --slow
    pixels = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 0, 0), (255, 255, 255)]
    pxdata = []
    im = Image.new('RGB', (w, h))
    for i in xrange(w * h):
        pxdata.append(random.choice(pixels))
    im.putdata(pxdata)
    try:
        im.save("{}\\{}{}{}".format(pth, name, ind, fm))
    except IOError as e:
        print e
        sys.exit(1)
    except ValueError as e:
        print e
        sys.exit(1)

def add_multiple(li, it, n):
    for i in xrange(n):
        li.append(it)


def fast_create_pic(name, w, h, fm, ind, pth):
    # creates file with 100*100 px stretched to given size --faster
    pixels = [(255, 0, 0), (0, 255, 0), (0, 0, 255)] #(0, 0, 0), (255, 255, 255)]
    pxdata = []

    im = Image.new('RGB', (100, 100))
    for i in xrange(100 * 100):
        pxdata.append(random.choice(pixels))
    im.putdata(pxdata)
    im = im.resize((w, h))
    try:
        im.save("{}\\{}{}{}".format(pth, name, ind, fm))
    except IOError as e:
        print e
        sys.exit(1)
    except ValueError as e:
        print e
        sys.exit(1)


def text_create_pic(name, w, h, fm, ind, pth, txt):
    # creates pic with given text. Needs link to font!!!
    im = Image.new('RGB', (w, h), (255, 255, 255))
    d = ImageDraw.Draw(im)
    d.text((10, 10), '{!s} \n{}'.format(txt, ind), font=fnt, fill=(0, 0, 0))
    try:
        im.save("{}\\{}{}{}".format(pth, name, ind, fm))
    except IOError as e:
        print e
        sys.exit(1)
    except ValueError as e:
        print e
        sys.exit(1)


def just_text(name, fm, ind, pth, txt):
    # creates files containing text with fixed size
    im = Image.new('RGB', (591, 591), (255, 255, 255))
    d = ImageDraw.Draw(im)
    d.text((10, 10), '{!s} \n{}'.format(txt, ind), font=fnt, fill=(0, 0, 0))
    try:
        im.save("{}\\{}{}{}".format(pth, name, ind, fm))
    except IOError as e:
        print e
        sys.exit(1)
    except ValueError as e:
        print e
        sys.exit(1)


def return_size(idx):
    # returns size/dimensions needed to create idx+1.MB file
    # 1MB(1024² byte) / 3 (3byte per RGB pixel) == w*h if w==h
    mb = (idx) * MB
    return int(math.sqrt(mb / BYTES))+1


def return_text(fl):
    #tries to open given string as path to file. Returns input as string if path not valid.
    try:
        with open(fl,'rb') as f:
            text = f.read()
    except IOError:
        print "{} is not a valid file path. Input will be used as string.".format (fl)
        text = fl
    return text

if __name__ == "__main__":
    # constants
    MB = 1024 * 1024.00000
    BYTES = 3
    # default values
    name_pic = "pic"
    nr_pics = 3
    file_format = ".tif"
    func = create_pic
    path = os.getcwd()
    one_file = False
    # textfile defaults
    txt = "Hello World \n newline"
    font_size = 20
    fnt = ImageFont.truetype('C:\\PATH\\TO\\FONT\\font.ttf', font_size)
    # get sysargs
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hqjot:n:f:p:i:d:")
    except getopt.GetoptError:
        print 'create_pics.py -h=help -q=fast_mode -j=just_text -o=one_file -t=textfile "string" or <textfilepath>'\
         '-n <number_pics> -f <.file_format> -p <outpath> -i <name>'
        sys.exit(2)

    # switch defaults with sysargs
    for opt, arg in opts:
        if opt == '-h':
            print 'create_pics.py -h=help -q=fast_mode -j=just_text -o=one_file -t=textfile "string" or <textfilepath> '\
             '-n <number_pics> -f <.file_format> -p <outpath> -i <name>'
            sys.exit()
        elif opt == '-t':
            txt = return_text(arg)
            func = text_create_pic
        elif opt == '-q':
            func = fast_create_pic
            print "fast_mode = On"
        elif opt == '-j':
            func = just_text
            print "just text = On"
        elif opt == '-o':
            one_file = True
            print "Creating one file of given size (default ~{}MB)".format(nr_pics)
        elif opt == '-n':
            nr_pics = int(arg)
            if not one_file:
                print "number of pics to create: {}".format(nr_pics)
            else:
                print "size of file: ~{}MB".format(nr_pics)
        elif opt == '-f':
            file_format = arg
            if file_format == '.pdf':
                MB *= 4
            print "file format changed to {}. Please be aware that file sizes will probably be off the mark".format(arg)
        elif opt == "-p":
            path = arg
            print "path changed to {}".format(path)
        elif opt == '-i':
            name_pic = arg
            print "filename changed to {}".format(arg)

    if not one_file:
        if func == text_create_pic:
            for i in xrange(1, nr_pics+1):
                wh = return_size(i)
                text_create_pic(name_pic, wh, wh, file_format, i, path, txt)
                print path + "\\pic" + str(i)

        elif func == just_text:
            for i in xrange(1,nr_pics+1):
                just_text(name_pic, file_format, i, path, txt)
                print "{}\\pic{}".format(path,str(i))
        else:
            for i in xrange(1,nr_pics+1):
                wh = return_size(i)
                func(name_pic, wh, wh, file_format, i, path)
                print "{}\\pic{} {}  {:.5f}".format(path, str(i), wh, (wh ** 2 * BYTES / MB))
    else:
        if func == text_create_pic:
            wh = return_size(nr_pics)
            text_create_pic("of"+name_pic, wh, wh, file_format, nr_pics, path, txt)
            print "{}\\pic{}".format(path,str(nr_pics))

        elif func == just_text:
            print "just text"
            just_text("of"+name_pic, file_format, nr_pics, path, txt)
            print "{}\\pic{}".format(path,str(nr_pics))
        else:
            wh = return_size(nr_pics)
            func("of"+name_pic, wh, wh, file_format, nr_pics, path)
            print "{}]\\pic{} {}  {:.5f}".format(path,str(nr_pics), wh,(wh ** 2 * BYTES / MB))
