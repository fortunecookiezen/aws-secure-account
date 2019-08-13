import json, sys, boto3


def get_account_id(profile):
    session = boto3.Session(profile_name=profile)
    client = session.client("sts")
    account_id = client.get_caller_identity()["Account"]

    return account_id


def print_bucket_policy(profile):
    session = boto3.Session(profile_name=profile)
    client = session.client("s3control", region_name="us-east-1")

    response = client.delete_public_access_block(AccountId=get_account_id(profile))
    print(json.dumps(response, indent=4))


if (
    __name__ == "__main__"
):  # takes profile_name as an argument. this could be done simpler, but I use profiles.
    print_bucket_policy(sys.argv[1])
