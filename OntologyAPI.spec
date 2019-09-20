/*
A KBase module: OntologyAPI
*/

module OntologyAPI {
    
    /* A boolean. 0 = false, other = true. */
    typedef int boolean;
    
    /* ID : name space/ontology term id */
    typedef string ID;

    /* ID : name space/ontology term id */
    typedef structure {
        ID  id;
        int ts;
        int  limit;
        int  offset;
    } InputParams;

    /*
     * Generic results
     * stats - Query execution information from ArangoDB.
     * results - array of objects of results.
     */
    typedef structure {
        UnspecifiedObject stats;
        list<UnspecifiedObject> results;
    } Results;

    /**
     * Retrieve descendants
     * @return descendants
     */
    funcdef get_descendants(InputParams) returns (Results) authentication optional;
    funcdef get_ancestors(InputParams) returns (Results) authentication optional;
    funcdef get_children(InputParams) returns (Results) authentication optional;
    funcdef get_parents(InputParams) returns (Results) authentication optional;
    funcdef get_related(InputParams) returns (Results) authentication optional;
    funcdef get_siblings(InputParams) returns (Results) authentication optional;
    funcdef get_metadata(InputParams) returns (Results) authentication optional;
    funcdef get_hierarchicalAncestors(InputParams) returns (Results) authentication optional;
    funcdef get_hierarchicalChildren(InputParams) returns (Results) authentication optional;
    funcdef get_hierarchicalDescendants(InputParams) returns (Results) authentication optional;
    funcdef get_hierarchicalParents(InputParams) returns (Results) authentication optional;
};
