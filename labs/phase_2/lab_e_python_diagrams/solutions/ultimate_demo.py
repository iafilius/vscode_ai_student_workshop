from diagrams import Diagram, Cluster
from diagrams.generic.network import Switch, Router
from diagrams.onprem.compute import Server
from diagrams.aws.network import InternetGateway

with Diagram("Ultimate Datacenter Topology", show=False, filename="ultimate_demo"):
    
    wan = InternetGateway("DCI WAN")

    with Cluster("Datacenter 1 (DC1)"):
        core_router_1 = Router("DC1 Core Router")
        
        with Cluster("Spine Layer"):
            spines_1 = [Switch("DC1-Spine-1"), Switch("DC1-Spine-2")]
            
        with Cluster("Compute Leaf Layer"):
            leaves_1 = [Switch(f"DC1-Leaf-{i+1}") for i in range(4)]
            
        with Cluster("Compute Payload"):
            for leaf in leaves_1:
                hosts = [Server(f"{leaf.label}-ESXi-A"), Server(f"{leaf.label}-ESXi-B")]
                leaf >> hosts

        core_router_1 >> spines_1
        for leaf in leaves_1:
            spines_1 >> leaf

    with Cluster("Datacenter 2 (DC2)"):
        core_router_2 = Router("DC2 Core Router")
        
        with Cluster("Spine Layer"):
            spines_2 = [Switch("DC2-Spine-1"), Switch("DC2-Spine-2")]
            
        with Cluster("Compute Leaf Layer"):
            leaves_2 = [Switch(f"DC2-Leaf-{i+1}") for i in range(4)]
            
        with Cluster("Compute Payload"):
            for leaf in leaves_2:
                hosts = [Server(f"{leaf.label}-ESXi-A"), Server(f"{leaf.label}-ESXi-B")]
                leaf >> hosts

        core_router_2 >> spines_2
        for leaf in leaves_2:
            spines_2 >> leaf

    wan >> core_router_1
    wan >> core_router_2
