# Datacenter 1: Underlay & Logical Spine-Leaf Fabric Details

This Knowledge Item documents the production-grade physical and logical subnet layout for Datacenter 1.

---

## 🏗️ Spine-Leaf Subnet Allocations

### 1. Spine Link Subnets
- **Spine-01 / Spine-02 links:** `10.250.0.0/24`
- **Link allocation:**
  - `10.250.0.1` -> Spine-01 GigabitEthernet0/1
  - `10.250.0.2` -> Spine-02 GigabitEthernet0/1

### 2. Leaf Node Subnets
- **Leaf-01 User Subnet:** `10.250.10.0/24` (VLAN 10)
- **Leaf-02 VoIP Subnet:** `10.250.20.0/24` (VLAN 20)
- **Leaf-03 DB Subnet:** `10.250.30.0/24` (VLAN 30)

### 3. Interconnect Data Center Links (DCI)
- **DCI Link Pairs:** `10.255.1.0/30`
- **DCI Link-01 IP:** `10.255.1.1`
- **DCI Link-02 IP:** `10.255.1.2`
