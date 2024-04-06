def lambda_handler(event, context):
    # Retrieve numbers from the event
    num1 = event["num1"]
    num2 = event["num2"]

    # Calculate the sum
    total = num1 + num2

    # Return the result
    return {"statusCode": 200, "body": {"result": total}}
