# AWS EBS Volume Event Alert System

This project provides a complete event-driven monitoring solution for Amazon EBS volumes using AWS managed services.

Whenever an EBS volume is **created**, **modified**, or **deleted**, an Amazon EventBridge rule automatically triggers an AWS Lambda function. The Lambda function logs the event details to CloudWatch Logs and sends an email notification using Amazon SNS.

## Architecture

```text
EBS Volume Event
        │
        ▼
Amazon EventBridge
        │
        ▼
AWS Lambda (EBSVolumeNotifier)
        │
        ├── CloudWatch Logs
        │
        └── Amazon SNS
                │
                ▼
          Email Notification
```

## Services Used

- Amazon EC2 (EBS Volumes)
- Amazon EventBridge
- AWS Lambda
- Amazon SNS
- Amazon CloudWatch Logs

## Project Structure

```text
.
├── Lambda/
│   ├── lambda_function.py
│   └── README.md
│
├── SNS/
│   └── README.md
│
├── EventBridge/
│   └── README.md
│
└── README.md
```

## Use Case

This solution helps administrators and cloud engineers monitor EBS volume activities in real time.

Whenever any of the following events occur:

- `createVolume`
- `modifyVolume`
- `deleteVolume`

the system automatically:

1. Captures the event using EventBridge.
2. Triggers the Lambda function.
3. Logs the event details to CloudWatch Logs.
4. Sends an email notification to subscribed users through SNS.

## Deployment Order

Follow the setup steps in the following order:

### Step 1 - Create SNS Topic

Configure the SNS Topic and email subscription.

📖 Refer to:

```text
SNS/README.md
```

### Step 2 - Create Lambda Function

Create the Lambda function and configure SNS publishing permissions.

📖 Refer to:

```text
Lambda/README.md
```

### Step 3 - Create EventBridge Rule

Configure EventBridge to trigger the Lambda function on EBS volume events.

📖 Refer to:

```text
EventBridge/README.md
```

## Testing

After completing the setup:

1. Open the EC2 service.
2. Navigate to:

   ```text
   Elastic Block Store
   └── Volumes
   ```

3. Create a new EBS volume.
4. Verify that:

   - An email notification is received.
   - Event details are available in CloudWatch Logs.

## Expected Outcome

When an EBS volume is created, modified, or deleted:

- EventBridge captures the event.
- Lambda processes the event.
- CloudWatch stores the logs.
- SNS sends an email notification.

This creates a simple, serverless, and fully managed AWS event monitoring workflow.

## Cleanup

To avoid unnecessary AWS charges, delete the following resources when testing is complete:

- EventBridge Rule
- Lambda Function
- SNS Topic and Subscription
- Test EBS Volumes
- Associated CloudWatch Log Groups

## Author

This project demonstrates how to build a serverless event-driven notification system using AWS services.
