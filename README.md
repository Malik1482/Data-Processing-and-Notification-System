                      <.All these commands work only on the command window/terminal.>


verify-email comand :
aws ses verify-email-identity --email-address "your email" --region ap-south-1
 
THIS COMND CHEK YOUR FILE SENTEX IS VOLD
aws cloudformation validate-template --template-body file://Secrets_Manager.yaml --region ap-south-1



if stack delete then use this command 
aws cloudformation delete-stack --stack-name tcLambdaFunction --region ap-south-1


deployment comand for VPC :
aws cloudformation deploy --template-file VPC.yaml --stack-name tcVPC --capabilities CAPABILITY_NAMED_IAM --region ap-south-1

deployment comand for Security_Group :
aws cloudformation deploy --template-file Security_Group.yaml --stack-name tcSecurityGroup --capabilities CAPABILITY_NAMED_IAM --region ap-south-1

deployment comand for Secrets_Manager :
aws cloudformation deploy --template-file Secrets_Manager.yaml --stack-name tcSecretsManager --capabilities CAPABILITY_NAMED_IAM --region ap-south-1 --parameter-overrides DBUsername=dbadmin DBPassword=MyPassword123

deployment comand for Lambda_IAM_Role :
aws cloudformation deploy --template-file Lambda_IAM_Role.yaml --stack-name tcLambdaIAMRole --capabilities CAPABILITY_NAMED_IAM --region ap-south-1

deployment comand for SNS_Topic:
aws cloudformation deploy --template-file SNS_Topic.yaml --stack-name tcSNSTopic --capabilities CAPABILITY_NAMED_IAM --region ap-south-1 --parameter-overrides EmailSubscriber="your email"

Deploment comand for RDS :
aws cloudformation deploy --template-file RDS.yaml --stack-name tcRDS --capabilities CAPABILITY_NAMED_IAM --region ap-south-1 --parameter-overrides DBUsername=dbadmin DBPassword=MyPassword123
 
Deploment comand for Lambda_Function :
aws cloudformation deploy --template-file Lambda_Function.yaml --stack-name tcLambdaFunction --capabilities CAPABILITY_NAMED_IAM --region ap-south-1


Deploment comand for CloudWatch_Events :
aws cloudformation deploy --template-file CloudWatch_Events.yaml --stack-name tcCloudWatchEvents --capabilities CAPABILITY_NAMED_IAM --region ap-south-1

Deploment command for s3_code_bucket :
aws cloudformation deploy --template-file s3_code_bucket.yaml --stack-name tcs3codebucket --capabilities CAPABILITY_NAMED_IAM --region ap-south-1



compress Lambda code :
this command use on git and lanix ubuntu :
zip lambda_function.zip lambda_function.py
this command use on only window powershell:
Compress-Archive -Path * -DestinationPath lambda_code.zip


Upload Code to Created Bucket :
aws s3 cp lambda_code.zip s3://"your buckt name "/lambda_code.zip


CHEK the bucket name aws s3 ls on cli :
aws s3 ls 

Get the latest log streams for your Lambda : 
aws logs describe-log-streams --log-group-name "/aws/lambda/SalesProcessorFunction" --order-by LastEventTime --descending --limit 1 --region ap-south-1

full logs : 
aws logs get-log-events --log-group-name "/aws/lambda/SalesProcessorFunction" --log-stream-name 'logs name ' --limit 50 --region ap-south-1


Tum CLI se verify kar sakte ho:
aws sns list-topics --region ap-south-1


Topic me email subscription ho, aur wo confirm bhi ho :
aws sns list-subscriptions-by-topic --topic-arn "your sns topic arn" --region ap-south-1


only for testing :
aws sns publish --topic-arn arn:aws:sns:"your sns topic arn" --message "🎯 This is a test message from CLI!"
