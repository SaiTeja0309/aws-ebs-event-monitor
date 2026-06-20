# Amazon Simple Notification Service (SNS)

Amazon SNS is used to send email notifications whenever an EBS volume-related event is detected. The Lambda function publishes event details to this SNS Topic, which then delivers email alerts to all subscribed users.

## Create the SNS Topic

1. Open the **Amazon Simple Notification Service (SNS)** service in the AWS Management Console.
2. In the left menu, click **Topics**.
3. Click **Create Topic**.

4. Configure the topic:

   - **Type:** Standard
   - **Name:** `EBS-EventAlert-Topic`
   - **Display Name:** `EBSAlert`

5. Click **Create Topic**.

---

## Create an Email Subscription

1. Open the newly created **`EBS-EventAlert-Topic`**.
2. Under **Subscriptions**, click **Create Subscription**.

3. Configure the subscription:

   - **Topic ARN:** `arn:aws:sns:ap-south-2:111222333444:EBS-EventAlert-Topic`
   - **Protocol:** Email
   - **Endpoint:** Your email address

4. Click **Create Subscription**.

---

## Confirm the Subscription

1. Check the email inbox of the address provided during subscription creation.
2. Open the email sent by AWS SNS.
3. Click the **Confirm Subscription** link.

> **Note:** If the email is not visible in your inbox, check other folders such as Spam, Promotions, or Junk Mail.

---

## Next Steps

After successfully creating and confirming the SNS subscription, follow the instructions in the **Lambda Function README.md** file to:

- Configure the Lambda function.
- Grant SNS publish permissions.
- Test the complete notification workflow.
