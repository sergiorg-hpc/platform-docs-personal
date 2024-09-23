# Accounting Service

Tracks costs for services; when a service is launched it either sends a message via SQS saying it’s starting, and then when it ends or it uses an API call to do the same.
Future work: deploy multiple copies of this for HA.

![Accounting Service - Main Architecture](resources/1_main.drawio.svg)

> **TODO**
> Add proper overview of the service, provide technical details, consolidate Draw.io figures, ..., etc. [See example template for further information](../template/).

## Content below copied from GitLab
![Swagger API](https://openbluebrain.com/api/accounting/docs)
![Dashboard](https://us-east-1.console.aws.amazon.com/cloudwatch/home?region=us-east-1#dashboards/dashboard/Accounting)

### Goals:

* Be able to breakdown costs at the `Project` level, as well as the `Virtual Lab` level.
* Be able to say 'how much credit is left, so that costs are capped to what the user has already paid for
  * Prior to a use of a cost incurring resource usage, the budget will be checked if there is enough money
