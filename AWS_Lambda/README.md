# Lambda Function - AWS Lambda Service

This Lambda function is triggered by an Amazon EventBridge Rule. When triggered, it:

- Logs relevant event data to CloudWatch Logs.
- Sends an email notification to subscribers using Amazon SNS.

## Create the Lambda Function

1. Create a Lambda function named **`EBSVolumeNotifier`**.
2. Open the function and replace the default code with the contents of **`lambda_function.py`**.
3. After creating the SNS Topic, replace the value of **`TOPIC_ARN`** in the code with your SNS Topic ARN.

> **Note:** Refer to the `README.md` file in the SNS folder for SNS Topic creation steps.

---

## Configure Lambda Permissions

After creating the SNS Topic and adding a subscription:

1. Open the **`EBSVolumeNotifier`** Lambda function.
2. Navigate to:

   ```
   Configuration
   └── Permissions
       └── Execution Role
           └── Permissions Policies
               └── Add Permissions
                   └── Create Inline Policy
   ```

3. Configure the policy:

   - **Service:** SNS
   - **Actions Allowed:** Publish
   - **Resources:** Specific

4. Click **Add ARN** and provide:

   - Region
   - Topic Name
   - SNS Topic ARN

5. Click **Next**.
6. Enter the policy name:

   ```text
   ebs-sns-topic-role
   ```

7. Click **Create Policy**.

---

## Test the Lambda Function

1. Open the **EC2** service.
2. In the left menu, go to:

   ```
   Elastic Block Store
   └── Volumes
   ```

3. Click **Create Volume**.
4. Set:

   - **Volume Size:** `1 GiB`

5. Click **Create Volume**.

---

## Verify the Results

After the volume is created:

- Check your email inbox for the SNS notification.
- Open CloudWatch Logs and verify that the event details have been logged successfully.
