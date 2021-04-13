import os
import shutil

"""
yolov4数据集和VOC基本相同
"""
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


def copyXml(origin_xml_path, object_path, filenames):
    """
    复制图片到指定文件夹内
    """
    for filename in filenames:
        shutil.copy(os.path.join(origin_xml_path, filename+".xml"), os.path.join(object_path, filename+".xml"))


if __name__ == '__main__':
    train_filenames = readtxt("C:/Users/Administrator/Desktop/PEST/PEST/ImageSets/train.txt")
    val_filenames = readtxt("C:/Users/Administrator/Desktop/PEST/PEST/ImageSets/val.txt")
    test_filenames = readtxt("C:/Users/Administrator/Desktop/PEST/PEST/ImageSets/test.txt")

    origin_xml_path = "C:/Users/Administrator/Desktop/PEST/PEST/Annotations"
    img_path = "C:/Users/Administrator/Desktop/PEST/yolov4/Annotations"
    copyXml(origin_xml_path, os.path.join(img_path, "train"), train_filenames)
    copyXml(origin_xml_path, os.path.join(img_path, "val"), val_filenames)
    copyXml(origin_xml_path, os.path.join(img_path, "test"), test_filenames)