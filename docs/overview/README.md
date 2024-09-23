# Introduction and Architecture Overview 

Brief introduction with an overview of the platform. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam...

> **TODO**
> Add proper introduction and Draw.io diagram below, instead of PNG

![Blue Brain Open Platform - Main Architecture](resources/1_main.drawio.svg)

## High-level Infrastructure Overview

Brief introduction with an overview of the infrastructure, such as load balancer, NAT, DNS, etc. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam...

> **TODO**
> Add proper details and Draw.io diagram below, instead of PNG

![Blue Brain Open Platform - Main Architecture](resources/2_infrastructure.drawio.svg)

### Virtual Labs and Projects

`Virtual Labs` and `Projects` are two concepts used for authentication, permissions and billing.
A `Virtual Lab` is an organizational aide under which `Projects` can be created.
There are two types of users within a `Virtual Lab`: `Admins` and `Team Members`.
Admins are able to manage the users within the `Virtual Lab`, manage billing, and are able to set budget on `Project`, in a dollar amount.
`Virtual Labs` can be created by any logged in user, and they must have a unique name within the set of all `Virtual Labs`.

Within `Virtual Labs`, `Projects` can be created to help with organization.
These `Projects` then have resources attached to them, including a private Nexus project.
These resources are accounted for and billed in a per `Project` fashion.
Team members must be granted access to `Projects`, and they are the only ones with access to the Nexus project.
It is possible to be part of a `Virtual Lab`, but not part of a `project`.

### Configuration and Deployment
The AWS infrastructure required for the Blue Brain Open Platform is exclusively managed through infrastructure-as-code. We use Terraform to configure and deploy the different components of the platform, including setting up IAM policies, security groups, or tagging.

Each service is defined on its own Terraform module and operates independently from the rest of the services.

> **TODO**
> Elaborate some of the deployment details and general information. 

### Cost Monitoring Support
Our infrastructure relies heavily on the use of **AWS Tags** in order to understand the overall operational costs for each of the services running in the platform. Our goal is to ensure that we can not only provide realistic costs estimates, but also identify the specific resources that each Virtual Lab and Project utilizes.

![Blue Brain Open Platform - Main Architecture](resources/3_costmonitoring_tags.drawio.svg)

Further, we have introduced mechanisms for monitoring the tags of each resource after Terraform runs and deploys the infrastructure changes. In particular, a dedicated CI job runs and utilizes **AWS Resource Explorer** to query for untagged resources. We then utilize different information from the resource to determine the component, and in certain cases the resource is tagged automatically (e.g., Terraform does not tag private ENIs).

Daily updates are provided for the teams to monitor their untagged resources and fix any potential issues introduced in the infrastructure-as-code modules.

