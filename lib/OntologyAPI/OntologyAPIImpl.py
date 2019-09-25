# -*- coding: utf-8 -*-
#BEGIN_HEADER
import logging
import os
import re

from OntologyAPI.utils import re_api, misc
from pprint import pprint
#END_HEADER


class OntologyAPI:
    '''
    Module Name:
    OntologyAPI

    Module Description:
    A KBase module: OntologyAPI
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = "https://github.com/kbaseapps/ontology_api"
    GIT_COMMIT_HASH = "3e11237bcf2d04f0e1d6a0a8aa889407e41a5c9e"

    #BEGIN_CLASS_HEADER
    def validate_params(self, params, schema='default'):
        _params = misc.validate_params(params, schema);
        return _params
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.shared_folder = config['scratch']
        logging.basicConfig(format='%(created)s %(levelname)s: %(message)s',
                            level=logging.INFO)
        #END_CONSTRUCTOR
        pass


    def get_descendants(self, ctx, GenericParams):
        """
        Retrieve descendants of an ontology term by ID
        :param GenericParams: instance of type "GenericParams" (Generic
           Parameters id - required - ontology term id, such as "GO:0000002"
           ts - optional - fetch documents with this active timestamp,
           defaults to now ns - optional - ontology namespace to use,
           defaults to "go" limit - optional - number of results to return
           (defaults to 20) offset - optional - number of results to skip
           (defaults to 0)) -> structure: parameter "id" of type "ID" (ID :
           ontology term id, such as "GO:0000002"), parameter "ts" of Long,
           parameter "ns" of String, parameter "limit" of Long, parameter
           "offset" of Long
        :returns: instance of type "GenericResults" (Generic results stats -
           Query execution information from ArangoDB. results - array of
           objects of results.) -> structure: parameter "stats" of
           unspecified object, parameter "results" of list of unspecified
           object, parameter "ts" of Long
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_descendants
        validated_params=self.validate_params(GenericParams);
        results = re_api.query("get_descendants", validated_params)

        returnVal={"stats": results["stats"], "results": results["results"], "ts": validated_params["ts"]}
        #END get_descendants

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method get_descendants return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def get_ancestors(self, ctx, GenericParams):
        """
        Retrieve ancestors of an ontology term by ID
        :param GenericParams: instance of type "GenericParams" (Generic
           Parameters id - required - ontology term id, such as "GO:0000002"
           ts - optional - fetch documents with this active timestamp,
           defaults to now ns - optional - ontology namespace to use,
           defaults to "go" limit - optional - number of results to return
           (defaults to 20) offset - optional - number of results to skip
           (defaults to 0)) -> structure: parameter "id" of type "ID" (ID :
           ontology term id, such as "GO:0000002"), parameter "ts" of Long,
           parameter "ns" of String, parameter "limit" of Long, parameter
           "offset" of Long
        :returns: instance of type "GenericResults" (Generic results stats -
           Query execution information from ArangoDB. results - array of
           objects of results.) -> structure: parameter "stats" of
           unspecified object, parameter "results" of list of unspecified
           object, parameter "ts" of Long
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_ancestors
        validated_params=self.validate_params(GenericParams);
        results = re_api.query("get_ancestors", validated_params)

        returnVal={"stats": results["stats"], "results": results["results"], "ts": validated_params["ts"]}
        #END get_ancestors

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method get_ancestors return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def get_children(self, ctx, GenericParams):
        """
        Retrieve children of an ontology term by ID
        :param GenericParams: instance of type "GenericParams" (Generic
           Parameters id - required - ontology term id, such as "GO:0000002"
           ts - optional - fetch documents with this active timestamp,
           defaults to now ns - optional - ontology namespace to use,
           defaults to "go" limit - optional - number of results to return
           (defaults to 20) offset - optional - number of results to skip
           (defaults to 0)) -> structure: parameter "id" of type "ID" (ID :
           ontology term id, such as "GO:0000002"), parameter "ts" of Long,
           parameter "ns" of String, parameter "limit" of Long, parameter
           "offset" of Long
        :returns: instance of type "GenericResults" (Generic results stats -
           Query execution information from ArangoDB. results - array of
           objects of results.) -> structure: parameter "stats" of
           unspecified object, parameter "results" of list of unspecified
           object, parameter "ts" of Long
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_children
        validated_params=self.validate_params(GenericParams);
        results = re_api.query("get_children", validated_params)

        returnVal={"stats": results["stats"], "results": results["results"], "ts": validated_params["ts"]}
        #END get_children

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method get_children return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def get_parents(self, ctx, GenericParams):
        """
        Retrieve parents of an ontology term by ID
        :param GenericParams: instance of type "GenericParams" (Generic
           Parameters id - required - ontology term id, such as "GO:0000002"
           ts - optional - fetch documents with this active timestamp,
           defaults to now ns - optional - ontology namespace to use,
           defaults to "go" limit - optional - number of results to return
           (defaults to 20) offset - optional - number of results to skip
           (defaults to 0)) -> structure: parameter "id" of type "ID" (ID :
           ontology term id, such as "GO:0000002"), parameter "ts" of Long,
           parameter "ns" of String, parameter "limit" of Long, parameter
           "offset" of Long
        :returns: instance of type "GenericResults" (Generic results stats -
           Query execution information from ArangoDB. results - array of
           objects of results.) -> structure: parameter "stats" of
           unspecified object, parameter "results" of list of unspecified
           object, parameter "ts" of Long
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_parents
        validated_params=self.validate_params(GenericParams);
        results = re_api.query("get_parents", validated_params)

        returnVal={"stats": results["stats"], "results": results["results"], "ts": validated_params["ts"]}
        #END get_parents

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method get_parents return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def get_related(self, ctx, GenericParams):
        """
        Retrieve related terms of an ontology term by ID
        :param GenericParams: instance of type "GenericParams" (Generic
           Parameters id - required - ontology term id, such as "GO:0000002"
           ts - optional - fetch documents with this active timestamp,
           defaults to now ns - optional - ontology namespace to use,
           defaults to "go" limit - optional - number of results to return
           (defaults to 20) offset - optional - number of results to skip
           (defaults to 0)) -> structure: parameter "id" of type "ID" (ID :
           ontology term id, such as "GO:0000002"), parameter "ts" of Long,
           parameter "ns" of String, parameter "limit" of Long, parameter
           "offset" of Long
        :returns: instance of type "GenericResults" (Generic results stats -
           Query execution information from ArangoDB. results - array of
           objects of results.) -> structure: parameter "stats" of
           unspecified object, parameter "results" of list of unspecified
           object, parameter "ts" of Long
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_related
        validated_params=self.validate_params(GenericParams);
        results = re_api.query("get_related", validated_params)

        returnVal={"stats": results["stats"], "results": results["results"], "ts": validated_params["ts"]}
        #END get_related

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method get_related return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def get_siblings(self, ctx, GenericParams):
        """
        Retrieve siblings terms of an ontology term by ID
        :param GenericParams: instance of type "GenericParams" (Generic
           Parameters id - required - ontology term id, such as "GO:0000002"
           ts - optional - fetch documents with this active timestamp,
           defaults to now ns - optional - ontology namespace to use,
           defaults to "go" limit - optional - number of results to return
           (defaults to 20) offset - optional - number of results to skip
           (defaults to 0)) -> structure: parameter "id" of type "ID" (ID :
           ontology term id, such as "GO:0000002"), parameter "ts" of Long,
           parameter "ns" of String, parameter "limit" of Long, parameter
           "offset" of Long
        :returns: instance of type "GenericResults" (Generic results stats -
           Query execution information from ArangoDB. results - array of
           objects of results.) -> structure: parameter "stats" of
           unspecified object, parameter "results" of list of unspecified
           object, parameter "ts" of Long
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_siblings
        validated_params=self.validate_params(GenericParams);
        results = re_api.query("get_siblings", validated_params)

        returnVal={"stats": results["stats"], "results": results["results"], "ts": validated_params["ts"]}
        #END get_siblings

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method get_siblings return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def get_terms(self, ctx, GetTermsParams):
        """
        Retrieve metadata of a list of ontology terms by IDs
        :param GetTermsParams: instance of type "GetTermsParams" (Parameters
           for get_terms ids - required - a list of name ontology term id,
           such as '["GO:0000002", "GO:0000266"]' ts - optional - fetch
           documents with this active timestamp, defaults to now ns -
           optional - ontology namespace to use, defaults to "go") ->
           structure: parameter "ids" of list of type "ID" (ID : ontology
           term id, such as "GO:0000002"), parameter "ts" of Long, parameter
           "ns" of String
        :returns: instance of type "GenericResults" (Generic results stats -
           Query execution information from ArangoDB. results - array of
           objects of results.) -> structure: parameter "stats" of
           unspecified object, parameter "results" of list of unspecified
           object, parameter "ts" of Long
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_terms
        validated_params=self.validate_params(GetTermsParams, "get_terms");
        results = re_api.query("get_terms", validated_params)

        returnVal={"stats": results["stats"], "results": results["results"], "ts": validated_params["ts"]}
        #END get_terms

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method get_terms return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def get_hierarchicalAncestors(self, ctx, GenericParams):
        """
        Retrieve hierarchicalAncestors of an ontology term by ID
        :param GenericParams: instance of type "GenericParams" (Generic
           Parameters id - required - ontology term id, such as "GO:0000002"
           ts - optional - fetch documents with this active timestamp,
           defaults to now ns - optional - ontology namespace to use,
           defaults to "go" limit - optional - number of results to return
           (defaults to 20) offset - optional - number of results to skip
           (defaults to 0)) -> structure: parameter "id" of type "ID" (ID :
           ontology term id, such as "GO:0000002"), parameter "ts" of Long,
           parameter "ns" of String, parameter "limit" of Long, parameter
           "offset" of Long
        :returns: instance of type "GenericResults" (Generic results stats -
           Query execution information from ArangoDB. results - array of
           objects of results.) -> structure: parameter "stats" of
           unspecified object, parameter "results" of list of unspecified
           object, parameter "ts" of Long
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_hierarchicalAncestors
        validated_params=self.validate_params(GenericParams);
        results = re_api.query("get_hierarchicalAncestors", validated_params)

        returnVal={"stats": results["stats"], "results": results["results"], "ts": validated_params["ts"]}
        #END get_hierarchicalAncestors

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method get_hierarchicalAncestors return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def get_hierarchicalChildren(self, ctx, GenericParams):
        """
        Retrieve hierarchicalChildren of an ontology term by ID
        :param GenericParams: instance of type "GenericParams" (Generic
           Parameters id - required - ontology term id, such as "GO:0000002"
           ts - optional - fetch documents with this active timestamp,
           defaults to now ns - optional - ontology namespace to use,
           defaults to "go" limit - optional - number of results to return
           (defaults to 20) offset - optional - number of results to skip
           (defaults to 0)) -> structure: parameter "id" of type "ID" (ID :
           ontology term id, such as "GO:0000002"), parameter "ts" of Long,
           parameter "ns" of String, parameter "limit" of Long, parameter
           "offset" of Long
        :returns: instance of type "GenericResults" (Generic results stats -
           Query execution information from ArangoDB. results - array of
           objects of results.) -> structure: parameter "stats" of
           unspecified object, parameter "results" of list of unspecified
           object, parameter "ts" of Long
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_hierarchicalChildren
        validated_params=self.validate_params(GenericParams);
        results = re_api.query("get_hierarchicalChildren", validated_params)

        returnVal={"stats": results["stats"], "results": results["results"], "ts": validated_params["ts"]}
        #END get_hierarchicalChildren

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method get_hierarchicalChildren return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def get_hierarchicalDescendants(self, ctx, GenericParams):
        """
        Retrieve hierarchicalDescendants of an ontology term by ID
        :param GenericParams: instance of type "GenericParams" (Generic
           Parameters id - required - ontology term id, such as "GO:0000002"
           ts - optional - fetch documents with this active timestamp,
           defaults to now ns - optional - ontology namespace to use,
           defaults to "go" limit - optional - number of results to return
           (defaults to 20) offset - optional - number of results to skip
           (defaults to 0)) -> structure: parameter "id" of type "ID" (ID :
           ontology term id, such as "GO:0000002"), parameter "ts" of Long,
           parameter "ns" of String, parameter "limit" of Long, parameter
           "offset" of Long
        :returns: instance of type "GenericResults" (Generic results stats -
           Query execution information from ArangoDB. results - array of
           objects of results.) -> structure: parameter "stats" of
           unspecified object, parameter "results" of list of unspecified
           object, parameter "ts" of Long
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_hierarchicalDescendants
        validated_params=self.validate_params(GenericParams);
        results = re_api.query("get_hierarchicalDescendants", validated_params)

        returnVal={"stats": results["stats"], "results": results["results"], "ts": validated_params["ts"]}
        #END get_hierarchicalDescendants

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method get_hierarchicalDescendants return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def get_hierarchicalParents(self, ctx, GenericParams):
        """
        Retrieve hierarchicalParents of an ontology term by ID
        :param GenericParams: instance of type "GenericParams" (Generic
           Parameters id - required - ontology term id, such as "GO:0000002"
           ts - optional - fetch documents with this active timestamp,
           defaults to now ns - optional - ontology namespace to use,
           defaults to "go" limit - optional - number of results to return
           (defaults to 20) offset - optional - number of results to skip
           (defaults to 0)) -> structure: parameter "id" of type "ID" (ID :
           ontology term id, such as "GO:0000002"), parameter "ts" of Long,
           parameter "ns" of String, parameter "limit" of Long, parameter
           "offset" of Long
        :returns: instance of type "GenericResults" (Generic results stats -
           Query execution information from ArangoDB. results - array of
           objects of results.) -> structure: parameter "stats" of
           unspecified object, parameter "results" of list of unspecified
           object, parameter "ts" of Long
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_hierarchicalParents
        validated_params=self.validate_params(GenericParams);
        results = re_api.query("get_hierarchicalParents", validated_params)

        returnVal={"stats": results["stats"], "results": results["results"], "ts": validated_params["ts"]}
        #END get_hierarchicalParents

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method get_hierarchicalParents return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
