import json
import os
import networkx as nx
from networkx.readwrite import json_graph

def export_graph_json(G, filename="graph.json"):
    data = json_graph.node_link_data(G)
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"[+] Graph JSON saved to {filename}")

def export_graph_html(G, filename="graph.html"):
    data = json_graph.node_link_data(G)

    html_template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>VulnGraph Report</title>
        <script src="https://cdn.jsdelivr.net/npm/vis-network/standalone/umd/vis-network.min.js"></script>
        <style>#mynetwork {{ width: 100%; height: 800px; border: 1px solid lightgray; }}</style>
    </head>
    <body>
        <h2>Vulnerability Graph</h2>
        <div id="mynetwork"></div>
        <script>
            const data = {json.dumps(data)};

            const nodes = new vis.DataSet(data.nodes.map(n => ({
                id: n.id,
                label: n.label,
                group: n.type
            })));

            const edges = new vis.DataSet(data.links.map(l => ({
                from: l.source,
                to: l.target,
                label: l.relation || '',
                arrows: 'to'
            })));

            const container = document.getElementById('mynetwork');
            const network = new vis.Network(container, { nodes, edges }, {{}});
        </script>
    </body>
    </html>
    """

    with open(filename, "w") as f:
        f.write(html_template)
    print(f"[+] Graph HTML saved to {filename}")
