# **Blue Brain Open Platform** - Architecture Documentation

The main goal of this repository is to provide a technical overview of the **Blue Brain Open Platform** and its overall architecture running on [Amazon Web Services (AWS)](https://aws.amazon.com/). In particular, each section contains some of the most relevant technical decisions and design considerations, as well as provides other relevant details such as which AWS services are required, among others.

> [!IMPORTANT]
> **Don't forget:** Use [VSCode on GitHub](https://github.dev/BlueBrain/platform-docs) to edit the different sections, as well as to create/modify the diagrams via the recommended [Draw.io plugin](https://www.drawio.com/blog/edit-diagrams-with-github-dev) for VSCode.

## Table of Contents

1. [Introduction and Architecture Overview](overview/)
1. [Accounting Service](modules/accounting/)
1. [Authentication and Authorization](modules/authnz/)
1. [Interactive Application Service](modules/interactive/)
1. Machine Learning Services:
   - [Agent Service](modules/machinelearning/agent/)
   - [Inference Service](modules/machinelearning/inference/)
   - [Literature Service](modules/machinelearning/literature/)
1. [Mesh Generation Service](modules/meshgeneration/)
1. [Metadata and Data Service](modules/knowledgegraph/)
1. [Model Data Service](modules/pointcloud/)
1. [ParallelCluster Provisioner](modules/provisioner/)
1. [Thumbnail Service](modules/thumbnail/)
1. [Virtual Lab Service](modules/vlab/)
1. [Visualization Service](modules/visualization/)
1. [Workflow Service](modules/workflow/)
