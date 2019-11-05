import boto3

client = boto3.client('cloudformation', 'ap-northeast-1')

response = client.list_stacks(
    StackStatusFilter=['DELETE_FAILED']
)

for stack in response['StackSummaries']:
    client.delete_stack(
        StackName=stack['StackName']
    )