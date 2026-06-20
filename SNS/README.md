Amazon Simple Notification Service

1. In AWS Management Console, Open Amazon Simple Notification Service.
2. Click on Topics in the left menu.
3. Click on Create Topic. 
    Details:
        Type: Standard
        Name: EBS-EventAlert-Topic
        Display name : EBSAlert
4. Click Create Topic.

5. Open the "EBS-EventAlert-Topic" topic which we just created.
6. Under Subscriptions: 
    Click Create Subscription:
        Details:
            Name: arn:aws:sns:ap-south-2:111222333444:EBS-EventAlert-Topic
            Protocol: Email
            Endpoint: Provide your email address.
    Click Create Subscription.
7. AWS has Sent you a mail on the provided email address. Click on Confirm Subscription link in that mail. (If mail not found in inbox, check other folders like spam etc..)
8. Check Lambda Function README.md file for further steps.
