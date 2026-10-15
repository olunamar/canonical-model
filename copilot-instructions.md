# Enterprise IT canonical-model instructions

This repository is the authoritative source for the company's canonical
IT model and graph lineage.

## Mandatory evidence rules

1. Use only information present in this repository or returned by approved
   read-only MCP tools.
2. Never invent an entity, identifier, class, relationship, direction,
   cardinality or dependency.
3. Distinguish clearly between:
   - canonical model definitions,
   - graph instance data,
   - inferred impact,
   - verified impact,
   - missing information.
4. If a relationship is not allowed by the canonical model, state that it
   is invalid.
5. If there is insufficient evidence, respond with `NOT DETERMINED`.
6. Include repository paths or graph evidence supporting conclusions.
7. Preserve relationship direction exactly as defined.
8. Do not treat physical containment, logical dependency, ownership and
   service consumption as equivalent relationships.

## Canonical concepts

The principal canonical domains are:

- Customer
- Service
- Workload
- Environment
- Infrastructure
- Catalog

Subclasses and specialized types must be read from the canonical model.
Do not create subclasses that do not exist in the model.

## Impact-analysis method

For every impact-analysis request:

1. Resolve the starting entity by ID, name or approved alias.
2. Report ambiguous matches before continuing.
3. Identify the node's canonical type.
4. Traverse only relationships with impact propagation enabled.
5. Respect relationship direction.
6. Detect and suppress cycles.
7. Deduplicate entities reached by multiple paths.
8. Separate direct and indirect impact.
9. Identify unaffected entities only when graph evidence proves that they
   use an independent path.
10. Return all evidence paths.

## Required answer structure

- Interpretation
- Starting entity
- Direct impact
- Indirect technical impact
- Workload impact
- Service impact
- Customer impact
- Unaffected components
- Evidence paths
- Data-quality warnings
- Confidence

## Confidence levels

- VERIFIED: supported by an explicit graph path.
- PARTIAL: some path segments are explicit and others are unresolved.
- NOT DETERMINED: evidence is insufficient.
