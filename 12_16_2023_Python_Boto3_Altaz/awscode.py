'''
Required imports.
- boto3 for AWS
- json for all JSON processing
- datetime to get the current time
- pytz to get ensure accurate time zone
'''

import boto3
import json
from datetime import datetime
import pytz

'''
Define the tag key values which will determine if the instance needs to be 
stopped and/or started.  If the instance doesn't have these tags, the
scheduler will ignore the instance
'''
label_start_time = "SchedulerStartTime"
label_stop_time = "SchedulerStopTime"



'''
Define the s3 and ec2 boto3 client which we can use as needed
'''
Reservations
- Groups
    - GroupName: Group1
      GroupId: GroupId1
    - GroupName:Group2
      GroupId: GroupId2
- Instances
    - ImageId:
      InstanceId:
      InstanceType: t2.micro
      State:
          Code:
          Name:
      BlockDeviceMappings
                     



'''
Function to takes a specific key as input and determine the associated value
if it exists in the instance tags
'''





'''
Return a list of all of the instances that have the keys specified
'''





'''
Decide what to do with an instance, given the instance state and current time:
- if instance is running and stop_time is now, stop it
- if instance is stopped and start_time is now, start it
- in all other cases, leave the instance as is
'''






'''
Get the list of all instances that have the start and stop tags, 
then process those instances.
'''






'''
Check whether "versioning" is enabled on the specified bucket.
If not, then enable versioning.
'''






'''
Get the list of all buckets and process each one
'''





'''
Main lambda_handler.  This Lambda function should be triggered on a schedule.
We can ignore the event and context input variables.
'''
def lambda_handler(event, context):
    return
    
'''
This is put in for testing from the IDE.  If this function is not running as a
Lambda function, then __name__ will be "__main__" and we can brute force call
the lambda_handler.
'''
if __name__ == "__main__":
    lambda_handler(None, None)