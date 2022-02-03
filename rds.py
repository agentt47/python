import boto3

client = boto3.client('rds')

filter_tag=[
        {
            'Name': 'tag:Env',
            'Values': ['non-prod' ]
        }
 ]



#response = client.describe_db_instances(Filters=filter_tag)
#response = client.describe_db_instances()
#print(response)

rdsInstances = ['database-1']
client.stop_db_instance(DBInstanceIdentifier=rdsInstances[0])
