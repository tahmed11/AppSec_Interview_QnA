### Why Cloud Computing:
On demand access to shared pool of resources such as applications, servers, storage and network security. Benefits include economies of scale, cost-saving and uniform security standards.

#### Well Architected Framework:
5 Pillars:
1. Operational Excellence 
2. Security 
3. Reliability
4. Performance Efficiency 
5. Cost-Optimization


#### Shared responsibility model:
AWS: Security 'of' the cloud
Customer: Security 'in' the cloud. 

AWS Security framework/ Security in the Cloud composed of 5 areas:
1. Identity and Access Management
2. Detective Controls
3. Infrastructure protection
4. Data Protection
5. Incident Response

#### Identity and Access Management 

Protection of AWS Credentials:
1. Use federation if possible
2. If federation not possible for service to service interaction then protect using the AWS Security token service to generate and manage temporary access tokens.
3. Fine grained authorisation: create roles using principle of least privilege

#### Detective Controls: 
1. Capture and Analyze Logs: Use AWS CloudTrail to continously log and monitor and retain account activity related to actions across AWS infrastructure.
2. Integration Auditing controls with notification and workflow. 
3. Use AWS Inspector
4. AWS Security Hub 

#### Infrastructure Protection
1. Protecting Network and Host level boundaries
  AWS VPC Security Groups provides a per host stateful firewall
  AWS Direct connect
  AWS NACL 

2. System security configuration and Maintenance
  AWS System manager, patch manager, inventory,etc. 
  
3. Enforcing Service level protection:
  Use AWS IAM policy to restrict who can have access to what AWS services
  
#### Data Protection
  1. Data Classification -> use tags
  2. Encryption/Tokenization -> AWS KMS, CloudHSM
  3. Protecting data at rest 
  3. Protecting data in transit 
  4. Data backup, replication, recovery
  
#### Incident Response
Incident response plan. 
	The foundation of a successful incident response program in the cloud is to Educate, Prepare, Simulate, and Iterate.
1. Educate your security operations and incident response staff about cloud technologies and how your organization intends to use them.
2. Prepare your incident response team to detect and respond to incidents in the cloud, enabling detective capabilities, and ensuring appropriate access to the necessary tools and cloud services. Additionally, prepare the necessary runbooks, both manual and automated, to ensure reliable and consistent responses. Work with other teams to establish expected baseline operations, and use that knowledge to identify deviations from those normal operations.
3. Simulate both expected and unexpected security events within your cloud environment to understand the effectiveness of your preparation.
4. Iterate on the outcome of your simulation to improve the scale of your response posture, reduce time to value, and further reduce risk
	

AWS IAM (continued):
Identity and access management in cloud manages who has access and who can access what resources on AWS. 
Access Control: AWS administrators use policies to control access to AWS resources. 
Resources: AWS Services such as RDS, S3. 

IAM resources include: Users, Groups, Roles 
Policies - JSON policy documents that define the permissions for the object to which they are attached. Two types of policies: 

Identity based policies: Identity-based policies are attached to an IAM user, group, or role. These policies let you specify what that identity can do (its permissions). For example, you can attach the policy to the IAM user named John, stating that he is allowed to perform the Amazon EC2 RunInstances action. The policy could further state that John is allowed to get items from an Amazon DynamoDB table named MyCompany. You can also allow John to manage his own IAM security credentials. Identity-based policies can be managed or inline.

Resource based policies: Defines particular resources (for example: particular S3) can be controlled by a principal. Resource-based policies are inline only, not managed.

Identity-based policies and resource-based policies are both permissions policies and are evaluated together. For a request to which only permissions policies apply, AWS first checks all policies for a Deny. If one exists, then the request is denied. Then AWS checks for each Allow. If at least one policy statement allows the action in the request, the request is allowed. It doesn't matter whether the Allow is in the identity-based policy or the resource-based policy.


Different sets of policy: AWS Managed policies, Customer Managed policies, Inline policies. 
https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html

AWS Managed policies: An AWS managed policy is a standalone policy that is created and administered by AWS. 

Customer managed policies: You can create standalone policies that you administer in your own AWS account, which we refer to as customer managed policies. 

Inline Policies: An inline policy is a policy that's embedded in a principal entity (a user, group, or role)—that is, the policy is an inherent part of the principal entity. You can create a policy and embed it in a principal entity, either when you create the principal entity or later.


we recommend that you use managed policies instead of inline policies.

The AWS Security Token Service (STS) is a web service that enables you to request temporary, limited-privilege credentials for AWS Identity and Access Management (IAM) users or for users that you authenticate (federated users).

AssumeRole:
Returns a set of temporary security credentials that you can use to access AWS resources that you might not normally have access to. These temporary credentials consist of an access key ID, a secret access key, and a security token. Typically, you use AssumeRole within your account or for cross-account access.

Identity and Access Management:
SEC 1: How do you manage credentials and authentication?
	IAM policy and roles, principle of least privilege.
	MFA
	AWS organization
SEC 2: How do you control human access?
	Active directory federation service tied with 
SEC 3: How do you control programmatic access?
	AWS Secret manager
  
AWS provides the service AWS Secrets Manager for easier management of secrets. Secrets can be database credentials, passwords, third-party API keys, and even arbitrary text. You can store and control access to these secrets centrally by using the Secrets Manager console, the Secrets Manager command line interface (CLI), or the Secrets Manager API and SDKs.

	1. The database administrator creates a set of credentials on the Personnel database for use by an application called MyCustomApp. The administrator also configures those credentials with the permissions required for the application to access the Personnel database.
	2. The database administrator stores the credentials as a secret in Secrets Manager named MyCustomAppCreds. Then, Secrets Manager encrypts and stores the credentials within the secret as the protected secret text.
	3. Then MyCustomApp accesses the database, the application queries Secrets Manager for the secret named MyCustomAppCreds.
	4. Secrets Manager retrieves the secret, decrypts the protected secret text, and returns the secret to the client app over a secured (HTTPS with TLS) channel.
	5. The client application parses the credentials, connection string, and any other required information from the response and then uses the information to access the database server.


Detective control:
SEC 4: How do you detect and investigate security events?
	CloudTrail 
SEC 5: How do you defend against emerging security threats?
	 Amazon GuardDuty is a managed threat detection service that continuously monitors for malicious or unauthorized behavior to help you protect your AWS accounts and workloads.
	
Infrastructure Protection
SEC 6: How do you protect your networks?
VPC, NACL, Security group
AWS shield, WAF


SEC 7: How do you protect your compute resources?
	Amazon Inspector
	
Data Protection
SEC 8: How do you classify your data?
	Custom tag
SEC 9: How do you protect your data at rest?
	Encryption while at rest
	AWS KMS
SEC 10: How do you protect your data in transit?
	Encryption ssl, etc
	

AWS Cognito:
	Cognito Identity enables you to authenticate users through an external identity provider and provides temporary security credentials to access your app’s backend resources in AWS or any service behind Amazon API Gateway. Amazon Cognito works with external identity providers that support SAML or OpenID Connect, social identity providers (such as Facebook, Twitter, Amazon) and you can also integrate your own identity provider.
	Q: How does the login flow work with public identity providers?
	Your mobile app authenticates with an Identity Provider (IdP) using the provider’s SDK. Once the end user is authenticated with the IdP, the OAuth or OpenID Connect token or the SAML assertion returned from the IdP is passed by your app to Cognito Identity, which returns a new Cognito ID for the user and a set of temporary, limited-privilege AWS credentials.
	
	Q: How does Cognito Identity help me control permissions and access AWS services securely?
	Cognito Identity assigns your users a set of temporary, limited privilege credentials to access your AWS resources so you do not have to use your AWS account credentials. The permissions for each user are controlled through AWS IAM roles that you create. You can define rules to choose the IAM role for each user, or if you are using groups in a Cognito user pool, you can assign IAM roles based on groups. Cognito Identity also allows you to define a separate IAM role with limited permissions for guest users who are not authenticated. In addition, you can use the unique identifier that Cognito generates for your users to control access to specific resources. For example you can create a policy for an S3 bucket that only allows each user access to their own folder within the bucket.
