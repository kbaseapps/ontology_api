/*
A KBase module: OntologyAPI
*/

module OntologyAPI {
    
    /* A boolean. 0 = false, other = true. */
    typedef int boolean;
    
    /*
      Ontology term id, such as "GO:0000002"
    */
    typedef string ID;

    /*
      Ontology term 
    */
    typedef structure {
      ID  id;
      string  name;
      string  namespace;
      list<string>  alt_ids;
      UnspecifiedObject  def;
      list<string>  comments;
      list<UnspecifiedObject>  synonyms;
      list<UnspecifiedObject>  xrefs;
      int created;
      int expired;
    } Term;

    /*
      workspace object
    */
    typedef structure {
      int workspace_id;
      int object_id;
      int version;
      string  name;
    } WSObj;

    /*
      workspace genome feature
    */
    typedef structure {
      string  feature_id;
      int updated_at;
      int workspace_id;
      int object_id;
      int version;
    } Feature;

    /*
      workspace genome feature, lite version
    */
    typedef structure {
      string  feature_id;
      int updated_at;
    } FeatureLite;

    /*
      Ontology terms with associated workspace genome feature
      terms - a list of Term object
      feature - Feature object
    */
    typedef structure {
      list<Term> terms;
      Feature feature;
    } TermsWithWSFeature;

    /*
      Workspace obj with associated workspace genome features
      ws_obj - WSObj object
      features - a list of FeatureLite object
    */
    typedef structure {
      WSObj ws_obj;
      list<FeatureLite> features;
    } WSObjWithWSFeatures;

    /* 
      Workspace obj with count of associated workspace genome features
      feature_count - count of features associated.
      ws_obj - WSObj object
    */
    typedef structure {
      int feature_count;
      WSObj ws_obj;
    } WSObjectsWithFeatureCount;

    /*
      Parameters for get_terms
      ids - required - a list of ontology term id, such as '["GO:0000002", "GO:0000266"]'
      ts - optional - fetch documents with this active timestamp, defaults to now
      ns - optional - ontology namespace to use, defaults to "go"
      limit - optional - number of results to return (defaults to 20)
      offset - optional - number of results to skip (defaults to 0)
    */
    typedef structure {
        list<ID>  ids;
        int ts;
        string  ns;
        int  limit;
        int  offset;
    } GetTermsParams;
    
    /*
      Parameters for get_terms_from_ws_feature
      id - required - ontology term id, such as "GO:0016209"
      obj_ref - optional - workspace object ref, such as "6976/926/2"
      ts - optional - fetch documents with this active timestamp, defaults to now
      ns - optional - ontology namespace to use, defaults to "go"
      limit - optional - number of results to return (defaults to 20)
      offset - optional - number of results to skip (defaults to 0)
    */
    typedef structure {
        ID  id;
        string  obj_ref;
        string  ns;
        int ts;
        int  limit;
        int  offset;
    } GetAssociatedWSFeaturesParams;

    /*
      Parameters for get_terms_from_ws_object
      obj_ref - required - workspace object ref, such as "6976/926/2"
      ts - optional - fetch documents with this active timestamp, defaults to now
      ns - optional - ontology namespace to use, defaults to "go"
      limit - optional - number of results to return (defaults to 20)
      offset - optional - number of results to skip (defaults to 0)
    */
    typedef structure {
        string  obj_ref;
        string  ns;
        int ts;
        int  limit;
        int  offset;
    } GetTermsFromWSObjParams;

    /*
      Parameters for get_terms_from_ws_feature
      obj_ref - required - workspace object ref, such as "6976/926/2"
      feature_id - required - workspace feature id, such as "b3908"
      ts - optional - fetch documents with this active timestamp, defaults to now
      ns - optional - ontology namespace to use, defaults to "go"
      limit - optional - number of results to return (defaults to 20)
      offset - optional - number of results to skip (defaults to 0)
    */
    typedef structure {
        string  obj_ref;
        string  feature_id;
        string  ns;
        int ts;
        int  limit;
        int  offset;
    } GetTermsFromWSFeatureParams;

    /*
      Parameters for get_term_by_name
      name - required - ontology name for search, such as "terrestrial biome"
      ancestor_term - optional - ontology term id of an ancestor ontology node
      ts - optional - fetch documents with this active timestamp, defaults to now
      ns - optional - ontology namespace to use, defaults to "go"
      limit - optional - number of results to return (defaults to 20)
      offset - optional - number of results to skip (defaults to 0)
    */
    typedef structure {
        string name;
        ID ancestor_term;
        int ts;
        string ns;
        int  limit;
        int  offset;
    } GetTermByNameParams;

    /*
      Generic Parameters 
      id - required - ontology term id, such as "GO:0016209"
      ts - optional - fetch documents with this active timestamp, defaults to now
      ns - optional - ontology namespace to use, defaults to "go"
      limit - optional - number of results to return (defaults to 20)
      offset - optional - number of results to skip (defaults to 0)
    */
    typedef structure {
        ID  id;
        int ts;
        string ns;
        int  limit;
        int  offset;
    } GenericParams;

    /*
      Generic results
      stats - Query execution information from ArangoDB.
      results - array of objects of results.
      ts - Timestamp used in the request
      ns - Ontology namespace used in the request.
    */
    typedef structure {
        UnspecifiedObject stats;
        list<UnspecifiedObject> results;
        int ts;
        string ns;
    } GenericResults;

    /*
      Results from get_associated_ws_objects
      stats - Query execution information from ArangoDB.
      results - array of WSObjectsResults objects.
      ts - Timestamp used in the request
      ns - Ontology namespace used in the request.
      total_count - total count of associated workspace objects
    */
    typedef structure {
        UnspecifiedObject stats;
        list<WSObjectsWithFeatureCount> results;
        int ts;
        string ns;
        int total_count;
    } GetAssociatedWSObjectsResults;

    /* 
      Sample data with sample_metadata_key
      id - sample id
      name - sample name
      node_tree - sample metadata
      save_date - sample data saved date
      version - sample data version
      sample_metadata_key - metadata key referencing ontology term
    */
    typedef structure {
        string id;
        string name;
        UnspecifiedObject node_tree;
        int save_date;
        int version;
        string sample_metadata_key;
    } SampleWithMetadataKey;

    /*
      Results from get_associated_ws_features
      stats - Query execution information from ArangoDB.
      results - array of WSObjectsResults objects.
      ts - Timestamp used in the request
      ns - Ontology namespace used in the request.
      total_count - total count of associated workspace features
    */
    typedef structure {
        UnspecifiedObject stats;
        list<WSObjWithWSFeatures> results;
        int ts;
        string ns;
        int total_count;
    } GetAssociatedWSFeaturesResults;

    /*
      Results from get_associated_samples
      stats - Query execution information from ArangoDB.
      results - array of SampleWithMetadataKey objects.
      ts - Timestamp used in the request
      ns - Ontology namespace used in the request.
      total_count - total count of associated samples
    */
    typedef structure {
        UnspecifiedObject stats;
        list<SampleWithMetadataKey> results;
        int ts;
        string ns;
        int total_count;
    } GetAssociatedSamplesResults;

    /*
      Results from get_terms_from_ws_feature
      stats - Query execution information from ArangoDB.
      results - array of TermsWithWSFeature objects.
      ts - Timestamp used in the request
      ns - Ontology namespace used in the request.
    */
    typedef structure {
        UnspecifiedObject stats;
        list<TermsWithWSFeature> results;
        int ts;
        string ns;
    } GetTermsFromWSFeatureResults;

    /*
      Results from get_terms_from_ws_obj
      stats - Query execution information from ArangoDB.
      results - array of TermsWithWSFeature objects.
      ts - Timestamp used in the request
      ns - Ontology namespace used in the request.
    */
    typedef structure {
        UnspecifiedObject stats;
        list<TermsWithWSFeature> results;
        int ts;
        string ns;
    } GetTermsFromWSObjResults;

    typedef structure {
      UnspecifiedObject namespaces;
    } GetNamespacesResults;

    /* Retrieve descendants of an ontology term by ID*/
    funcdef get_descendants(GenericParams) returns (GenericResults) authentication optional;

    /* Retrieve ancestors of an ontology term by ID*/
    funcdef get_ancestors(GenericParams) returns (GenericResults) authentication optional;

    /* Retrieve children of an ontology term by ID*/
    funcdef get_children(GenericParams) returns (GenericResults) authentication optional;

    /* Retrieve parents of an ontology term by ID*/
    funcdef get_parents(GenericParams) returns (GenericResults) authentication optional;

    /* Retrieve related terms of an ontology term by ID*/
    funcdef get_related(GenericParams) returns (GenericResults) authentication optional;

    /* Retrieve siblings terms of an ontology term by ID*/
    funcdef get_siblings(GenericParams) returns (GenericResults) authentication optional;

    /* Retrieve metadata of a list of ontology terms by IDs*/
    funcdef get_terms(GetTermsParams) returns (GenericResults) authentication optional;

    /* Retrieve hierarchical_ancestors of an ontology term by ID*/
    funcdef get_hierarchical_ancestors(GenericParams) returns (GenericResults) authentication optional;

    /* Retrieve hierarchical_children of an ontology term by ID*/
    funcdef get_hierarchical_children(GenericParams) returns (GenericResults) authentication optional;

    /* Retrieve hierarchical_descendants of an ontology term by ID*/
    funcdef get_hierarchical_descendants(GenericParams) returns (GenericResults) authentication optional;

    /* Retrieve hierarchical_parents of an ontology term by ID*/
    funcdef get_hierarchical_parents(GenericParams) returns (GenericResults) authentication optional;

    /* Retrieve associated workspace genome objects of an ontology term by ID*/
    funcdef get_associated_ws_genomes(GenericParams) returns (GetAssociatedWSObjectsResults) authentication optional;

    /* Retrieve associated workspace genome features of an ontology term by ID and workspace obj_ref*/
    funcdef get_associated_ws_features(GetAssociatedWSFeaturesParams) returns (GetAssociatedWSFeaturesResults) authentication optional;

    /* Retrieve ontology terms of an workspace genome feature by workspace obj_ref and feature id*/
    funcdef get_terms_from_ws_feature(GetTermsFromWSFeatureParams) returns (GetTermsFromWSFeatureResults) authentication optional;

    /* Retrieve ontology terms of an workspace object by workspace obj_ref*/
    funcdef get_terms_from_ws_object(GetTermsFromWSObjParams) returns (GetTermsFromWSObjResults) authentication optional;

    /* Retrieve associated samples of an ontology term by ID*/
    funcdef get_associated_samples(GenericParams) returns (GetAssociatedSamplesResults) authentication optional;

    /* Retrieve ontology term by name */
    funcdef get_term_by_name(GetTermByNameParams) returns (GenericResults) authentication optional;

    funcdef get_namespaces() returns (GetNamespacesResults results) authentication required;
};
