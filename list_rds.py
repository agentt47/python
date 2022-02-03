import boto3

#connect ot rds instance
client = boto3.client('rds')

#rds_instance will have all rds information in dictionary.
rds_instance = client.describe_db_instances()

#print(rds_instance)
all_list = rds_instance['DBInstances']

#print(all_list)

print('RDS Instance Name \t| Instance Type \t| Status \t | ARN')

for i in rds_instance['DBInstances']:
    dbInstanceName = i['DBInstanceIdentifier']
    dbInstanceEngine = i['DBInstanceClass']
    dbInstanceStatus = i['DBInstanceStatus']
    dbInstancearn = i['DBInstanceArn']
    resp2=client.list_tags_for_resource(ResourceName=dbInstancearn)
    print('%s \t| %s \t| %s \t| %s \t| %s' %(dbInstanceName, dbInstanceEngine, dbInstanceStatus, dbInstancearn, resp2))
    if 0==len(resp2['TagList']):
                    print('DB Instance {0} is not part of autoshutdown'.format(i['DBInstanceIdentifier']))
    else:
         for tag in resp2['TagList']:
#If the tags match, then stop the instances by validating the current status.
            if tag['Key']=='Name' and tag['Value']=='auto-stop':
                if i['DBInstanceStatus'] == 'available':
                     client.stop_db_instance(DBInstanceIdentifier = i['DBInstanceIdentifier'])
                     print('stopping DB instance {0}'.format(i['DBInstanceIdentifier']))
                elif i['DBInstanceStatus'] == 'stopped':
                     print('DB Instance {0} is already stopped'.format(i['DBInstanceIdentifier']))
#resp2=client.list_tags_for_resource(ResourceName=dbInstancearn)
#print(resp2)
