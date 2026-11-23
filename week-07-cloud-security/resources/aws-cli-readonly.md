# AWS CLI: read-only commands for my own account

Use a profile with **SecurityAudit + ViewOnlyAccess**: `--profile audit`. Redact account IDs, ARNs and bucket names before sharing output. These commands only **read** configuration.

## Identity
```
aws sts get-caller-identity
aws iam get-account-summary
aws iam get-account-password-policy
```

## IAM
```
aws iam list-users
aws iam list-groups
aws iam list-roles
aws iam list-policies --scope Local
aws iam list-attached-user-policies --user-name <user>
aws iam list-access-keys --user-name <user>
aws iam list-mfa-devices --user-name <user>
aws iam generate-credential-report
aws iam get-credential-report --query Content --output text | base64 -d
```
Export a customer-managed policy for the offline checker:
```
aws iam get-policy --policy-arn <arn> --query Policy.DefaultVersionId --output text
aws iam get-policy-version --policy-arn <arn> --version-id <v1> --query PolicyVersion.Document > policy.json
python3 scripts/iam_policy_checker.py policy.json
```

## S3
```
aws s3api list-buckets --query "Buckets[].Name"
aws s3api get-public-access-block --bucket <bucket>
aws s3api get-bucket-policy --bucket <bucket>
aws s3api get-bucket-policy-status --bucket <bucket>
aws s3api get-bucket-acl --bucket <bucket>
aws s3api get-bucket-encryption --bucket <bucket>
aws s3api get-bucket-versioning --bucket <bucket>
aws s3api get-bucket-logging --bucket <bucket>
aws s3control get-public-access-block --account-id <account-id>
```

## EC2 and network
```
aws ec2 describe-regions --query "Regions[].RegionName" --output text
aws ec2 describe-instances --query "Reservations[].Instances[].[InstanceId,State.Name,PublicIpAddress]" --output table
aws ec2 describe-security-groups > sg.json
python3 scripts/sg_checker.py sg.json
aws ec2 describe-vpcs
aws ec2 describe-subnets
aws ec2 describe-network-acls
aws ec2 describe-flow-logs
aws ec2 describe-snapshots --owner-ids self --query "Snapshots[].SnapshotId"
```
Repeat per region with `--region <region>`.

## Logging and detection
```
aws cloudtrail describe-trails
aws cloudtrail get-trail-status --name <trail>
aws guardduty list-detectors
aws configservice describe-configuration-recorders
```

## Do NOT (without authorization)
- Run any of these against an account that isn't mine.
- Use `put`, `delete`, `create` or `attach` commands during an audit.
