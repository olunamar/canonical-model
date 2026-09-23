import os
import re
import json
import yaml



# Target folder where the canonical model lives
CANONICAL_MODEL_DIR = os.path.join("okf-catalog-IT", "canonical_model_okf")

def parse_okf_repository(base_path):
    graph = {
        "nodes": [],
        "edges": []
    }
    
    if not os.path.exists(base_path):
        print(f"Error: Directory '{base_path}' does not exist.")
        return graph

    for root, dirs, files in os.walk(base_path):
        if ".git" in root or ".gitlab" in root or "graph" in dirs:
            continue
            
        for file in files:
            if file.endswith(".md") and file != "README.md" and file != "index.md":
                file_path = os.path.join(root, file)
                
                # Relative entity path inside the canonical model
                rel_path = "/" + os.path.relpath(file_path, base_path).replace("\\", "/")
                
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                        
                    # Extract YAML frontmatter
                    fm_match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
                    if fm_match:
                        metadata = yaml.safe_load(fm_match.group(1)) or {}
                        entity_id = rel_path
                        
                        # Add Node entry
                        graph["nodes"].append({
                            "id": entity_id,
                            "name": metadata.get("entity_name", os.path.basename(file).replace(".md", "")),
                            "domain": metadata.get("domain", ""),
                            "type": metadata.get("type", "CanonicalEntity"),
                            "path": rel_path
                        })
                        
                        # Add Edges from relations block
                        relations = metadata.get("relations", [])
                        if isinstance(relations, list):
                            for rel in relations:
                                if isinstance(rel, dict) and "target" in rel and "type" in rel:
                                    graph["edges"].append({
                                        "source": entity_id,
                                        "target": rel["target"],
                                        "relationship": rel["type"]
                                    })
                except Exception as e:
                    print(f"Error parsing {file_path}: {e}")

    return graph

if __name__ == "__main__":
    graph_data = parse_okf_repository(CANONICAL_MODEL_DIR)
    
    # Save output graph directly inside the canonical model graph/ directory
    output_dir = os.path.join(CANONICAL_MODEL_DIR, "graph")
    os.makedirs(output_dir, exist_ok=True)
    out_path = os.path.join(output_dir, "lineage-graph.json")
    
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(graph_data, f, indent=2)
        
    print(f"Graph index generated successfully at {out_path} ({len(graph_data['nodes'])} nodes, {len(graph_data['edges'])} edges).")