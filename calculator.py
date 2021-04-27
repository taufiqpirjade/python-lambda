import json
def lambda_handler(event, context):
	message = 'Hello {} {}!'.format(event['first_name'], event['last_name'])
	return	{
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "message ": message
        })
	}