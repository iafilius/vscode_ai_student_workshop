# Egress Firewall Policies (DMZ-FW-01)

The following strict ingress/egress rules are enforced at the datacenter boundary. Default action is DENY.

## Rule ID: FW-ALLOW-BGP
- **Source IP:** 10.250.0.1 (Spine-01)
- **Source IP:** 10.250.0.2 (Spine-02)
- **Destination IP:** 10.255.1.2 (Primary BGP Peer)
- **Destination IP:** 10.255.1.6 (Backup BGP Peer)
- **Protocol:** TCP
- **Port:** 179
- **Action:** PERMIT

## Rule ID: FW-DENY-VM-BGP
- **Source IP:** 10.250.10.0/24 (Leaf-01 VMs)
- **Source IP:** 10.250.11.0/24 (Leaf-02 VMs)
- **Destination IP:** Any
- **Protocol:** TCP
- **Port:** 179
- **Action:** DENY
