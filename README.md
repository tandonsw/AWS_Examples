# AWS_Examples
This is a personal repository containing code examples of some medium to complex problems that I've faced while implementing stuff in the AWS Cloud

Included are the following code examples:

# Complete Nested Stack Example (Folder called 'Nested_Stack')
This example contains code for deploying a nested stack. I've included sub-stacks that have exported variables which are then used in the other stacks. 

Note: I initially had a hard time piecing out this information from AWS official documentation, but the way to sequence these nested stacks is to use the 'DependsOn' tag

# A Python Lambda Function to restart Sagemaker Notebook Instances (Folder called 'SagemakerRestartNI')

# Boto3 code to create a Sagemaker Notebook Instance

# Boto3 code to assume any role in any AWS account using STS called 'assume_role.py'

# Boto3 code to create a cloudformation stack in any AWS Account called 'cf_create_stack.py'

# Boto3 code to invoke a Lambda function in any AWS Account called 'invoke_lambda.py'

# Boto3 S3 code for putting an encrypted file on S3 called 's3_put_file_encrypted.py'





