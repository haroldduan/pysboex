# -*- coding: utf-8 -*-
# Author: Harold.Duan
# This module is sbo error process implements.

__version__ = "0.0.1.dev"
__author__ = "Harold.Duan"
__all__ = ['Error']

import json


class Error(object):
    ''' define Error Repository class '''

    # def __init__(self, **kwargs):
    #     ''' constructor '''
    #     self.__error_code = 0
    #     self.__error_message = 'Ok'
    #     try:
    #         # properties set value
    #         if kwargs:
    #             atts = kwargs if isinstance(
    #                 kwargs, dict) else json.loads(kwargs)
    #             print(atts)
    #             for k, v in atts.items():
    #                 # print(k)
    #                 # print("__%s" % k)
    #                 setattr(self, k, v)
    #     except Exception as e:
    #         raise e

    def __init__(self, code: int = 0, message: str = ''):
        ''' constructor '''
        try:
            self.__error_code: int = code
            self.__error_message: str = message
        except Exception as e:
            raise e

    @property
    def error_code(self) -> int:
        return self.__error_code

    @property
    def error_message(self) -> str:
        return self.__error_message
