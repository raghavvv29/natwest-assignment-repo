variable "aws_region" {
  description = "AWS Region:"
}

variable "instance_type" {
  description = "EC2 Instance Type:"
}

variable "key_name" {
  description = "Enter SSH Key Name:"
}

variable "my_ip" {
  description = "Which IP you want to restrict SSH to?"
}

variable "bucket_name" {
  description = "Enter Bucket Name for static website hosting:"
}

variable "lambda_function_name" {
  description = "Name of the Lambda function:"
}

