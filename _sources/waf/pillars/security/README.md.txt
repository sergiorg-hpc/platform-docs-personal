# **AWS WAF Review** - Security Pillar

The **Security Pillar** provides guidance to help us apply best practices and current recommendations in the design, delivery and maintenance of secure AWS workloads. It also helps in meeting our business and regulatory requirements.

Similar to other pillars from the AWS Well-Architected Framework Review, the document is divided in different questions that aim at reflecting the potential flaws in the design considerations of our architecture.

## Table of Contents

1. [**SEC 1:** How do you securely operate your workload?](#sec-1-how-do-you-securely-operate-your-workload)
1. [**SEC 2:** How do you manage identities for people and machines?](#sec-2-how-do-you-manage-identities-for-people-and-machines)
1. [**SEC 3:** How do you manage permissions for people and machines?](#sec-3-how-do-you-manage-permissions-for-people-and-machines)
1. [**SEC 4:** How do you detect and investigate security events?](#sec-4-how-do-you-detect-and-investigate-security-events)
1. [**SEC 5:** How do you protect your network resources?](#sec-5-how-do-you-protect-your-network-resources)
1. [**SEC 6:** How do you protect your compute resources?](#sec-6-how-do-you-protect-your-compute-resources)
1. [**SEC 7:** How do you classify your data?](#sec-7-how-do-you-classify-your-data)
1. [**SEC 8:** How do you protect your data at rest?](#sec-8-how-do-you-protect-your-data-at-rest)
1. [**SEC 9:** How do you protect your data in transit?](#sec-9-how-do-you-protect-your-data-in-transit)
1. [**SEC 10:** How do you anticipate, respond to, and recover from incidents?](#sec-10-how-do-you-anticipate-respond-to-and-recover-from-incidents)
1. [**SEC 11:** How do you incorporate and validate the security properties of applications throughout the design, development, and deployment lifecycle?](#sec-11-how-do-you-incorporate-and-validate-the-security-properties-of-applications-throughout-the-design-development-and-deployment-lifecycle)


### **SEC 1:** How do you securely operate your workload?
Try and follow best practices:
- Least priv. access
- TLS all web communication
- AuthN/Z for services handled by keycloak
- Nearly all infra brought up by Terraform, plan to make it not directly accessible even to those directly working on it (in the future)
- 1 deployment for all users.


### **SEC 2:** How do you manage identities for people and machines?
- End users are defined in Keycloak. All(??) exposed services verify if users are authenticated in Keycloak.
- Identity is stored is GitHub
- Personnel have their own AWS IAM Identity Center account.
- AWS components like EC2 VMs have certain IAM roles with limited rights which are created/deployed with Terraform.


### **SEC 3:** How do you manage permissions for people and machines?
- For users, keycloak
- For employees, limited read only access to AWS console
- Terraform for bringing up infra; generally doesn't include access except for admins, still some exists for employees as things are brought online


### **SEC 4:** How do you detect and investigate security events?
- The WAF could likely detect security events, but we're not actively monitoring its logs and we have no alerting setup.
- We also have no active monitoring & alerting for other signs of security issues, such as high number of errors in containers, or big increase in network or S3 I/O traffic.


### **SEC 5:** How do you protect your network resources?
- Single VPC with network segmentation
  - But access rules between subnets are too open
- All web traffic traverses a loadbalancer, with WAF in front of the load balancer


### **SEC 6:** How do you protect your compute resources?
- Infra generally isn't accessible, even to employees (is the goal)
- Users authenticated by keycloak, if jobs are launched, plan is to account for usage, and bill that way
- Have alerts for excess costs


### **SEC 7:** How do you classify your data?
Our main storage is S3 and managed by a knowledge graph data management service (i.e., Nexus).

The plan is to have read-only public assets accessible by all users, as well as read-write private assets accessible exclusively by their respective owner (i.e., Project ID of a specific Virtual Lab ID).

We plan to use tags to classify the ownership and purpose of the data at S3 object storage-level.

We have active support for tag verification and automatic tagging of AWS resources based on component owner. This work could be extended for data stored on S3 from specific users.

`Potential issue:` We currently do not have a proper data lifecycle management (e.g., for how long are we going to retain data from organizations that no longer utilize the platform, etc.).


### **SEC 8:** How do you protect your data at rest?
Stored in S3, behind a service that handles authN/Z

Our main storage is S3 and managed by a knowledge graph data management service (i.e., Nexus).

We have hashes of the data stored in the knowledge graph for data integrity purposes.

Assets are read-only. Write is only supported prior to authentication and validation by data management service.

`Potential issue:` We currently do not encrypt our assets on S3, and even if we did, it would help to protect against external attacks and not internal attacks (i.e., one user reading confidential data from another user without data management service interference).


### **SEC 9:** How do you protect your data in transit?
TLS


### **SEC 10:** How do you anticipate, respond to, and recover from incidents?
Backup / restore consistency between RDS / S3 is not managed

No process. 


### **SEC 11:** How do you incorporate and validate the security properties of applications throughout the design, development, and deployment lifecycle?
Experts review the terraform changes.
