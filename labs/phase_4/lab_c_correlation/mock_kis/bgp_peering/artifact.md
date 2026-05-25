# External BGP Peering Topology

All external traffic routes through the primary transit peer located in the DMZ.

## Primary Peer
- **ASN:** 65001
- **IP Address:** 10.255.1.2
- **State:** ACTIVE
- **Location:** DCI-Gateway-A

## Backup Peer
- **ASN:** 65002
- **IP Address:** 10.255.1.6
- **State:** STANDBY
- **Location:** DCI-Gateway-B
