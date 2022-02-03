import boto3
import logging

#setup simple logging for INFO
logger = logging.getLogger()
logger.setLevel(logging.INFO)

#define the connection
ec2 = boto3.resource('ec2', region_name='us-east-1')


# all stopped EC2 instances.
filters = [#{
           # 'Name': 'tag:OS',
           # 'Values': ['Amazon']
       # },
        {
            'Name': 'instance-state-name', 
            'Values': ['stopped']
        }
    ]
    
    #filter the instances
instances = ec2.instances.filter(Filters=filters)
#print(instances)

    #locate all stopped instances
RunningInstances = [instance.id for instance in instances]
    
print(RunningInstances)
