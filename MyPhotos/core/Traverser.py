# -*- coding: utf-8 -*-

import os
import magic
import shutil
from MyPhotos.MyImages.MyImage import MyImage

class Traverser(object):

    # _source = "."
    # _dest = "NewFolder"
    # _images = None
    # _duplicates = None
    #
    # def __init__(self, source, dest):
    #     self._source = source
    #     self._dest = dest
    #     self._images_by_hash = []
    #     self._images_by_date = []
    #     self._duplicates = []

    def organize(self, src, dest):
        '''
        Copy images from src to dest, organizing by datetime of creation
        '''
        total = self._count_files(src) #TODO: Check for errors
        print "Total files:", total

        count = 0
        percentagem = -1

        for dirName, subdirList, fileList in os.walk(self._source):
            for file in fileList:
                count += 1
                if count * 100 / total != percentagem:
                    percentagem = count * 100 / total
                    print "{} de {} - {}%".format(count, total, percentagem)

                file_path = os.path.join(dirName, file)
                type = magic.from_file(file_path).split()[0]

                if type == 'JPEG':
                    im = MyImage(file_path, type) #TODO: how to take datetime from other types od img?
                else:
                    continue

                the_datetime = im.get_datetime_orginal()
                new_path = os.path.join(dest, the_datetime.year, the_datetime.month)
                if not os.path.exists(new_path):
                    os.makedirs(new_path)

                name = im.get_name()
                if os.path.exists(os.path.join(new_path, name)):
                    c = 0
                    name = name.split(".")
                    name.insert(-1,str(c))
                    name = ".".join(name)
                    while os.path.exists(os.path.join(new_path, name)):
                        c += 1
                        name = name.split(".")
                        name[-2, str(c)]
                        name = ".".join(name)

                shutil.copy2(file_path, os.path.join(new_path, name))





    def _count_files(self, dir):
        return int(os.popen("find {} -not -path '*/\.*' -type f | wc -l".format(dir) ).read())

    # def run(self):
    #
    #     print "find {} -type f | wc -l".format(self._source)
    #     total_files =  int(os.popen("find {} -not -path '*/\.*' -type f | wc -l".format(self._source) ).read())
    #     count = 1
    #
    #     not_sup = []
    #
    #     for dirName, subdirList, fileList in os.walk(self._source):
    #
    #         print "{} de {} - {}%".format(count, total_files, count*100/total_files)
    #
    #         for file in fileList:
    #             file_path = os.path.join(dirName, file)
    #             type = magic.from_file(file_path).split()[0]
    #             if type == 'JPEG':
    #                 # print 'imagem:', file
    #                 im = MyImage(file_path, type)
    #                 self._images_by_date.append((str(im.get_datetime_orginal()), im))
    #                 self._images_by_hash.append((im.get_hash(), im))
    #             else:
    #                 not_sup.append(file_path)
    #
    #                 # print im
    #
    #             count += 1
    #
    #     print " ------------- FILES NOT SUPORTED ------------- "
    #     for i in not_sup:
    #         print i
    #     print " ------------- xxxxxxxxxxxxxxxxxx ------------- "
    #
    #     self._images_by_date = sorted(self._images_by_date, key= lambda img : img[0])
    #     self._images_by_hash = sorted(self._images_by_hash, key=lambda img: img[0])
    #
    #     last = None
    #     las_dup = []
    #
    #     for i in range(len(self._images_by_hash)-1):
    #         if self._images_by_hash[i][0] == self._images_by_hash[i+1][0]:
    #             if not las_dup:
    #                 las_dup += [i, i+1]
    #             else:
    #                 las_dup += [i + 1]
    #         elif las_dup:
    #             self._duplicates.append(las_dup)
    #             las_dup = []
    #
    #     for i in self._images_by_hash:
    #         print i[0], i[1].get_hash()
    #
    #     for i in self._duplicates:
    #         print i



