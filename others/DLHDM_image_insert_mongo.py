import os
from pymongo import MongoClient


def dlhdm_image_into_mongo():
    '''
    将道路对应的道路横断面的图片入库
    :return:
    '''
    dlhdm_image_path = r'C:\Users\95768\Desktop\横断面图片'
    coon = MongoClient('0.0.0.0', 27017)
    db = coon.JN_SYSTEM
    collection_name = db.DLHDM_image
    image_dir = os.walk(dlhdm_image_path)
    for image_item_dir in image_dir:
        print(image_item_dir)
        if len(image_item_dir[2]) > 0:
            for item_image in image_item_dir[2]:
                # splitext将文件名和后缀名分开,split()将路径和文件名分开
                if os.path.splitext(item_image)[1].upper() == '.PNG':
                    # print(os.path.splitext(item_image))
                    image_objectid = os.path.splitext(item_image)[0]
                    # print(image_objectid)
                    image_file = os.path.join(image_item_dir[0], item_image)
                    # print(image_file)
                    f = open(image_file, 'rb')
                    image_content = f.read()
                    image_dict = {}
                    image_dict['image_objectid'] = int(image_objectid)
                    image_dict['image_content'] = image_content
                    try:
                        collection_name.insert(image_dict)
                        print(str(item_image)+'写入成功！！！')
                    except Exception as e:
                        f_err = open('./img_err.txt', 'a')
                        f_err.write(str(item_image))
                        f_err.write(',')
                        f_err.write(str(e))
                        f_err.write('\n')
                        continue


if __name__ == '__main__':
    dlhdm_image_into_mongo()
