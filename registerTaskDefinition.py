import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    client = boto3.client('ecs', region_name='us-east-1')
    response = client.register_task_definition(
        family='string',
        networkMode='awsvpc',
        containerDefinitions=[
            {
                'name': 'string',
                'image': 'image:tag',
                'cpu': 10,
                'memory': 512,
                'essential': True,
                'command' : [
                    '--ecs-mode'
                    ],
                'environment': [
                    {
                        "name": "KEY",
                        "value": "VALUE"
                    },
                ],
                'mountPoints': [
                    {
                        'sourceVolume': 'volume',
                        'containerPath': '/path',
                        'readOnly': False
                    },
                    {
                        'sourceVolume': 'volume',
                        'containerPath': '/path',
                        'readOnly': False
                    },
                    {
                        'sourceVolume': 'volume',
                        'containerPath': '/path',
                        'readOnly': False
                    },
                ],
                }
        ],
        volumes=[
            {
                'name': 'volume',
                'host': {
                    'sourcePath': '/path'
                    }
            },
            {
                'name': 'volume',
                'host': {
                    'sourcePath': '/path'
                    }
            },
            {
                'name': 'volume',
                'host': {
                    'sourcePath': '/path'
                    }
            },
        ],
    )
