/*
A KBase module: OntologyAPI
*/

module OntologyAPI {
    
    /* A boolean. 0 = false, other = true. */
    typedef int boolean;
    
    /*
      ID : ontology term id, such as "GO:0000002"
    */
    typedef string ID;

    /*
      Parameters for get_terms
      ids - required - a list of name ontology term id, such as '["GO:0000002", "GO:0000266"]'
      ts - optional - fetch documents with this active timestamp, defaults to now
      ns - optional - ontology namespace to use, defaults to "go"
    */
    typedef structure {
        list<ID>  ids;
        int ts;
        string ns;
    } GetTermsParams;

    /*
      Generic Parameters 
      id - required - ontology term id, such as "GO:0000002"
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

    /* Retrieve hierarchicalAncestors of an ontology term by ID*/
    funcdef get_hierarchicalAncestors(GenericParams) returns (GenericResults) authentication optional;

    /* Retrieve hierarchicalChildren of an ontology term by ID*/
    funcdef get_hierarchicalChildren(GenericParams) returns (GenericResults) authentication optional;

    /* Retrieve hierarchicalDescendants of an ontology term by ID*/
    funcdef get_hierarchicalDescendants(GenericParams) returns (GenericResults) authentication optional;

    /* Retrieve hierarchicalParents of an ontology term by ID*/
    funcdef get_hierarchicalParents(GenericParams) returns (GenericResults) authentication optional;
};
