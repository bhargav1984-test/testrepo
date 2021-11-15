from __future__ import print_function
import redshift_handler
import json

def lambda_handler(event, context):
    #insquery = '''insert into public.queue_output
    #values('123','task1','bhargav','12','inprogress')'''
    for record in event['Records']:
        print("test")
        payload = record["body"]
        print(str(payload))
        j=json.loads(payload)
        insquery='''insert into public.queue_output
        values('{0}','{1}','{2}','{3}','{4}')'''
        insquery=insquery.format(j["taskid"],j["taskdetails"],j["taskowner"],j["timelimit"],j["taskstatus"])
        print('insquery:',insquery)
        #insert_query_gp(insquery)
        redshift_handler.redshift_connect(insquery)
