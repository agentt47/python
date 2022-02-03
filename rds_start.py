import boto3

#connect ot rds instance
client = boto3.client('rds')

#rds_instance will have all rds information in dictionary.
rds_instance = client.describe_db_instances()
start_Instance_name = []
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
    if dbInstanceStatus == 'stopped':
       start_Instance_name.append(dbInstanceName)

   # else:
   #     print('No RDS To Stop ... Exiting')
   #     exit()

print(start_Instance_name)

if len(start_Instance_name) == 0:
    print('No RDS To Start... Exiting')

else:
  for i in start_Instance_name:
     client.start_db_instance(DBInstanceIdentifier=i)
     print('Starting RDS Instance ... Triggered By Lambda Function')
