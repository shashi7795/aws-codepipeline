from aws_cdk import (
    Stack,
    aws_sqs as sqs,
    Duration,
    aws_lambda as function_lambda,
    aws_s3 as s3
)
from constructs import Construct
from aws_cdk import aws_iam as iam


class ResourceStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Define the Lambda execution role
        lambda_execution_role = iam.Role(
            self,
            "LambdaExecutionRole",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
            role_name="LambdaExecutionRole"
        )

        # Attach necessary policies to the Lambda execution role
        lambda_execution_role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaBasicExecutionRole")
        )


        function = function_lambda.Function(self,
                                            "shashi-demo",
                                            function_name="codepipeline_lambda",
                                            runtime=function_lambda.Runtime.PYTHON_3_9,
                                            code=function_lambda.Code.from_asset('./lambda_code_demo'),
                                            handler="demo_lambda.lambda_handler",
                                            role=lambda_execution_role)