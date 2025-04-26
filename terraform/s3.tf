resource "aws_s3_bucket" "static_site_bucket" {
  bucket = var.bucket_name

  tags = {
    Name = "StaticWebsiteBucket"
  }
}

resource "aws_s3_bucket_public_access_block" "bucket_access_block" {
  bucket = aws_s3_bucket.static_site_bucket.id

  block_public_acls   = false
  block_public_policy = false
  ignore_public_acls  = false
  restrict_public_buckets = false
}

