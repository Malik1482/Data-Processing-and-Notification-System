import json
import boto3
import pymysql
import os

def lambda_handler(event, context):
    print("Lambda function started.")

    secrets_client = boto3.client('secretsmanager')
    sns_client = boto3.client('sns')

    try:
        # Load environment variables
        print("Loading environment variables...")
        secret_arn = os.environ['SECRET_ARN']
        db_name = os.environ['DB_NAME']
        rds_host = os.environ['RDS_HOST']
        sns_topic_arn = os.environ['SNS_TOPIC_ARN']
        print(f"Environment variables loaded. RDS_HOST={rds_host}")

        # Fetch secrets from Secrets Manager
        print("Fetching secret from Secrets Manager...")
        secret = secrets_client.get_secret_value(SecretId=secret_arn)
        credentials = json.loads(secret['SecretString'])
        print("Secret fetched successfully.")

        # Connect to RDS MySQL
        print("Connecting to RDS MySQL...")
        conn = pymysql.connect(
            host=rds_host,
            user=credentials['username'],
            password=credentials['password'],
            database=db_name,
            connect_timeout=5
        )
        print("Connected to RDS successfully.")

        try:
            with conn.cursor() as cursor:
                print("Creating 'orders' table if it doesn't exist...")
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS orders (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        item_name VARCHAR(255),
                        quantity INT,
                        price DECIMAL(10,2),
                        order_date DATETIME DEFAULT CURRENT_TIMESTAMP
                    );
                """)
                print("Fetching order count...")
                cursor.execute("SELECT COUNT(*) FROM orders")
                order_count = cursor.fetchone()[0]

            message = f"Total orders in database: {order_count}"
            print(f"Publishing to SNS: {message}")
            sns_client.publish(TopicArn=sns_topic_arn, Message=message)

            print("Lambda completed successfully.")
            return {
                'statusCode': 200,
                'body': json.dumps({'message': message})
            }

        finally:
            print("Closing RDS connection...")
            conn.close()

    except Exception as e:
        error_message = f"Error occurred: {str(e)}"
        print(error_message)
        return {
            'statusCode': 500,
            'body': json.dumps({'error': error_message})
        }
