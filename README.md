# Ontology API for KBase using Relation Engine

This is an API for ontology data that queries the relation engine.

## API

The InputParams should be an object containing `id` field with value `ontology namespace/ontology term id`, ex. {"id": "go_ontology/GO:0000002"}

### get_descendants

Retrieve the descendants document data for an ontolgy term

Example:
ret = OntologyAPI.get_descendants(self.ctx, {"id": "go_ontology/GO:0000002"})

```

```
# Installation from another module

To use this code in another SDK module, call `kb-sdk install OntologyAPI` in the other module's root directory.

# Help

You may find the answers to your questions in our [FAQ](https://kbase.github.io/kb_sdk_docs/references/questions_and_answers.html) or [Troubleshooting Guide](https://kbase.github.io/kb_sdk_docs/references/troubleshooting.html).
# ontology_api
