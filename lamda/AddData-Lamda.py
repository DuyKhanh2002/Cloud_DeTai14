import sys
import logging
import pymysql
import json
from urllib.parse import unquote

#rds settings

rds_host = "database-test3306.clcqijtl2xor.us-east-1.rds.amazonaws.com"
name = "admin"
password = "12345678"
db_name = "ManageUser"

logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    conn = pymysql.connect(host=rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
except pymysql.MySQLError as e:
    logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
    logger.error(e)
    sys.exit()

logger.info("SUCCESS: Connection to RDS MySQL instance succeeded")

def lambda_handler(event, context):
    data = event['Records'][0]['body']
    data = unquote(data)
    data = data.replace("\'", "\"")
    
    data = json.loads(data)
    print(data)
    getData = str(data['query'])
    newStr = getData.replace('$', '"')
    print(newStr)
    response = add_data_table(data)

def add_data_table(event):
    try:
        with conn.cursor() as cur:
            str = event['query']
            newStr = str.replace('$', '"')
            print(newStr)
            cur.execute(newStr)
        conn.commit()
    except Exception as e: print(e)

