/*
A KBase module: OntologyAPI
*/

module OntologyAPI {
    
    /* A boolean. 0 = false, other = true. */
    typedef int boolean;
    
    /* TermID : Unique ontology term id */
    typedef string TermID;

    typedef structure {
        TermID key;
        string name_space;
        int  limit;
        int  offset;
    } InputParams;

    typedef list<TermID> TermIDList;

    /**
     * Retrieve descendants
     * @return descendants
     */
    funcdef get_descendants(InputParams) returns (TermIDList) authentication optional;
    funcdef get_ancestors(InputParams) returns (TermIDList) authentication optional;
    funcdef get_children(InputParams) returns (TermIDList) authentication optional;
    funcdef get_parents(InputParams) returns (TermIDList) authentication optional;
    funcdef get_related(InputParams) returns (TermIDList) authentication optional;
    funcdef get_siblings(InputParams) returns (TermIDList) authentication optional;
    funcdef get_metadata(InputParams) returns (TermIDList) authentication optional;
    funcdef get_hierarchicalAncestors(InputParams) returns (TermIDList) authentication optional;
    funcdef get_hierarchicalChildren(InputParams) returns (TermIDList) authentication optional;
    funcdef get_hierarchicalDescendants(InputParams) returns (TermIDList) authentication optional;
    funcdef get_hierarchicalParents(InputParams) returns (TermIDList) authentication optional;
};
