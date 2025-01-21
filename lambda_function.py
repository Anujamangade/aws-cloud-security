# lambda_function.py
import boto3

def lambda_handler(event, context):
    guardduty = boto3.client('guardduty')
    iam = boto3.client('iam')

    for record in event['Records']:
        finding = record['Sns']['Message']
        print("Finding:", finding)

        # Example: Disable compromised IAM user access keys
        if 'UnauthorizedAccess:IAMUser' in finding:
            user_name = 'ExtractedFromFinding'  # Extract username from the finding
            print(f"Disabling access keys for user: {user_name}")

            # List and deactivate keys
            response = iam.list_access_keys(UserName=user_name)
            for key in response['AccessKeyMetadata']:
                access_key_id = key['AccessKeyId']
                iam.update_access_key(
                    UserName=user_name,
                    AccessKeyId=access_key_id,
                    Status='Inactive'
                )
                print(f"Deactivated key: {access_key_id}")

    return {"statusCode": 200, "message": "Lambda executed successfully."}