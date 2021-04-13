import os
import xml.dom.minidom
import shutil

trans_dict = {'1':'0','2':'1','3':'2','5':'3','6':'4','7':'5','8':'6','10':'7','11':'8','12':'9','13':'10',
              '14':'11','15':'12','16':'13','24':'14','25':'15','28':'16','29':'17','31':'18','32':'19',
              '34':'20','35':'21','36':'22','37':'23'}


def xml2txt(xml_path, txt_path, filenames):
    for filename in filenames:
        xml_filename = filename + ".xml"
        dom = xml.dom.minidom.parse(os.path.join(xml_path, xml_filename))
        root = dom.documentElement
        width = int(root.getElementsByTagName('width')[0].firstChild.data)
        height = int(root.getElementsByTagName('height')[0].firstChild.data)
        name = root.getElementsByTagName('name')
        xmin = root.getElementsByTagName('xmin')
        xmax = root.getElementsByTagName('xmax')
        ymin = root.getElementsByTagName('ymin')
        ymax = root.getElementsByTagName('ymax')

        with open(os.path.join(txt_path, filename + ".txt"), 'w', encoding='UTF-8') as f:
            for i in range(len(name)):
                idx = name[i].firstChild.data
                idx = trans_dict[idx]
                center_x = round(((int(xmin[i].firstChild.data) + int(xmax[i].firstChild.data)) / 2) / width, 8)
                center_y = round(((int(ymin[i].firstChild.data) + int(ymax[i].firstChild.data)) / 2) / height, 8)
                width_gt = round((int(xmax[i].firstChild.data) - int(xmin[i].firstChild.data)) / width, 8)
                height_gt = round((int(ymax[i].firstChild.data) - int(ymin[i].firstChild.data)) / height, 8)

                str_temp = str(idx) + ' ' + str(center_x) + ' ' + str(center_y) + ' ' + str(width_gt) + ' ' + str(
                    height_gt) + '\n'
                f.write(str_temp)
        f.close()


def readtxt(txt_path):
    """
    读取train.txt,val.txt,test.txt分别返回 xml2txt函数所需的filenames。
    :return: filenames:List[str]
    """
    f = open(txt_path)
    lines = f.readlines()
    print(type(lines))
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines


def copyImg(origin_img_path, object_path, filenames):
    """
    复制图片到指定文件夹内
    """
    for filename in filenames:
        shutil.copy(os.path.join(origin_img_path, filename+".jpg"), os.path.join(object_path, filename+".jpg"))


if __name__ == '__main__':
    train_filenames = readtxt("H:/pest/ImageSets/train.txt")
    val_filenames = readtxt("H:/pest/ImageSets/val.txt")
    test_filenames = readtxt("H:/pest/ImageSets/test.txt")
    xml_path = "H:/pest/Annotations"
    txt_path = "H:/pest/labels"
    xml2txt(xml_path, os.path.join(txt_path, "train"), train_filenames)
    xml2txt(xml_path, os.path.join(txt_path, "val"), val_filenames)
    xml2txt(xml_path, os.path.join(txt_path, "test"), test_filenames)

    # 上面通过读取train.txt,val.txt,test.txt将xml转换成txt之后放入对应文件夹中
    # 下面把图片放入到对应的文件夹中去
    origin_img_path = "H:/pest/JPEGImages"
    img_path = "H:/pest/images"
    # copyImg(origin_img_path, os.path.join(img_path, "train"), train_filenames)
    # copyImg(origin_img_path, os.path.join(img_path, "val"), val_filenames)
    # copyImg(origin_img_path, os.path.join(img_path, "test"), test_filenames)


