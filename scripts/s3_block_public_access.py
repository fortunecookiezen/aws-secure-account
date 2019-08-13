import sys, boto3


def get_account_id(profile):
    session = boto3.Session(profile_name=profile)
    client = session.client("sts")
    account_id = client.get_caller_identity()["Account"]

    return account_id


def secure_buckets(profile):
    session = boto3.Session(profile_name=profile)
    client = session.client("s3control", region_name="us-east-1")

    response = client.put_public_access_block(
        PublicAccessBlockConfiguration={
            "BlockPublicAcls": True,
            "IgnorePublicAcls": True,
            "BlockPublicPolicy": True,
            "RestrictPublicBuckets": True,
        },
        AccountId=get_account_id(profile),
    )

    print(response)


if (
    __name__ == "__main__"
):  # takes profile_name as an argument. this could be done simpler, but I use profiles.
    secure_buckets(sys.argv[1])
