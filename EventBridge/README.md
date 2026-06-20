# Amazon EventBridge

Amazon EventBridge is used to monitor EBS volume events and automatically trigger the Lambda function whenever a volume is created, modified, or deleted.

## Create an EventBridge Rule

1. Open the **Amazon EventBridge** service in the AWS Management Console.
2. In the left menu, select **Rules**.
3. Click **Create Rule**.

---

## Define Rule Details

Configure the rule with the following values:

- **Name:** `EBS-Volume-Event-alert-rule`
- **Description:** Triggers the Lambda function whenever an EBS volume event occurs.
- **Event Bus:** `default`

4. Click **Next**.

---

## Build the Event Pattern

### Events

- **Event Source:** AWS events or EventBridge partner events

### Event Pattern

- **Event Source:** AWS Services
- **AWS Service:** EC2
- **Event Type:** EBS Volume Notification

### Event Type Specification 1

- **Specific Events**
  - `createVolume`
  - `modifyVolume`
  - `deleteVolume`

### Event Type Specification 2

- **Any Volume ARN**

The generated event pattern should look similar to:

```json
{
  "source": ["aws.ec2"],
  "detail-type": ["EBS Volume Notification"],
  "detail": {
    "event": [
      "createVolume",
      "modifyVolume",
      "deleteVolume"
    ]
  }
}
```

5. Click **Next**.

---

## Configure the Target

Under **Target 1**, configure the following:

- **Target Type:** AWS Service
- **Select a Target:** Lambda Function
- **Target Location:** Target in this account
- **Function:** `EBSVolumeNotifier`
- **Execution Role:** Create a new execution role for this specific resource
- **Role Name:** Leave the default value or provide a custom name

6. Click **Next**.

---

## Review and Create

1. (Optional) Add tags if required.
2. Click **Next**.
3. Review the configuration.
4. Click **Create Rule**.

---

## Result

The EventBridge rule is now configured to automatically trigger the **`EBSVolumeNotifier`** Lambda function whenever any of the following EBS volume events occur:

- `createVolume`
- `modifyVolume`
- `deleteVolume`

The Lambda function will then log the event details to CloudWatch Logs and send email notifications through SNS.
