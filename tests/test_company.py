# -*- coding: utf-8 -*-
# Author: Harold.Duan
# This module is unit test for sboex.di.company module.

import sys
import os
from win32com import client
from inspect import getmembers

# cur_path = os.getcwd()
# print(cur_path)
path_sboex = os.path.abspath('./src')
sys.path.append(path_sboex)

from pysboex.di.datatypes import BoDataServerTypes,BoObjectTypes, BoSuppLangs,SBOCOMClass
from pysboex.di import company,get_com_object
from pysboex.di.error import Error
from pysboex.di.company import Company

class TestClassCompany(object):
    ''' Test class for sboex.di.Company '''

    def test_connect(self):
        ''' Test method for function connect '''
        company.db_server_type = BoDataServerTypes.MSSQL2012
        company.server = 'DEVSRV-B1'
        company.license_server = 'DEVSRV-B1:30000'
        company.company_db = 'SBO_Standard_Demo_Null'
        company.db_user_name = 'sa'
        company.db_password = 'AVAtech2010$'
        company.language = BoSuppLangs.CHINESE
        company.user_name = 'manager'
        company.password = '111111'
        company.sld_server = 'DEVSRV-B1:40000'
        ret_val = company.connect()
        assert isinstance(ret_val, Error)
        print('ErrorCode:%i ErrorMessage:%s' %
              (ret_val.error_code, ret_val.error_message))

    def test_disconnect(self):
        ''' Test method for function disconnect '''
        company.disconnect()
        assert company.is_connected

    def test_get_business_object(self):
        ''' Test method for function get business object '''
        ret_val = company.get_business_object(BoObjectTypes.BUSINESS_PARTNERS)
        assert isinstance(ret_val,)
        print(ret_val)


def _get_com_members(com_obj_type : SBOCOMClass):
    ''' Get COM object members '''
    try:
        com_obj = client.gencache.EnsureDispatch(str(com_obj_type))
        fields = list(com_obj._prop_map_get_.keys())
        print(fields)
        # print(com_obj)
        # print(dir(com_obj))
        for key in dir(com_obj):
            method = getattr(com_obj,key)
            if str(type(method)) == "<type 'instance'>":
                print(key)
                for sub_method in dir(method):
                    if not sub_method.startswith("_") and not "clsid" in sub_method.lower():
                        print(sub_method)
            else:
                print(method)
    except Exception as e:
        raise e

def _print_members(com_obj_type : SBOCOMClass):
    ''' Print members of given COM object '''
    # obj = client.gencache.EnsureDispatch(str(com_obj_type))
    obj = client.Dispatch(str(com_obj_type))
    print(type(obj))
    try:
        fields = list(obj._prop_map_get_.keys())
    except AttributeError:
        print("Object has no attribute '_prop_map_get_'")
        print("Check if the initial COM object was created with"
              "'win32com.client.gencache.EnsureDispatch()'")
        raise
    methods = [m[0] for m in getmembers(obj) if (not m[0].startswith("_") and "clsid" not in m[0].lower())]
    if len(fields) + len(methods) > 0:
        print("Members of '{}' ({}):".format(str(com_obj_type), obj))
    else:
        raise ValueError("Object has no members to print")
    print("\tFields:")
    if fields:
        for field in fields:
            print(f"\t\t{field}")
    else:
        print("\t\tObject has no fields to print")
    print("\tMethods:")
    if methods:
        for method in methods:
            print(f"\t\t{method}")
    else:
        print("\t\tObject has no methods to print")

if __name__ == '__main__':
    # test = TestClassCompany()
    # test.test_connect()
    # test.test_get_business_object()
    # _get_com_members(SBOCOMClass.COMPANY)
    _print_members(SBOCOMClass.COMPANY)
    pass
