# Datacenter 1 Subnet Allocation Matrix

This Knowledge Item documents the verified subnet distribution plan for our Spine-Leaf datacenter fabric.

## Subnet Ranges
- **Spine Switch Transit Fabric:** `10.250.0.0/24`
- **Leaf Access Nodes (1..28):** `10.250.10.0/24` to `10.250.38.0/24`
- **Interconnect DCI Transit Link:** `10.255.1.0/30`
- **VMware / NSX-T Underlay Transport:** `10.250.254.0/23`

## Compliance Verification
- Fully compliant with corporate RFC 1918 allocations.
- BGP EVPN autonomous systems range: `AS 65100` to `AS 65128`.
