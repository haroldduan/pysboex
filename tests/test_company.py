# -*- coding: utf-8 -*-
# Author: Harold.Duan
# This module is unit test for sboex.di.company module.

import sys
import os

# cur_path = os.getcwd()
# print(cur_path)
path_sboex = os.path.abspath('./src')
sys.path.append(path_sboex)

from pysboex.di.company import Company
from pysboex.di.error import Error
from pysboex.di.datatypes import BoDataServerTypes, BoSuppLangs
from pysboex.di import company

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
        error = company.connect()
        assert isinstance(error,Error)
        print('ErrorCode:%i ErrorMessage:%s' % (error.error_code,error.error_message))

if __name__ == '__main__':
    test = TestClassCompany()
    test.test_connect()
    pass