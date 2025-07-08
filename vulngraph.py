import argparse
import json
from modules.graph_builder import build_graph
from modules.graph_export import export_graph_json, export_graph_html

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="VulnGraph - visualize hosts, services, and CVEs in a graph.")
    parser.add_argument("--input", required=True, help="Path to enriched scan results (JSON)")
    parser.add_argument("--html", action="store_true", help="Export graph to HTML")
    parser.add_argument("--json", action="store_true", help="Export graph to JSON")
    args = parser.parse_args()

    with open(args.input, "r") as f:
        data = json.load(f)

    G = build_graph(data)

    if args.json:
        export_graph_json(G, filename="graph.json")

    if args.html:
        export_graph_html(G, filename="graph.html")
