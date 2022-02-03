import boto3

#connect ot rds instance
client = boto3.client('rds')

#rds_instance will have all rds information in dictionary.
rds_instance = client.describe_db_instances()

for i in rds_instance['DBInstances']:
    dbInstanceName = i['DBInstanceIdentifier']
    dbInstanceStatus = i['DBInstanceStatus']
    dbInstancearn = i['DBInstanceArn']
    tags=client.list_tags_for_resource(ResourceName=dbInstancearn)
    if 0==len(tags['TagList']):
        print('DB Instance {0} is not part of autoshutdown'.format(dbInstanceName))
    else:
        for tag in tags['TagList']:
#If the tags match, then start the instances by validating the current status.
            if tag['Key']=='Name' and tag['Value']=='auto-stop':
                if dbInstanceStatus == 'stopped':
                     client.start_db_instance(DBInstanceIdentifier = dbInstanceName)
                     print('starting DB instance {0}'.format(dbInstanceName))
                elif dbInstanceStatus == 'available':
                     print('DB Instance {0} is already available'.format(dbInstanceName))

