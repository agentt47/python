import boto3

import logging

#setup simple logging for INFO
logger = logging.getLogger()
logger.setLevel(logging.INFO)

#connect ot rds instance
client = boto3.client('rds')

#rds_instance will have all rds information in dictionary.
rds_instance = client.describe_db_instances()
stop_Instance_name = []
#print(type(rds_instance))
#print(rds_instance['DBInstances'])
#all_list = rds_instance['DBInstances']

#print(type(all_list))
#print(all_list[1]['DBInstanceStatus'])

#print('RDS Instance Name \t| Instance Type \t| Status')

for i in rds_instance['DBInstances']:
   # print(i)
    dbInstanceName = i['DBInstanceIdentifier']
    dbInstanceEngine = i['DBInstanceClass']
    dbInstanceStatus = i['DBInstanceStatus']
    #print('%s \t| %s \t| %s' %(dbInstanceName, dbInstanceEngine, dbInstanceStatus))
    if dbInstanceStatus == 'available':
       stop_Instance_name.append(dbInstanceName)

   # else:
   #     print('No RDS To Stop ... Exiting')
   #     exit()

print(stop_Instance_name)

if len(stop_Instance_name) == 0:
    print('No RDS To Stop ... Exiting')

else:
  for i in stop_Instance_name:
     client.stop_db_instance(DBInstanceIdentifier=i)
     print('Stopping RDS Instance ... Triggered By Lambda Function')

