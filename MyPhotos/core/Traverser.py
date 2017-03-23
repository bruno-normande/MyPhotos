# -*- coding: utf-8 -*-

import os
import magic
from MyPhotos.MyImages.MyImage import MyImage

class Traverser(object):

    _source = "."
    _dest = "NewFolder"

    def __init__(self, source, dest):
        self._source = source
        self._dest = dest

    def run(self):

        print "find {} -type f | wc -l".format(self._source)
        total_files =  int(os.popen("find {} -not -path '*/\.*' -type f | wc -l".format(self._source) ).read())
        count = 1

        for dirName, subdirList, fileList in os.walk(self._source):

            print "{} de {} - {}%".format(count, total_files, count*100/total_files)

            for file in fileList:
                file_path = os.path.join(dirName, file)
                type = magic.from_file(file_path).split()[0]
                if type in ['JPEG', 'PNG']:
                    print 'imagem:', file
                    im = MyImage(file_path, type)

                    # print im

                count += 1

