import networkx as nx

def build_graph(scan_results):
    """
    Build a directed graph from scan results enriched with CVEs.

    Args:
        scan_results (dict): Output from CVE-enriched scanner

    Returns:
        networkx.DiGraph: Graph of hosts, services, CVEs
    """
    G = nx.DiGraph()

    for host, data in scan_results.items():
        G.add_node(host, type="host", label=host)

        for port, service in data.get("tcp", {}).items():
            svc_id = f"{host}:{port}"
            label = f"{service.get('name', '')} {port}"
            G.add_node(svc_id, type="service", label=label)
            G.add_edge(host, svc_id, relation="exposes")

            for cve in service.get("cves", []):
                G.add_node(cve, type="cve", label=cve)
                G.add_edge(svc_id, cve, relation="vulnerable_to")

    return G
