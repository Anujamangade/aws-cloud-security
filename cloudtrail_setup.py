# cloudtrail_setup.py
import boto3

def setup_cloudtrail():
    cloudtrail = boto3.client('cloudtrail')

    response = cloudtrail.create_trail(
        Name='SecurityTrail',
        S3BucketName='my-cloudtrail-logs',
        IsMultiRegionTrail=True
    )
    print("Trail created:", response)

    cloudtrail.start_logging(Name='SecurityTrail')
    print("CloudTrail logging started.")

if __name__ == "__main__":
    setup_cloudtrail()