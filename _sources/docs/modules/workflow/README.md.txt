# Workflow Service
> [!NOTE]
> **Also known as:** `bbp-workflow`

One of the future use-cases expected in the Blue Brain Open Platform, would be to run large-scale simulations that may require dozens or even hundreds of computational resources and high-performance storage infrastructure (e.g., Lustre FSx). The orchestration for such simulations is mostly led by the **Workflow Service**, whose purpose is to spawn tailor-made resources through the [ParallelCluster Provisioner](../Provisioner/) and to control / monitor the execution of the different tasks associated with the workloads, among others.

When a new simulation is requested from the interface of the platform, a request is made to the REST API of the Workflow Service to authorize the request and also to orchestrate the deployment of [`bbp-workflow`](https://github.com/BlueBrain/bbp-workflow) inside an ECS Container Instance. The Provisioner is in charge of deploying the necessary infrastructure (if required) and provides the Workflow Service with the necessary information to locate and authenticate on the cluster. After this, the service will schedule and monitor the execution of the different tasks running in the cluster, as well as coordinate the data registration in the knowledge graph via the [Metadata and Data Service](../Nexus/).

![Workflow Service - Main Architecture](resources/1_main.drawio.svg)

Here are some of the key technologies utilized for the infrastructure:

- The Workflow Service mainly runs on an **ECS Container Instance** orchestrated via an **ECS Cluster**, with one instance launched per Virtual Lab Project[^Deployment].
  - The service is based on the use of a container image from  [`bbp-workflow`](https://github.com/BlueBrain/bbp-workflow).
  - The source code of bbp-workflow is written in Python 3 and relies on the use of [Luigi Framework](https://github.com/spotify/luigi) to build the job pipelines and monitor the execution.
- All the communication with the Workflow Service is handled exclusively via a REST API provided by **AWS API Gateway**.
  - Only the authorized users are allowed to interact with the service.
- A dedicated **AWS Lambda** handles the authentication and authorization of the requests via the [Authentication and Authorization Service](../Keycloak/).
  - An authorization token is provided for the Container Instances Handler.
- The Container Instances Handler is another **AWS Lambda** that validates the authorization token and provides support in the orchestration of the Workflow instances.
- The [ParallelCluster Provisioner](../Provisioner/) provides the necessary details to request the SSH private key to the **AWS Secrets Manager**, as well as to locate the ParallelCluster deployed for the specific Virtual Lab Project.
- Interactions with the [Metadata and Data Service](../Nexus/) are required to register new data into the knowledge graph.
  - In the case of large-scale simulations with Lustre FSx, the synchronization of the data is managed by a dedicated job with elevated permissions that relies on the existing S3-DRA setup. The Workflow service handles the request to store the data, monitor the job that is communicating with the Lustre HSM Service, and finally handles the confirmation of the synchronization.
  - In the case of large-scale simulations without Lustre FSx (e.g., eModel Fitting), the synchronization of the data is managed via direct upload to the knowledge graph using the support provided by Nexus. 

[^Deployment]: Each ParallelCluster deployment is constrained to a Project inside a Virtual Lab. Thus, the approach is to deploy a container instance per Project. We might limit the number of instances in the future.
