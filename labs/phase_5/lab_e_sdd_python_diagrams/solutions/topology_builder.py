#!/usr/bin/env python3
from diagrams import Diagram, Cluster
from diagrams.onprem.network import Switch
from diagrams.generic.network import Router

def build_fabric_diagram():
    # Renders fabric_topology.png programmatically
    print("--> Commencing Diagram Compilation...")
    
    with Diagram("Multi-DC Spine-Leaf Fabric", show=False, filename="fabric_topology"):
        with Cluster("Datacenter 1"):
            spines = [Switch("Spine-01"), Switch("Spine-02")]
            leaves = [Switch("Leaf-01"), Switch("Leaf-02")]
            
            # Full mesh physical connections
            for s in spines:
                for l in leaves:
                    s - l

        # Edge DCI transit router
        dci = Router("DCI Transit Router")
        spines[0] - dci
        
    print("✓ Diagram compiled successfully. Output written to: fabric_topology.png")

if __name__ == "__main__":
    build_fabric_diagram()
