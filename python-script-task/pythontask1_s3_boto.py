import boto3

def list_s3_buckets():
    """List all S3 buckets in the my AWS account."""
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    print("\nList of S3 Buckets:")
    for bucket in response['Buckets']:
        print(f" - {bucket['Name']}")
    return response['Buckets']

def count_objects_in_bucket(bucket_name):
    """total number of objects in a specific S3 bucket."""
    s3 = boto3.client('s3')
    paginator = s3.get_paginator('list_objects_v2')
    page_iterator = paginator.paginate(Bucket=bucket_name)

    object_count = 0
    for page in page_iterator:
        if 'Contents' in page:
            object_count += len(page['Contents'])

    print(f"\nNumber of objects in my bucket '{bucket_name}': {object_count}")

def main():
    print("Starting AWS S3 Interaction Script...\n")

    list_s3_buckets()

    bucket_name = 'natwest-assignment-bucket'

    count_objects_in_bucket(bucket_name)

if __name__ == "__main__":
    main()
