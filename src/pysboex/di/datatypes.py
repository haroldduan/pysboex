# -*- coding: utf-8 -*-
# Author: Harold.Duan
# This module is sbo enum colletions.

from enum import Enum, IntEnum, unique


class SBOCOMClass(Enum):
    ''' SBO Business Class Types list '''

    NONE = ''
    COMPANY = 'SAPBobsCOM.Company'
    ITEMS = 'SAPBobsCOM.Items'

    def __str__(self):
        ''' str() function implement '''
        return self.value


class BoDataServerTypes(IntEnum):
    ''' SBO Business Class Types list '''

    NONE = 0
    MSSQL = 1  # Microsoft SQL Server 2000 (Not Supported from 8.8)
    DB_2 = 2  # DB2 (Not Supported from 8.8)
    SYBASE = 3  # Sybase (Not Supported from 8.8)
    MSSQL2005 = 4  # Microsoft SQL Server 2005
    MAXDB = 5  # MaxDB (Not Supported from 8.8)
    MSSQL2008 = 6  # Microsoft SQL Server 2008
    MSSQL2012 = 7  # Microsoft SQL Server 2012
    MSSQL2014 = 8  # Microsoft SQL Server 2014
    HANADB = 9  # SAP HANA Platform Edition 1.0
    MSSQL2016 = 10  # Microsoft SQL Server 2016
    MSSQL2017 = 11  # Microsoft SQL Server 2017


class BoObjectTypes(IntEnum):
    ''' SBO Business Object Types list '''

    NONE = 0
    CHART_OF_ACCOUNTS = 1
    BUSINESS_PARTNERS = 2
    BANKS = 3
    ITEMS = 4
    VAT_GROUPS = 5
    PRICE_LISTS = 6
    SPECIAL_PRICES = 7
    ITEM_PROPERTIES = 8
    USERS = 12
    INVOICES = 13
    CREDIT_NOTES = 14
    DELIVERY_NOTES = 15
    RETURNS = 16
    ORDERS = 17
    PURCHASE_INVOICES = 18
    PURCHASE_CREDIT_NOTES = 19
    PURCHASE_DELIVERY_NOTES = 20
    PURCHASE_RETURNS = 21
    PURCHASE_ORDERS = 22
    QUOTATIONS = 23
    INCOMING_PAYMENTS = 24
    JOURNAL_VOUCHERS = 28
    JOURNAL_ENTRIES = 30
    STOCK_TAKINGS = 31
    CONTACTS = 33
    CREDIT_CARDS = 36
    CURRENCY_CODES = 37
    PAYMENT_TERMS_TYPES = 40
    BANK_PAGES = 42
    MANUFACTURERS = 43
    OVENDOR_PAYMENTS = 46
    LANDED_COST_SCODES = 48
    SHIPPING_TYPES = 49
    LENGTH_MEASURES = 50
    WEIGHT_MEASURES = 51
    ITEM_GROUPS = 52
    SALES_PERSONS = 53
    CUSTOMS_GROUPS = 56
    CHECKSFOR_PAYMENT = 57
    INVENTORY_GEN_ENTRY = 59
    INVENTORY_GEN_EXIT = 60
    WAREHOUSES = 64
    COMMISSION_GROUPS = 65
    PRODUCT_TREES = 66
    STOCK_TRANSFER = 67
    WORK_ORDERS = 68
    CREDIT_PAYMENT_METHODS = 70
    CREDIT_CARD_PAYMENTS = 71
    ALTERNATE_CAT_NUM = 73
    BUDGET = 77
    BUDGET_DISTRIBUTION = 78
    MESSAGES = 81
    BUDGET_SCENARIOS = 91
    SALES_OPPORTUNITIES = 97
    USER_DEFAULT_GROUPS = 93
    SALES_STAGES = 101
    ACTIVITY_TYPES = 103
    ACTIVITY_LOCATIONS = 104
    DRAFTS = 112
    DEDUCTION_TAX_HIERARCHIES = 116
    DEDUCTION_TAX_GROUPS = 117
    ADDITIONAL_EXPENSES = 125
    SALES_TAX_AUTHORITIES = 126
    SALES_TAX_AUTHORITIES_TYPES = 127
    SALES_TAX_CODES = 128
    QUERY_CATEGORIES = 134
    FACTORING_INDICATORS = 138
    PAYMENTS_DRAFTS = 140
    ACCOUNT_SEGMENTATIONS = 142
    ACCOUNT_SEGMENTATION_CATEGORIES = 143
    WAREHOUSE_LOCATIONS = 144
    FORMS1099 = 145
    INVENTORY_CYCLES = 146
    WIZARD_PAYMENT_METHODS = 147
    B_P_PRIORITIES = 150
    DUNNING_LETTERS = 151
    USER_FIELDS = 152
    USER_TABLES = 153
    PICK_LISTS = 156
    PAYMENT_RUN_EXPORT = 158
    USER_QUERIES = 160
    MATERIAL_REVALUATION = 162
    CORRECTION_PURCHASE_INVOICE = 163
    CORRECTION_PURCHASE_INVOIC_EREVERSAL = 164
    CORRECTION_INVOICE = 165
    CORRECTION_INVOICE_REVERSAL = 166
    CONTRACT_TEMPLATES = 170
    EMPLOYEES_INFO = 171
    CUSTOMER_EQUIPMENT_CARDS = 176
    WITHHOLDING_TAX_CODES = 178
    BILL_OF_EXCHANGE_TRANSACTIONS = 182
    KNOWLEDGE_BASE_SOLUTIONS = 189
    SERVICE_CONTRACTS = 190
    SERVICE_CALLS = 191
    USER_KEYS = 193
    QUEUE = 194
    SALES_FORECAST = 198
    TERRITORIES = 200
    INDUSTRIES = 201
    PRODUCTION_ORDERS = 202
    PACKAGES_TYPES = 205
    USER_OBJECTS_M_D = 206
    TEAMS = 211
    RELATIONSHIPS = 212
    USER_PERMISSION_TREE = 214
    ACTIVITY_STATUS = 217
    CHOOSE_FROM_LIST = 218
    FORMATTED_SEARCHES = 219
    ATTACHMENTS2 = 221
    USER_LANGUAGES = 223
    MULTI_LANGUAGE_TRANSLATIONS = 224
    DYNAMIC_SYSTEM_STRINGS = 229
    HOUSE_BANK_ACCOUNTS = 231
    BUSINESS_PLACES = 247
    LOCAL_ERA = 250
    SALES_TAX_INVOICE = 280
    PURCHASE_TAX_INVOICE = 281
    BO_RECORDSET = 300
    BO_RECORDSET_EX = 301
    BO_BRIDGE = 305
    NOTA_FISCAL_USAGE = 260
    NOTA_FISCAL_C_F_O_P = 258
    NOTA_FISCAL_C_S_T = 259
    CLOSING_DATE_PROCEDURE = 261
    BUSINESS_PARTNER_GROUPS = 10
    B_P_FISCAL_REGISTRY_ID = 278
    DOWN_PAYMENTS = 203
    PURCHASE_DOWN_PAYMENTS = 204
    STOCK_TRANSFER_DRAFT = 1179
    PURCHASE_QUOTATIONS = 540000006
    INVENTORY_TRANSFER_REQUEST = 1250000001
    PURCHASE_REQUEST = 1470000113
    RETURN_REQUEST = 234000031
    GOODS_RETURN_REQUEST = 234000032


class BoSuppLangs(IntEnum):
    ''' Defines the current resource language lists '''

    NULL = 0
    HEBREW = 1  # Hebrew
    SPANISH_AR = 2  # Spanish (Argentina)
    ENGLISH = 3  # English (US)
    POLISH = 5  # Polish
    ENGLISH_SG = 6  # English (Singapore)
    SPANISH_PA = 7  # Spanish (Panama)
    ENGLISH_GB = 8  # English (Great Britain)
    GERMAN = 9  # German
    SERBIAN = 10  # Serbian
    DANISH = 11  # Danish
    NORWEGIAN = 12  # Norwegian
    ITALIAN = 13  # Italian
    HUNGARIAN = 14  # Hungarian
    CHINESE = 15  # Chinese
    DUTCH = 16  # Dutch
    FINNISH = 17  # Finnish
    GREEK = 18  # Greek *
    PORTUGUESE = 19  # Portuguese
    SWEDISH = 20  # Swedish
    ENGLISH_CY = 21  # English (Cyprus) *
    FRENCH = 22  # French
    SPANISH = 23  # Spanish
    RUSSIAN = 24  # Russian *
    SPANISH_LA = 25  # Spanish (Latin America)
    CZECH_CZ = 26  # Czech (Czech) *
    SLOVAK_SK = 27  # Slovak (Slovakia) *
    KOREAN_KR = 28  # Korean (Korea) *
    PORTUGUESE_BR = 29  # Portuguese (Brazil) *
    JAPANESE_JP = 30  # Japanese (Japan) *
    TURKISH_TR = 31  # Turkish (Turky) *
    ARABIC = 32
    UKRAINIAN = 33
    TRDTNLCHINESE_HK = 35  # Traditional Chinese (China) *
