/*
A KBase module: OntologyAPI
*/

module OntologyAPI {
    
    /* A boolean. 0 = false, other = true. */
    typedef int boolean;
    
    /* GoID : Unique GO term id (Source: external Gene Ontology database - http://www.geneontology.org/) */
    typedef string GoID;

    typedef structure {
        GoID key;
        int  limit;
        int  offset;
    } InputParams;

    typedef list<GoID> GoIDList;

    /**
     * Retrieve descendants
     * @return descendants
     */
    funcdef get_descendants(InputParams) returns (GoIDList) authentication optional;
    funcdef get_ancestors(InputParams) returns (GoIDList) authentication optional;
    funcdef get_children(InputParams) returns (GoIDList) authentication optional;
    funcdef get_parents(InputParams) returns (GoIDList) authentication optional;
    funcdef get_related(InputParams) returns (GoIDList) authentication optional;
    funcdef get_siblings(InputParams) returns (GoIDList) authentication optional;
    funcdef get_metadata(InputParams) returns (GoIDList) authentication optional;
    funcdef get_hierarchicalAncestors(InputParams) returns (GoIDList) authentication optional;
    funcdef get_hierarchicalChildren(InputParams) returns (GoIDList) authentication optional;
    funcdef get_hierarchicalDescendants(InputParams) returns (GoIDList) authentication optional;
    funcdef get_hierarchicalParents(InputParams) returns (GoIDList) authentication optional;
};
