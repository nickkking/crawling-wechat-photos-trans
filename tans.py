# coding: utf-8
from PIL import Image
import os
import os.path

# rootdir = r'D:\用户目录\我的图片\From Yun\背景图\背景图'  # 指明被遍历的文件夹
rootdir = r'E:/spider/photo'  # 原图片目录

for parent, dirnames, filenames in os.walk(rootdir):  # 遍历每一张图片
    for filename in filenames:
        print('parent is :' + parent)
        print('filename is :' + filename)
        currentPath = os.path.join(parent, filename)
        print('the fulll name of the file is :' + currentPath)

        im = Image.open(currentPath)  # 打开gif格式的图片


        def iter_frames(im):
            try:
                i = 0
                while 1:
                    im.seek(i)
                    imframe = im.copy()
                    if i == 0:
                        palette = imframe.getpalette()
                    else:
                        imframe.putpalette(palette)
                    yield imframe
                    i += 1
            except EOFError:
                pass


        for i, frame in enumerate(iter_frames(im)):
            print('frame信息：==>')
            print(frame.info)
            frame.save(r"1.0" + filename + '.png',
                       'png')
            # //frame.save(r"/Users/mamabang/Downloads/new_emoticon/"+filename +'.gif',**frame.info)

# 转化格式，重新命名保存到C_2文件夹，这里后面的.gif表示转换后的图片格式，要转化成png格式的话改成.png即可。其他格式相互转化类似。