import aws_cdk as core
import aws_cdk.assertions as assertions

from static_website.static_website_stack import StaticWebsiteStack

# example tests. To run these tests, uncomment this file along with the example
# resource in static_website/static_website_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = StaticWebsiteStack(app, "static-website")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
