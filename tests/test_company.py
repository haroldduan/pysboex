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

from pysboex.di.datatypes import BoDataServerTypes, BoObjectTypes, BoSuppLangs, SBOCOMClass
from pysboex.di import company, get_com_object,get_com_cls_info
from pysboex.di.company import Company
from pysboex.di.error import Error


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


if __name__ == '__main__':
    # test = TestClassCompany()
    # test.test_connect()
    # test.test_get_business_object()
    ret_val = get_com_cls_info(SBOCOMClass.COMPANY)
    # ret_val = get_com_cls_info(SBOCOMClass.ITEMS)
    pass
