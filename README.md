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
      title: Timestamp used in the request
    ns:
      type: string
      title: Ontology namespace used in the request
    stats:
      type: object
      description: RE query execution meta-info
    results:
      type: array
      items:
        type: object
        properties:
          edge:
            type: object
            additionalProperties: true
            description: Ontology term relation edge data; Standard RE database fields, plus all additional document-specific fields.
          term:
            type: object
            additionalProperties: true
            description: Ontology term data; Standard RE database fields, plus all additional document-specific fields.
```

### Timestamp parameter

Every method for this API can take a `ts` parameter, representing the Unix
epoch time (in milliseconds) of when the document was active in the
database. This is optional and defaults to the current time.

### Namespace parameter

Every method for this API can take a `ns` parameter, representing the ontology namespace to use. This is optional and defaults to `go_ontology`.

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
  ns:
    type: string
  limit:
    type: integer
    maximum: 1000
  offset:
    type: integer
    maximum: 100000
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
    ns:
      type: string
      title: Ontology namespace used in the request
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

### get_hierarchical_descendants

Retrieve the hierarchical_descendants of an ontolgy term

Example:
ret = OntologyAPI.get_hierarchical_descendants(self.ctx, {"id": "GO:0000002, "ts":1568820853135})

See the **Params** section for params schema.
See the **Result** section for result schema.

### get_hierarchical_ancestors

Retrieve the hierarchical_ancestors of an ontolgy term

Example:
ret = OntologyAPI.get_hierarchical_ancestors(self.ctx, {"id": "GO:0000002, "ts":1568820853135})

See the **Params** section for params schema.
See the **Result** section for result schema.

### get_hierarchical_children

Retrieve the hierarchical_children of an ontolgy term

Example:
ret = OntologyAPI.get_hierarchical_children(self.ctx, {"id": "GO:0000002, "ts":1568820853135})

See the **Params** section for params schema.
See the **Result** section for result schema.

### get_hierarchical_parents

Retrieve the hierarchical_parents of an ontolgy term

Example:
ret = OntologyAPI.get_hierarchical_parents(self.ctx, {"id": "GO:0000002, "ts":1568820853135})

See the **Params** section for params schema.
See the **Result** section for result schema.

### get_associated_ws_objects

Retrieve associated workspace objects of an ontology term

Example:
ret = OntologyAPI.get_associated_ws_objects(self.ctx, {"id": "GO:0016209"})

See the **Params** section for params schema.

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
    ns:
      type: string
      title: Ontology namespace used in the request
    total_count:
      type: integer
      title: total count of associated workspace objects
    stats:
      type: object
      description: RE query execution meta-info
    results:
      type: array
      items:
        type: object
        properties: 
            ws_obj:
              type: object
              description: workspace object
              properties:
                workspace_id: 
                  type: integer
                object_id:
                  type: integer
                version:
                  type: integer
                name:
                  type: string
            feature_count:
              type: integer
```

### get_associated_ws_features

Retrieve associated workspace genome features of an ontology term by ID and workspace obj_ref

Example:
ret = OntologyAPI.get_associated_ws_features(self.ctx, {"id": "GO:0016209", "obj_ref": "4258/36981/3"})

It has following params schema:
```yaml
type: object
required: ['id']
properties:
  id:
    type: string
  obj_ref:
    type: string
    description: workspace object ref
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
    ns:
      type: string
      title: Ontology namespace used in the request
    total_count:
      type: integer
      title: total count of associated workspace features
    stats:
      type: object
      description: RE query execution meta-info
    results:
      type: array
      items:
        type: object
          properties:
            ws_obj:
              type: object
              description: workspace object
              properties:
                workspace_id: 
                  type: integer
                object_id:
                  type: integer
                version:
                  type: integer
                name:
                  type: string
            features:
              type: array
              items:
                type: object
                description: workspace feature 
                properties:
                  feature_id:
                    type: string
                  updated_at:
                    type: integer
```

### get_terms_from_ws_feature

Retrieve ontology terms of an workspace genome feature by genome obj_ref and feature id

Example:
ret = OntologyAPI.get_terms_from_ws_feature(self.ctx, {"obj_ref": "4258/36981/3", "feature_id": "Thecc1EG022426"})

It has following params schema:
```yaml
type: object
required: ['obj_ref', 'feature_id']
properties:
  obj_ref:
    type: string
    description: workspace object ref
  feature_id:
    type: string
    description: workspace feature id
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
    ns:
      type: string
      title: Ontology namespace used in the request
    stats:
      type: object
      description: RE query execution meta-info
    results:
      type: array
      items:
        type: object
        properties:
          feature:
            type: object
            description: workspace feature
            properties:
              feature_id:
                type: string
              workspace_id: 
                type: integer
              object_id:
                type: integer
              version:
                type: integer
              updated_at:
                type: integer
          terms:
            type: array
            items:
              type: object
              description: Onyology term 
              properties:
                name:
                  type: string
                namespace:
                  type: string
                alt_ids:
                  type: array
                  items:
                    type: string
                    description: alternative id
                def:
                  type: object
                  descriptionL definition
                comments:
                  type: array
                  items:
                    type: string
                synonyms:
                  type: array
                  items:
                    type: object
                xrefs:
                  type: array
                  items:
                    type: object
                created:
                  type: integer
                expired:
                  type: integer
```

### get_terms_from_ws_obj

Retrieve ontology terms of an workspace object by workspace obj_ref

Example:
ret = OntologyAPI.get_terms_from_ws_obj(self.ctx, {"obj_ref": "4258/36981/3"})

It has following params schema:
```yaml
type: object
required: ['obj_ref']
properties:
  obj_ref:
    type: string
    description: workspace object ref
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
See the **get_terms_from_ws_feature** section for result schema.

# Installation from another module

To use this code in another SDK module, call `kb-sdk install OntologyAPI` in the other module's root directory.

# Help

You may find the answers to your questions in our [FAQ](https://kbase.github.io/kb_sdk_docs/references/questions_and_answers.html) or [Troubleshooting Guide](https://kbase.github.io/kb_sdk_docs/references/troubleshooting.html).
# ontology_api
