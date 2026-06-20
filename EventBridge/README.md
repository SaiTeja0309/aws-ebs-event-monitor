Amazon EventBridge

Create an Amazon EventBridge which Triggers the Lambda function on a EBS Volume Event, like createVolume, deleteVolume, etc..

1. In the AWS Management Console, Open Amazon EventBridge Service. Go to Rules section in the left menu.
2. Click on Create Rule.
3. Define Rule Details.
    Name: EBS-Volume-Event-alert-rule
    Description: This Rule triggers a Lambda Function on an EBS Volume Event.
    Event Bus: Default
4. Click Next. Provide Build event pattern. 
    Under Events :
       Event Source: AWS events or EventBridge partner events
   Under Event pattern :
       Event source: AWS Services
       AWS service: EC2
       Event type: EBS Volume Notification
       Event Type Specification 1 : Specific Events
           Specific Events: Select createVolume, modifyVolume, deleteVolume
       Event Type Specification 2 : Any volume ARN
       
    The JSON looks like below:
    {
      "source": ["aws.ec2"],
      "detail-type": ["EBS Volume Notification"],
      "detail": {
           "event": ["createVolume", "modifyVolume", "deleteVolume"]
       }
    }

5. Click Next. Now Select target(s).
     Under Target 1:
         Target types: AWS Service
         Select a target: Lambda Function
         Target Location: Target in this account
         Function: EBSVolumeNotifier
         ExecutionRole: Create a new execution role for this specific resource.
         Role Name: Leave it to default or give a custom Role Name.
6. Click Next. Add Tags - Optional.
7. Click Next. Review and Create.
8. Click Create Rule.
         
