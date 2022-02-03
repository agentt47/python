import boto3

#connect ot rds instance
client = boto3.client('rds')

#rds_instance will have all rds information in dictionary.
rds_instance = client.describe_db_instances()


#print('RDS Instance Name \t| Instance Type \t| Status \t | ARN')

for i in rds_instance['DBInstances']:
    dbInstanceName = i['DBInstanceIdentifier']
    dbInstanceStatus = i['DBInstanceStatus']
    dbInstancearn = i['DBInstanceArn']
    resp2=client.list_tags_for_resource(ResourceName=dbInstancearn)
 #   print('%s \t| %s \t| %s \t| %s \t| %s' %(dbInstanceName, dbInstanceEngine, dbInstanceStatus, dbInstancearn, resp2))
    if 0==len(resp2['TagList']):
                   # print('DB Instance {0} is not part of autoshutdown'.format(i['DBInstanceIdentifier']))
                    print('DB Instance {0} is not part of autoshutdown'.format(dbInstanceName))
    else:
         for tag in resp2['TagList']:
#If the tags match, then stop the instances by validating the current status.
            if tag['Key']=='Name' and tag['Value']=='auto-stop':
                if i['DBInstanceStatus'] == 'stopped':
                    # client.start_db_instance(DBInstanceIdentifier = i['DBInstanceIdentifier'])
                     client.start_db_instance(DBInstanceIdentifier = dbInstanceName)
                    # print('starting DB instance {0}'.format(i['DBInstanceIdentifier']))
                     print('starting DB instance {0}'.format(dbInstanceName)) 
                elif i['DBInstanceStatus'] == 'available':
                     print('DB Instance {0} is already available'.format(i['DBInstanceIdentifier']))

