#!/usr/bin/env python3
import os

import aws_cdk as cdk

from aws_codepipeline.aws_codepipeline_stack import AwsCodepipelineStack


app = cdk.App()
AwsCodepipelineStack(app, "AwsCodepipelineStack",
    # If you don't specify 'env', this stack will be environment-agnostic.
    # Account/Region-dependent features and context lookups will not work,
    # but a single synthesized template can be deployed anywhere.

    # Uncomment the next line to specialize this stack for the AWS Account
    # and Region that are implied by the current CLI configuration.

    #env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),

    # Uncomment the next line if you know exactly what Account and Region you
    # want to deploy the stack to. */
    # Testin

    env=cdk.Environment(account='209891200762', region='us-east-1'),
    stack_name='github-codepipeline-stack'

    # For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html
    )
cdk.Tags.of(app).add(key='feature',value='resource_stack')
cdk.Tags.of(app).add(key='contact',value='skrishna203@gmail.com')
cdk.Tags.of(app).add(key='team',value='shashi_team')
app.synth()
