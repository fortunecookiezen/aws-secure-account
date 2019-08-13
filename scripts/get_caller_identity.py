import sys, boto3


def get_account_id(profile):
    session = boto3.Session(profile_name=profile)
    client = session.client("sts")
    account_id = client.get_caller_identity()["Account"]

    return account_id


if __name__ == "__main__":  # takes profile as an argument
    print(get_account_id(sys.argv[1]))
