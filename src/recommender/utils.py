import mysql.connector
import pandas as pd
import logging
from recommender.settings import DATABASE

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


class SqlConnector(object):
    def __init__(self):
        logging.info('TRY TO CONNECT TO {}..'.format(DATABASE['host']))
        self.sql_conn = mysql.connector.connect(host=DATABASE['host'],         # your host, usually localhost
                                                user=DATABASE['user'],         # your username
                                                passwd=DATABASE['password'],   # your password
                                                db=DATABASE['db'])             # name of the data base

        logging.info('CONNECTED SUCCESSFULLY TO {}!'.format(DATABASE['host']))

    def selecting_query(self):
        query = ('SELECT ' + DATABASE['target_column'] + ' FROM ' + DATABASE['db'] + '.' + DATABASE['target_table'])
        return pd.read_sql(query, self.sql_conn)
