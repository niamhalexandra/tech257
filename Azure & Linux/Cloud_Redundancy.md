## Azure Redundancy Types:

1. Locally Redundant Storage (LRS):
* Data is replicated three times within a data center in a single region.
Offers low-cost redundancy but does not protect against data center failure.

2. Zone-Redundant Storage (ZRS):
* Data is replicated across multiple availability zones within a single region.
Provides higher durability and availability compared to LRS by distributing data across zones.

3. Geo-Redundant Storage (GRS):
* Data is replicated synchronously three times within the primary region and asynchronously to a secondary region hundreds of miles away.
Offers high durability and availability with data redundancy across regions.

4. Read-Access Geo-Redundant Storage (RA-GRS):
* Similar to GRS but allows read access to data in the secondary region.
Provides additional resilience and allows for read operations from the secondary region in case of a regional outage.

5. Geo-Zone-Redundant Storage (GZRS):
* Combines the features of ZRS and GRS by replicating data across availability zones within the primary region and asynchronously to a secondary region.
Offers both high availability within the primary region and geographic redundancy across regions.

6. Read-Access Geo-Zone-Redundant Storage (RA-GZRS):
* Similar to GZRS but allows read access to data in the secondary region.
Provides the highest level of redundancy and availability, allowing read access to data from both the primary and secondary regions.

### Cost Differences:

The cost varies depending on the redundancy type chosen and the region where the storage account is located. You can use the Azure Pricing Calculator to estimate the costs for each redundancy type.

#### Example Comparison between UK South and UK West:

The differences in cost between regions could be due to various factors such as data center infrastructure costs, availability of resources, demand-supply dynamics, and local regulations. It's recommended to use the Azure Pricing Calculator to compare costs for different redundancy options in each region.

#### Selecting a Redundancy Type on Azure Portal:

On the Azure portal, when creating or configuring a storage account, you can choose the redundancy type under the "Data Resiliency" section. Here, you'll find options to select between LRS, ZRS, GRS, RA-GRS, GZRS, and RA-GZRS. A screenshot illustrating this process can be provided upon request.