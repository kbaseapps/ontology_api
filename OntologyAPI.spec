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
      Parameters for get_terms
      ids - required - a list of name ontology term id, such as '["GO:0000002", "GO:0000266"]'
      ts - optional - fetch documents with this active timestamp, defaults to now
      ns - optional - ontology namespace to use, defaults to "go"
    */
    typedef structure {
        list<ID>  ids;
        int ts;
        string  ns;
    } GetTermsParams;
    
    /*
      Parameters for get_terms_from_ws_obj
      obj_ref - required - workspace object ref, such as "44640/9/1"
      ts - optional - fetch documents with this active timestamp, defaults to now
      ns - optional - ontology namespace to use, defaults to "go"
    */
    typedef structure {
      string  obj_ref;
      string  ns;
      int ts;
    } GetTermsFromWSObjParams;

    /*
      Parameters for get_terms_from_ws_feature
      obj_ref - required - workspace object ref, such as "44640/9/1"
      feature_id - required - workspace feature id, such as "b3908"
      ts - optional - fetch documents with this active timestamp, defaults to now
      ns - optional - ontology namespace to use, defaults to "go"
    */
    typedef structure {
      string  obj_ref;
      string  feature_id;
      string  ns;
      int ts;
    } GetTermsFromWSFeatureParams;

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
      total_count - total count of features associated.
      results - array of WSObjWithWSFeatures objects.
    */
    typedef structure {
      int total_count;
      list<WSObjWithWSFeatures> results;
    } WSObjectsResults;

    /*
      Results from get_associated_ws_objects
      stats - Query execution information from ArangoDB.
      results - array of WSObjectsResults objects.
      ts - Timestamp used in the request
      ns - Ontology namespace used in the request.
    */
    typedef structure {
        UnspecifiedObject stats;
        list<WSObjectsResults> results;
        int ts;
        string ns;
    } GetAssociatedWSObjectsResults;

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

    /* Retrieve associated workspace objects of an ontology term by ID*/
    funcdef get_associated_ws_objects(GenericParams) returns (GetAssociatedWSObjectsResults) authentication optional;

    /* Retrieve ontology terms of an workspace genome feature by genome obj_ref and feature id*/
    funcdef get_terms_from_ws_feature(GetTermsFromWSFeatureParams) returns (GetTermsFromWSFeatureResults) authentication optional;

    /* Retrieve ontology terms of an workspace object by workspace obj_ref*/
    funcdef get_terms_from_ws_obj(GetTermsFromWSObjParams) returns (GetTermsFromWSObjResults) authentication optional;
};
