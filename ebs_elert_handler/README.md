Lambda Function - AWS Lambda Service
This Lambda function, when triggered by an Amazon EventBridge Rule, logs the relevant data needed into the CloudWatch Logs and also sends an Email to the Subscriber using Amazon Simple Notification Service (SNS).

Create a Lambda Function with Name "EBSVolumeNotifier".
Open the Lambda function and inside code block, copy the content of lambda_function.py file.
Replace the TOPIC_ARN with SNS Topic ARN, after creating the SNS Topic.

FOr Creating the SNS Topic, Refer README.md in SNS folder.

After Creating SNS Topic and adding Subscription, follow the below steps.
1. Open the Lambda Function "EBSVolumeNotifier".
2. Under Configuration:
      Click on Permissions in the left menu.
          Under Execution Role:
              Open the Execution Role.
                  Under Permissions Policies:
                      Click Add Permissions: Create inline policy.
                          Select a Service: 
                              Service: SNS
                              Actions Allowed: Filter out and Select "Publish".
                              Resources: Specific
                              Add ARNs: 
                                  Provide the SNS Topic details like Region, Name, Resource ARN.
                              Click Add ARN.
                     Click Next.
                 Provide Policy name: ebs-sns-topic-role
                 Click Create Policy.


   Now Let's test the Lambda Function.
   Open EC2 Service. Click on Volumes under Elastic Block Store in the left menu.
   Click on Create Volume.
       Volume Size: 1G
       Click Create Volume.

   Now Check your email and also Open CLoud Watch Logs. You should see the event details.
