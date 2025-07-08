# VulnGraph

Visualize host/service/CVE relationships using interactive graphs.

## Features

- Import JSON from CVE scanners (like `cve-scanner`)
- Build graphs with hosts, ports, and CVEs
- Export to:
  - `graph.json`: raw data
  - `graph.html`: interactive web view with vis.js

## Installation

```bash
git clone https://github.com/sandrosana/vulngraph.git
cd vulngraph
pip install -r requirements.txt
```

## Usage

```bash
python vulngraph.py --input scan_results.json --html --json
```

## Output

- `graph.html`: interactive report
- `graph.json`: full graph structure

## Dependencies

- Python 3
- `networkx`
