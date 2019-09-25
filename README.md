# Ontology API for KBase using Relation Engine

This is an API for ontology data that queries the relation engine.

## API 

### Params

The generic params has following schema:

```yaml
type: object
required: [id]
properties:
  id:
    type: string
  ts:
    type: integer
  ns:
    type: string
  limit:
    type: integer
    maximum: 1000
  offset:
    type: integer
  maximum: 100000
```

### Result

The result is always wrapped in an array of one element, following KBase convention. The generic result has following schema, representing query results from RE:

```yaml
type: array
minItems: 1
maxItems: 1
items:
  type: object
  properties:
    ts:
      type: integer
      title: Timestamp used in the request, default is current time
    stats:
      type: object
      description: RE query execution meta-info
    results:
      type: array
      items:
        type: object
        properties:
          edge:
            type: onject
            additionalProperties: true
            description: Ontology term relation edge data; Standard RE database fields, plus all additional document-specific fields.
          term:
            type: onject
            additionalProperties: true
            description: Ontology term data; Standard RE database fields, plus all additional document-specific fields.
```

### Timestamp parameter

Every method for this API can take a `ts` parameter, representing the Unix
epoch time (in milliseconds) of when the document was active in the
database. This is optional and defaults to the current time.

### Namespace parameter

Every method for this API can take a `ns` parameter, representing the ontology namespace to use. This is optional and defaults to `go`.

## Methods

### get_descendants

Retrieve the descendants of an ontolgy term

Example:
ret = OntologyAPI.get_descendants(self.ctx, {"id": "GO:0000002, "ts":1568820853135})

See the **Params** section for params schema.
See the **Result** section for result schema.

### get_ancestors

Retrieve the ancestors of an ontolgy term

Example:
ret = OntologyAPI.get_ancestors(self.ctx, {"id": "GO:0000002, "ts":1568820853135})

See the **Params** section for params schema.
See the **Result** section for result schema.

### get_children

Retrieve the children of an ontolgy term

Example:
ret = OntologyAPI.get_children(self.ctx, {"id": "GO:0000002, "ts":1568820853135})

See the **Params** section for params schema.
See the **Result** section for result schema.

### get_parents

Retrieve the parents of an ontolgy term

Example:
ret = OntologyAPI.get_parents(self.ctx, {"id": "GO:0000002, "ts":1568820853135})

See the **Params** section for params schema.
See the **Result** section for result schema.

### get_related

Retrieve the related of an ontolgy term

Example:
ret = OntologyAPI.get_related(self.ctx, {"id": "GO:0000002, "ts":1568820853135})

See the **Params** section for params schema.
See the **Result** section for result schema.

### get_siblings

Retrieve the siblings of an ontolgy term

Example:
ret = OntologyAPI.get_siblings(self.ctx, {"id": "GO:0000002, "ts":1568820853135})

See the **Params** section for params schema.
See the **Result** section for result schema.

### get_terms

Retrieve the metadata of a list of ontolgy terms

Example:
ret = OntologyAPI.get_terms(self.ctx, {"ids": ["GO:0000002, "GO:0000266"], "ts":1568820853135})

It has following params schema:
```yaml
type: object
required: ['ids']
properties:
  ids:
    type: array
    items:
      type: string
      description: The list of Go term IDs to be fetched
      maxItems: 10000
  ts:
    type: integer
```

It has following reult schema:
```yaml
type: array
minItems: 1
maxItems: 1
items:
  type: object
  properties:
    ts:
      type: integer
      title: Timestamp used in the request, default is current time
    stats:
      type: object
      description: RE query execution meta-info
    results:
      type: array
      items:
        type: object
        additionalProperties: true
        description: Ontology term data; Standard RE database fields, plus all additional document-specific fields.
```

### get_hierarchicalDescendants

Retrieve the hierarchicalDescendants of an ontolgy term

Example:
ret = OntologyAPI.get_hierarchicalDescendants(self.ctx, {"id": "GO:0000002, "ts":1568820853135})

See the **Params** section for params schema.
See the **Result** section for result schema.

### get_hierarchicalAncestors

Retrieve the hierarchicalAncestors of an ontolgy term

Example:
ret = OntologyAPI.get_hierarchicalAncestors(self.ctx, {"id": "GO:0000002, "ts":1568820853135})

See the **Params** section for params schema.
See the **Result** section for result schema.

### get_hierarchicalChildren

Retrieve the hierarchicalChildren of an ontolgy term

Example:
ret = OntologyAPI.get_hierarchicalChildren(self.ctx, {"id": "GO:0000002, "ts":1568820853135})

See the **Params** section for params schema.
See the **Result** section for result schema.

### get_hierarchicalParents

Retrieve the hierarchicalParents of an ontolgy term

Example:
ret = OntologyAPI.get_hierarchicalParents(self.ctx, {"id": "GO:0000002, "ts":1568820853135})

See the **Params** section for params schema.
See the **Result** section for result schema.

# Installation from another module

To use this code in another SDK module, call `kb-sdk install OntologyAPI` in the other module's root directory.

# Help

You may find the answers to your questions in our [FAQ](https://kbase.github.io/kb_sdk_docs/references/questions_and_answers.html) or [Troubleshooting Guide](https://kbase.github.io/kb_sdk_docs/references/troubleshooting.html).
# ontology_api
