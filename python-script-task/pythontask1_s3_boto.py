import boto3

def list_s3_buckets():
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    print("\nList of S3 Buckets:")
    for bucket in response['Buckets']:
        print(f" - {bucket['Name']}")
    return [bucket['Name'] for bucket in response['Buckets']]

def count_objects_in_bucket(bucket_name):
    s3 = boto3.client('s3')
    paginator = s3.get_paginator('list_objects_v2')
    page_iterator = paginator.paginate(Bucket=bucket_name)

    object_count = 0
    for page in page_iterator:
        if 'Contents' in page:
            object_count += len(page['Contents'])

    print(f"\nNumber of objects in the bucket '{bucket_name}': {object_count}")

def main():

    bucket_names = list_s3_buckets()

    selected_bucket = input("\nEnter the bucket name you want to inspect: ").strip()

    if selected_bucket in bucket_names:
        count_objects_in_bucket(selected_bucket)
    else:
        print(f"\nThe bucket '{selected_bucket}' does not exist in your AWS account!")

if __name__ == "__main__":
    main()
