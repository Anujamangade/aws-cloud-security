# sns_setup.py
import boto3

def setup_sns():
    sns = boto3.client('sns')

    # Create an SNS topic
    response = sns.create_topic(Name='SecurityAlerts')
    topic_arn = response['TopicArn']
    print("SNS Topic ARN:", topic_arn)

    # Subscribe an email endpoint
    sns.subscribe(
        TopicArn=topic_arn,
        Protocol='email',
        Endpoint='your-email@example.com'
    )
    print("Subscription added. Confirm via email.")

if __name__ == "__main__":
    setup_sns()