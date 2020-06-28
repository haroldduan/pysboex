# -*- coding: utf-8 -*-
# Author: Harold.Duan
# This module is sbo Company implements.

__version__ = "0.0.1.dev"
__author__ = "Harold.Duan"
__all__ = ['Company']

from .error import Error
from .datatypes import BoDataServerTypes, BoSuppLangs, BoObjectTypes
import os
from win32com import client


class Company(object):
    ''' define Company Repository class '''

    def __init__(self):
        ''' constructor '''
        try:
            # self.__db_server_type: BoDataServerTypes
            # self.__server: str
            # self.__license_server: str
            # self.__company_db: str
            # self.__db_user_name: str
            # self.__db_password: str
            # self.__lanuage: BoSuppLangs
            # self.__user_name: str
            # self.__password: str
            # self.__sld_server: str
            # self.__is_connected: bool = False
            # self.__company_name: str = ''
            # self.__sbo_company: str = ''
            self.__db_server_type = BoDataServerTypes.NONE
            self.__server = ''
            self.__license_server = ''
            self.__company_db = ''
            self.__db_user_name = ''
            self.__db_password = ''
            self.__lanuage = BoSuppLangs.NULL
            self.__user_name = ''
            self.__password = ''
            self.__sld_server = ''
            self.__is_connected = False
            self.__company_name = ''
            self.__sbo_company = ''
            pass
        except Exception as e:
            raise e

    @property
    def db_server_type(self) -> BoDataServerTypes:
        return self.__db_server_type

    @db_server_type.setter
    def db_server_type(self, value: BoDataServerTypes):
        self.__db_server_type = value

    @property
    def server(self) -> str:
        return self.__server

    @server.setter
    def server(self, value: str):
        self.__server = value

    @property
    def license_server(self) -> str:
        return self.__license_server

    @license_server.setter
    def license_server(self, value: str):
        self.__license_server = value

    @property
    def company_db(self) -> str:
        return self.__company_db

    @company_db.setter
    def company_db(self, value: str):
        self.__company_db = value

    @property
    def db_user_name(self) -> str:
        return self.__db_user_name

    @db_user_name.setter
    def db_user_name(self, value: str):
        self.__db_user_name = value

    @property
    def db_password(self) -> str:
        return self.__db_password

    @db_password.setter
    def db_password(self, value: str):
        self.__db_password = value

    @property
    def language(self) -> BoSuppLangs:
        return self.__lanuage

    @language.setter
    def language(self, value: BoSuppLangs):
        self.__lanuage = value

    @property
    def user_name(self) -> str:
        return self.__user_name

    @user_name.setter
    def user_name(self, value: str):
        self.__user_name = value

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, value: str):
        self.__password = value

    @property
    def sld_server(self) -> str:
        return self.__sld_server

    @sld_server.setter
    def sld_server(self, value: str):
        self.__sld_server = value

    @property
    def is_connected(self) -> bool:
        return self.__is_connected

    @property
    def company_name(self) -> str:
        return self.__company_name

    def connect(self) -> Error:
        ''' connect sbo company instance '''
        err = Error()
        try:
            if not self.__is_connected:
                print(os.getcwd())
                # print(sys.path)
                # clr.FindAssembly('Interop.SAPbobsCOM.x86.dll')
                # from SAPbobsCOM import *
                # cur_path = os.path.abspath('./net')
                # sys.path.append(cur_path)
                # clr.AddReference('Interop.SAPbobsCOM.x86')
                # from SAPbobsCOM import Company
                # cmp = Company()
                if not self.__sbo_company:
                    self.__sbo_company = client.Dispatch('SAPBobsCOM.Company')
                self.__sbo_company.DbServerType = self.__db_server_type
                self.__sbo_company.Server = self.__server
                self.__sbo_company.LicenseServer = self.__license_server
                self.__sbo_company.CompanyDB = self.__company_db
                self.__sbo_company.DbUserName = self.__db_user_name
                self.__sbo_company.DbPassword = self.__db_password
                self.__sbo_company.Language = self.__lanuage
                self.__sbo_company.UserName = self.__user_name
                self.__sbo_company.Password = self.__password
                self.__sbo_company.SLDServer = self.__sld_server
                err_code = self.__sbo_company.Connect()
                if err_code != 0:
                    err_msg = self.__sbo_company.GetLastErrorDescription()
                    err = Error(err_code, err_msg)
                else:
                    self.__is_connected = True
                    self.__company_name = self.__sbo_company.CompanyName
            return err
        except Exception as e:
            raise e

    def disconnect(self):
        ''' disconnect sbo company instance '''
        try:
            if self.is_connected:
                if self.__sbo_company:
                    if self.__sbo_company.Connected:
                        self.__sbo_company.Disconnect()
        except Exception as e:
            raise e
        finally:
            self.__is_connected = False
            self.__db_server_type = 0
            self.__server = ''
            self.__license_server = ''
            self.__company_db = ''
            self.__db_user_name = ''
            self.__db_password = ''
            self.__lanuage = 0
            self.__user_name = ''
            self.__password = ''
            self.__sld_server = ''
            self.__company_name = ''
            self.__sbo_company = None

    def get_business_object(self, sbo_obj_type=BoObjectTypes.NONE):
        ''' Get SBO business object '''
        try:
            if not self.__sbo_company:
                raise Exception('SBO Company instance is invalid!')
            else:
                if not isinstance(sbo_obj_type, BoObjectTypes):
                    raise Exception('sbo_obj_type is invalid type.')
                else:
                    if sbo_obj_type == BoObjectTypes.NONE:
                        raise Exception(
                            'sbo_obj_type must not be Default or None.')
                    else:
                        return self.__sbo_company.GetBusinessObject(sbo_obj_type)
        except Exception as e:
            raise e

    def get_last_error_description(self) -> str:
        ''' Get SBO business object '''
        try:
            err_desc = self.__sbo_company.GetLastErrorDescription()
            return err_desc
        except Exception as e:
            raise e
