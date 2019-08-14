/*
A KBase module: OntologyAPI
*/

module OntologyAPI {
    
    /* A boolean. 0 = false, other = true. */
    typedef int boolean;
    
    /* GoID : Unique GO term id (Source: external Gene Ontology database - http://www.geneontology.org/) */
    typedef string GoID;

    typedef list<GoID> GoIDList;

    /**
     * Retrieve descendants
     * @return descendants
     */
    funcdef get_descendants(GoID) returns (GoIDList) authentication optional;
};
