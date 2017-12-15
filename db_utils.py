import sqlite3 as sql
import logging as log
from table_types import TableType

def _init_():
    log.basicConfig(level = log.DEBUG)
    global gConn
    gConn = None
    global gCur
    gCur = None
    global dbUrl
    dbUrl = 'database.db'

def init_db():
    _init_()
    try:
        global gConn
        global gCur
        gConn = sql.connect(dbUrl)
        gCur = gConn.cursor()
        log.debug('Successfully inited DB.')
    except:
        log.error('Unable to connect to ' + dbUrl)
    
def create_table(tableType):
    tableConfig = get_table_config(tableType)
    try:
        gCur.execute('CREATE TABLE IF NOT EXISTS ' + tableConfig['name'] + ' '
                    '(' + build_fields_string(tableConfig['fields']) + ')')
        log.debug('Successfully created table "' + tableConfig['name'] + '".')
    except:
        log.error('Unable to create table "' + tableConfig['name'] + '"')

def get_table_config(tableType):
    tableTypeConfigMap = {}
    tableTypeConfigMap[TableType.TABLE] = {
            'name' : 'tables',
            'fields' : [
                    ['id', 'TEXT PRIMARY KEY'],
                    ['establishment_id', 'TEXT'],
                    ['status', 'TEXT'],
                    ['user_id', 'TEXT'],
                    ['number', 'INTEGER']
                ]
        }
    tableTypeConfigMap[TableType.ESTABLISHMENT] = {
            'name' : 'establishments',
            'fields' : [
                    ['id', 'TEXT PRIMARY KEY'],
                    ['name', 'TEXT'],
                    ['location', 'TEXT'],
                    ['description', 'TEXT'],
                    ['open_time', 'TEXT'],
                    ['end_time', 'TEXT'],
                    ['img_url', 'TEXT']
                ]
        }
    return tableTypeConfigMap[tableType]

def build_fields_string(fields):
    result = ''
    if type(fields) is list:
        count = 0
        for fieldPair in fields:
            if (type(fieldPair) is list) and len(fieldPair) == 2:
                if count > 0:
                    result += ','
                result += fieldPair[0] + ' ' + fieldPair[1]
                count += 1
    return result
        
def insert_row(tableType, params):
    tableConfig = get_table_config(tableType)
    try:
        queryStr = ('INSERT INTO ' +  tableConfig['name'] + ' (' +
            build_keys_string(params) + ') VALUES (' +
            build_values_string(params) + ')')
        print(queryStr)
        gCur.execute(queryStr)
        gConn.commit()
        log.debug("Row successfully added.")
    except sql.Error as e:
        log.error(e)
    except:
        log.error('Unable to insert row into table "' + tableConfig['name'] + '"')

def build_keys_string(params):
    result = ''
    if type(params) is list:
        count = 0
        for param in params:
            if (type(param) is list) and len(param) == 2:
                if count > 0:
                    result += ','
                result += param[0]
                count += 1
    return result

def build_values_string(params):
    result = ''
    if type(params) is list:
        count = 0
        for param in params:
            if (type(param) is list) and len(param) == 2:
                if count > 0:
                    result += ','
                result += "'" + str(param[1]) + "'"
                count += 1
    return result

def read_all_rows_from_table(tableType):
    print(tableType)
    tableConfig = get_table_config(tableType)
    print(tableConfig)
    result = None
    try:
        gConn.row_factory = sql.Row
        queryStr = 'SELECT * FROM ' + tableConfig['name']
        gCur.execute(queryStr)
        rows = gCur.fetchall();
        result = form_rows_dict(rows, tableType)
    except sql.Error as e:
        log.error(e)
    except:
        log.error('Unable to read table "' + tableConfig['name'] + '"')
    return result

def form_rows_dict(rows, tableType):
    formed_rows = []
    try:
        tableConfig = get_table_config(tableType)
        fields = tableConfig['fields']
        for row in rows:
            formed_rows.append(form_row(row, fields))
    except:
        log.error('Unable to form rows!')
    return formed_rows

def form_row(row, fields):
    result = {}
    try:
        for i in range(len(fields)):
            field = fields[i][0]
            result[field] = row[i]
    except:
        log.error('Unable to form row!')
    return result

def form_establishments_row(row):
    result = {}
    print(row)
    try:
        result['id'] = row[0]
        result['establishment_id'] = row[1]
        result['status'] = row[2]
        result['user_id'] = row[3]
    except:
        log.error('Unable to form row from "tables"!')
    return result

def read_row_from_table_by_id(tableType, id):
    tableConfig = get_table_config(tableType)
    result = None
    try:
        gConn.row_factory = sql.Row
        queryStr = ("SELECT * FROM " + tableConfig["name"] +
                    " WHERE id='" + str(id) + "'")
        gCur.execute(queryStr)
        rows = gCur.fetchall();
        result = form_rows_dict(rows, tableType)
        if not (result is None):
            result = result[0]
    except sql.Error as e:
        log.error(e)
    except:
        log.error('Unable to read table "' + tableConfig['name'] + '"')
    return result

def read_establishment_tables(id):
    result = []
    tableType = TableType.TABLE
    tableConfig = get_table_config(tableType)
    try:
        gConn.row_factory = sql.Row
        queryStr = ("SELECT * FROM " + tableConfig["name"] +
                    " WHERE establishment_id='" + str(id) + "'")
        gCur.execute(queryStr)
        rows = gCur.fetchall();
        result = form_rows_dict(rows, tableType)
    except sql.Error as e:
        log.error(e)
    except:
        log.error('Unable to read table "' + tableConfig['name'] + '"')
    return result

def update_table_status(id, status, userName):
    tableConfig = get_table_config(TableType.TABLE)
    try:
        queryStr = ("UPDATE " +  tableConfig['name'] + " SET status = '" +
            status + "', user_id = '" + userName + "'" +
            " WHERE id = '" + id + "'")
        print(queryStr)
        gCur.execute(queryStr)
        gConn.commit()
        log.debug("Row successfully added.")
    except sql.Error as e:
        log.error(e)
    except:
        log.error('Unable to insert row into table "' + tableConfig['name'] + '"')

def print_table(tableType):
    tableConfig = get_table_config(tableType)
    try:
        gConn.row_factory = sql.Row
        queryStr = 'SELECT * FROM ' + tableConfig['name']
        gCur.execute(queryStr)
        rows = gCur.fetchall();
        print_rows(tableType, rows)
    except sql.Error as e:
        log.error(e)
    except:
        log.error('Unable to print table "' + tableConfig['name'] + '"')

def print_rows(tableType, rows):
    tableTypePrintMap = {}
    tableTypePrintMap[TableType.TABLE] = print_tables_row
    try:
        printRowFunc = tableTypePrintMap[tableType]
        for row in rows:
            printRowFunc(row)
    except:
        log.error('Unable to print rows!')

def print_tables_row(row):
    try:
        print('======')
        print('id:\t\t\t%s' % row[0])
        print('establishment_id:\t%s' % row[1])
        print('status:\t\t\t%s' % row[2])
        print('user_id:\t\t%s' % row[3])
        print('======')
    except:
        log.error('Unable to print row from "tables"!')

