# -*- coding: utf-8 -*-
import os

from PIL import Image
from PIL.ExifTags import TAGS

from datetime import datetime

class MyImage(object):

    _im = None
    _type = None
    _file_name = None

    # 36867: 'DateTimeOriginal',
    # 36868: 'DateTimeDigitized',
    # 306: 'DateTime'
    # 50971: 'PreviewDateTime'
    # 34853: 'GPSInfo'
    _datetime = None
    _datetime_original = None
    _datetime_digitized = None
    _datetime_preview = None
    _gps_info = None

    def __init__(self, im_path, type):
        """
        receives path to image
        :type im_path: string
        """
        self._im = Image.open(im_path)
        self._type = type
        self._file_name = os.path.basename(im_path)

        if type == 'JPEG': #TODO: use strategy pattern
            info = self._im._getexif()
            # print info
            if info : #TODO: what to do if has no info
                for tag, value in info.items():
                    if TAGS.get(tag,tag) == 'DateTime':
                        self._datetime = datetime.strptime(value, '%Y:%m:%d %H:%M:%S')
                    elif TAGS.get(tag,tag) == 'DateTimeOriginal':
                        self._datetime_original = datetime.strptime(value, '%Y:%m:%d %H:%M:%S')
                    elif TAGS.get(tag, tag) == 'DateTimeDigitized':
                        self._datetime_digitized = datetime.strptime(value, '%Y:%m:%d %H:%M:%S')
                    elif TAGS.get(tag, tag) == 'PreviewDateTime':
                        self._datetime_preview = datetime.strptime(value, '%Y:%m:%d %H:%M:%S')
                    elif TAGS.get(tag, tag) == 'GPSInfo':
                        self._gps_info = value

        elif type == 'PNG':
            print "Not yet implemented"

    def __unicode__(self):
        return "{}: {}, datetime: {}, original: {}, digitized: {}, preview: {}, GPS: {}".format(self._file_name,
                                                                                                  self._type,
                                                                                                  self._datetime,
                                                                                                  self._datetime_original,
                                                                                                  self._datetime_digitized,
                                                                                                  self._datetime_preview,
                                                                                                  self._gps_info)
    def __str__(self):
        return self.__unicode__()

        # get meta info





