# guardduty_setup.py
import boto3

def setup_guardduty():
    guardduty = boto3.client('guardduty')

    response = guardduty.create_detector(Enable=True)
    detector_id = response['DetectorId']
    print("GuardDuty enabled with Detector ID:", detector_id)

if __name__ == "__main__":
    setup_guardduty()