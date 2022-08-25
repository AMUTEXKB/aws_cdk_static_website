from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_s3 as _s3,
    aws_route53 as route53,
    aws_route53_targets as targets,
    aws_s3_deployment as s3deploy,
    RemovalPolicy,
    CfnOutput,
)
from constructs import Construct

class StaticWebsiteStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

  

        record_name = "www"
        domain_name = "oluwaseun.ml"

        bucket_website = _s3.Bucket(self, id="BucketWebsite",
            bucket_name=f"{record_name}.{domain_name}",  # www.example.com
            public_read_access=True,
            website_index_document="index.html"
        )
        s3deploy.BucketDeployment(self, id="DeployWebsite",
            sources=[s3deploy.Source.asset("./Sunglass/html")],
            destination_bucket=bucket_website
        )
        zone = route53.HostedZone.from_lookup(self, id="Zone", domain_name=domain_name) # example.com

        route53.ARecord(self, "AliasRecord",
            zone=zone,
            record_name=record_name,  # www
            target=route53.RecordTarget.from_alias(targets.BucketWebsiteTarget(bucket_website))
        )
        CfnOutput(self, id="ServiceAccountIamRole", value=bucket_website.bucket_website_domain_name)