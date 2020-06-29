# -*- coding: utf-8 -*-
# Author: Harold.Duan
# This module is sbo di api implements.

__version__ = "0.0.1.dev"
__author__ = "Harold.Duan"
__all__ = ['company','COMClassInfo','get_com_object','get_com_cls_info']

from win32com import client
from inspect import getmembers
from .company import Company
from .datatypes import SBOCOMClass
# from pythoncom import ProgIDFromCLSID


def get_com_object(com_obj_type: SBOCOMClass):
    ''' Get SBO COM object instance '''
    try:
        # com_obj = client.Dispatch(str(com_obj_type))
        com_obj = client.gencache.EnsureDispatch(str(com_obj_type))
        type_ = client.gencache.GetClassForProgID(str(com_obj_type))
        cls_id = com_obj.CLSID
        str_cls_id = str(cls_id)
        class_ = client.gencache.CLSIDToClass.GetClass(str_cls_id)
        prog_id = client.pythoncom.ProgIDFromCLSID(str_cls_id)
        # com_obj.__class__.__dict_
        # prog_id = com_obj.procids()
        # prog_id = ProgIDFromCLSID(cls_id)
        return com_obj
    except Exception as e:
        raise e

class COMClassInfo(object):
    ''' define COM class info '''

    def __init__(self, com_cls_type: SBOCOMClass):
        ''' constructor '''
        self.__com_class_type = SBOCOMClass
        self.__com_obj_ins = None
        self.__fields: []
        self.__methods: []
        self.__init(com_cls_type)
        pass

    @property
    def com_class_type(self) -> SBOCOMClass:
        ''' get COM class type '''
        return self.__com_class_type

    @property
    def com_object_instance(self):
        ''' get COM object instance '''
        return self.__com_obj_ins

    @property
    def fields(self) -> list:
        ''' get COM class fields '''
        return self.__fields

    @property
    def methods(self) -> list:
        ''' get COM class methods '''
        return self.__methods

    def __init(self, com_cls_type: SBOCOMClass):
        ''' class init function '''
        try:
            obj = get_com_object(com_cls_type)
            self.__get_com_class_fields(obj)
            self.__get_com_class_methods(obj)
        except Exception as e:
            raise e

    def __get_com_class_fields(self, com_obj_ins):
        ''' get COM class fields '''
        # obj = client.gencache.EnsureDispatch(str(com_obj_type))
        # obj = client.Dispatch(str(com_obj_type))
        try:
            fields = list(com_obj_ins._prop_map_get_.keys())
            self.__fields = fields
        except AttributeError as e:
            # print("Object has no attribute '_prop_map_get_'")
            # print("Check if the initial COM object was created with"
            #     "'win32com.client.Dispatch()'")
            raise e

    def __get_com_class_methods(self, com_obj_ins):
        ''' get COM class methods '''
        # obj = client.gencache.EnsureDispatch(str(com_obj_type))
        # obj = client.Dispatch(str(com_obj_type))
        try:
            # temp =  getmembers(com_obj_ins)
            # com_obj_ins.procids()
            val = com_obj_ins._find_dispatch_type_()
            methods = [m[0] for m in getmembers(com_obj_ins) if
                       (not m[0].startswith("_") and "clsid" not in m[0].lower())]
            self.__methods = methods
        except Exception as e:
            # print("Object has no attribute '_prop_map_get_'")
            # print("Check if the initial COM object was created with"
            #     "'win32com.client.Dispatch()'")
            raise e


def  get_com_cls_info(com_obj_type: SBOCOMClass) -> COMClassInfo:
    ''' Get SBO COM clss info instance '''
    try:
        ret_val = COMClassInfo(com_obj_type)
        return ret_val
    except Exception as e:
        raise e

ret_val = get_com_object(SBOCOMClass.COMPANY)
company = Company(ret_val)
