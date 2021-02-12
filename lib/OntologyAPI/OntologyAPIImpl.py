# -*- coding: utf-8 -*-
#BEGIN_HEADER
import logging
import re

from OntologyAPI.utils import re_api, misc, namespace
from installed_clients.authclient import KBaseAuth
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
    VERSION = "0.3.11"
    GIT_URL = ""
    GIT_COMMIT_HASH = "92a2aaf04d69eff45c9a9ff26afdd17e1fb962a0"

    #BEGIN_CLASS_HEADER
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
           Parameters id - required - ontology term id, such as "GO:0016209"
           ts - optional - fetch documents with this active timestamp,
           defaults to now ns - optional - ontology namespace to use,
           defaults to "go" limit - optional - number of results to return
           (defaults to 20) offset - optional - number of results to skip
           (defaults to 0)) -> structure: parameter "id" of type "ID"
           (Ontology term id, such as "GO:0000002"), parameter "ts" of Long,
           parameter "ns" of String, parameter "limit" of Long, parameter
           "offset" of Long
        :returns: instance of type "GenericResults" (Generic results stats -
           Query execution information from ArangoDB. results - array of
           objects of results. ts - Timestamp used in the request ns -
           Ontology namespace used in the request.) -> structure: parameter
           "stats" of unspecified object, parameter "results" of list of
           unspecified object, parameter "ts" of Long, parameter "ns" of
           String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_descendants
        validated_params=misc.validate_params(GenericParams)
        results = re_api.query("get_descendants", validated_params)

        returnVal={"stats": results["stats"], "ts": validated_params["ts"], "ns": validated_params["ns"]}
        if results.get('error'):
            returnVal["results"]=[]
            returnVal["error"]=results.get('error')
        else:
            returnVal["results"]=results["results"]
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
           Parameters id - required - ontology term id, such as "GO:0016209"
           ts - optional - fetch documents with this active timestamp,
           defaults to now ns - optional - ontology namespace to use,
           defaults to "go" limit - optional - number of results to return
           (defaults to 20) offset - optional - number of results to skip
           (defaults to 0)) -> structure: parameter "id" of type "ID"
           (Ontology term id, such as "GO:0000002"), parameter "ts" of Long,
           parameter "ns" of String, parameter "limit" of Long, parameter
           "offset" of Long
        :returns: instance of type "GenericResults" (Generic results stats -
           Query execution information from ArangoDB. results - array of
           objects of results. ts - Timestamp used in the request ns -
           Ontology namespace used in the request.) -> structure: parameter
           "stats" of unspecified object, parameter "results" of list of
           unspecified object, parameter "ts" of Long, parameter "ns" of
           String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_ancestors
        validated_params=misc.validate_params(GenericParams)
        results = re_api.query("get_ancestors", validated_params)

        returnVal={"stats": results["stats"], "ts": validated_params["ts"], "ns": validated_params["ns"]}
        if results.get('error'):
            returnVal["results"]=[]
            returnVal["error"]=results.get('error')
        else:
            returnVal["results"]=results["results"]
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
           Parameters id - required - ontology term id, such as "GO:0016209"
           ts - optional - fetch documents with this active timestamp,
           defaults to now ns - optional - ontology namespace to use,
           defaults to "go" limit - optional - number of results to return
           (defaults to 20) offset - optional - number of results to skip
           (defaults to 0)) -> structure: parameter "id" of type "ID"
           (Ontology term id, such as "GO:0000002"), parameter "ts" of Long,
           parameter "ns" of String, parameter "limit" of Long, parameter
           "offset" of Long
        :returns: instance of type "GenericResults" (Generic results stats -
           Query execution information from ArangoDB. results - array of
           objects of results. ts - Timestamp used in the request ns -
           Ontology namespace used in the request.) -> structure: parameter
           "stats" of unspecified object, parameter "results" of list of
           unspecified object, parameter "ts" of Long, parameter "ns" of
           String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_children
        validated_params=misc.validate_params(GenericParams)
        results = re_api.query("get_children", validated_params)

        returnVal={"stats": results["stats"], "ts": validated_params["ts"], "ns": validated_params["ns"]}
        if results.get('error'):
            returnVal["results"]=[]
            returnVal["error"]=results.get('error')
        else:
            returnVal["results"]=results["results"]
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
           Parameters id - required - ontology term id, such as "GO:0016209"
           ts - optional - fetch documents with this active timestamp,
           defaults to now ns - optional - ontology namespace to use,
           defaults to "go" limit - optional - number of results to return
           (defaults to 20) offset - optional - number of results to skip
           (defaults to 0)) -> structure: parameter "id" of type "ID"
           (Ontology term id, such as "GO:0000002"), parameter "ts" of Long,
           parameter "ns" of String, parameter "limit" of Long, parameter
           "offset" of Long
        :returns: instance of type "GenericResults" (Generic results stats -
           Query execution information from ArangoDB. results - array of
           objects of results. ts - Timestamp used in the request ns -
           Ontology namespace used in the request.) -> structure: parameter
           "stats" of unspecified object, parameter "results" of list of
           unspecified object, parameter "ts" of Long, parameter "ns" of
           String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_parents
        validated_params=misc.validate_params(GenericParams)
        results = re_api.query("get_parents", validated_params)

        returnVal={"stats": results["stats"], "ts": validated_params["ts"], "ns": validated_params["ns"]}
        if results.get('error'):
            returnVal["results"]=[]
            returnVal["error"]=results.get('error')
        else:
            returnVal["results"]=results["results"]
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
           Parameters id - required - ontology term id, such as "GO:0016209"
           ts - optional - fetch documents with this active timestamp,
           defaults to now ns - optional - ontology namespace to use,
           defaults to "go" limit - optional - number of results to return
           (defaults to 20) offset - optional - number of results to skip
           (defaults to 0)) -> structure: parameter "id" of type "ID"
           (Ontology term id, such as "GO:0000002"), parameter "ts" of Long,
           parameter "ns" of String, parameter "limit" of Long, parameter
           "offset" of Long
        :returns: instance of type "GenericResults" (Generic results stats -
           Query execution information from ArangoDB. results - array of
           objects of results. ts - Timestamp used in the request ns -
           Ontology namespace used in the request.) -> structure: parameter
           "stats" of unspecified object, parameter "results" of list of
           unspecified object, parameter "ts" of Long, parameter "ns" of
           String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_related
        validated_params=misc.validate_params(GenericParams)
        results = re_api.query("get_related", validated_params)

        returnVal={"stats": results["stats"], "ts": validated_params["ts"], "ns": validated_params["ns"]}
        if results.get('error'):
            returnVal["results"]=[]
            returnVal["error"]=results.get('error')
        else:
            returnVal["results"]=results["results"]
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
           Parameters id - required - ontology term id, such as "GO:0016209"
           ts - optional - fetch documents with this active timestamp,
           defaults to now ns - optional - ontology namespace to use,
           defaults to "go" limit - optional - number of results to return
           (defaults to 20) offset - optional - number of results to skip
           (defaults to 0)) -> structure: parameter "id" of type "ID"
           (Ontology term id, such as "GO:0000002"), parameter "ts" of Long,
           parameter "ns" of String, parameter "limit" of Long, parameter
           "offset" of Long
        :returns: instance of type "GenericResults" (Generic results stats -
           Query execution information from ArangoDB. results - array of
           objects of results. ts - Timestamp used in the request ns -
           Ontology namespace used in the request.) -> structure: parameter
           "stats" of unspecified object, parameter "results" of list of
           unspecified object, parameter "ts" of Long, parameter "ns" of
           String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_siblings
        validated_params=misc.validate_params(GenericParams)
        results = re_api.query("get_siblings", validated_params)

        returnVal={"stats": results["stats"], "ts": validated_params["ts"], "ns": validated_params["ns"]}
        if results.get('error'):
            returnVal["results"]=[]
            returnVal["error"]=results.get('error')
        else:
            returnVal["results"]=results["results"]
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
           optional - ontology namespace to use, defaults to "go" limit -
           optional - number of results to return (defaults to 20) offset -
           optional - number of results to skip (defaults to 0)) ->
           structure: parameter "ids" of list of type "ID" (Ontology term id,
           such as "GO:0000002"), parameter "ts" of Long, parameter "ns" of
           String, parameter "limit" of Long, parameter "offset" of Long
        :returns: instance of type "GenericResults" (Generic results stats -
           Query execution information from ArangoDB. results - array of
           objects of results. ts - Timestamp used in the request ns -
           Ontology namespace used in the request.) -> structure: parameter
           "stats" of unspecified object, parameter "results" of list of
           unspecified object, parameter "ts" of Long, parameter "ns" of
           String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_terms
        validated_params=misc.validate_params(GetTermsParams, "get_terms")
        results = re_api.query("get_terms", validated_params)

        returnVal={"stats": results["stats"], "ts": validated_params["ts"], "ns": validated_params["ns"]}
        if results.get('error'):
            returnVal["results"]=[]
            returnVal["error"]=results.get('error')
        else:
            returnVal["results"]=results["results"]
        #END get_terms

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method get_terms return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def get_hierarchical_ancestors(self, ctx, GenericParams):
        """
        Retrieve hierarchical_ancestors of an ontology term by ID
        :param GenericParams: instance of type "GenericParams" (Generic
           Parameters id - required - ontology term id, such as "GO:0016209"
           ts - optional - fetch documents with this active timestamp,
           defaults to now ns - optional - ontology namespace to use,
           defaults to "go" limit - optional - number of results to return
           (defaults to 20) offset - optional - number of results to skip
           (defaults to 0)) -> structure: parameter "id" of type "ID"
           (Ontology term id, such as "GO:0000002"), parameter "ts" of Long,
           parameter "ns" of String, parameter "limit" of Long, parameter
           "offset" of Long
        :returns: instance of type "GenericResults" (Generic results stats -
           Query execution information from ArangoDB. results - array of
           objects of results. ts - Timestamp used in the request ns -
           Ontology namespace used in the request.) -> structure: parameter
           "stats" of unspecified object, parameter "results" of list of
           unspecified object, parameter "ts" of Long, parameter "ns" of
           String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_hierarchical_ancestors
        validated_params=misc.validate_params(GenericParams)
        results = re_api.query("get_hierarchicalAncestors", validated_params)

        returnVal={"stats": results["stats"], "ts": validated_params["ts"], "ns": validated_params["ns"]}
        if results.get('error'):
            returnVal["results"]=[]
            returnVal["error"]=results.get('error')
        else:
            returnVal["results"]=results["results"]
        #END get_hierarchical_ancestors

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method get_hierarchical_ancestors return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def get_hierarchical_children(self, ctx, GenericParams):
        """
        Retrieve hierarchical_children of an ontology term by ID
        :param GenericParams: instance of type "GenericParams" (Generic
           Parameters id - required - ontology term id, such as "GO:0016209"
           ts - optional - fetch documents with this active timestamp,
           defaults to now ns - optional - ontology namespace to use,
           defaults to "go" limit - optional - number of results to return
           (defaults to 20) offset - optional - number of results to skip
           (defaults to 0)) -> structure: parameter "id" of type "ID"
           (Ontology term id, such as "GO:0000002"), parameter "ts" of Long,
           parameter "ns" of String, parameter "limit" of Long, parameter
           "offset" of Long
        :returns: instance of type "GenericResults" (Generic results stats -
           Query execution information from ArangoDB. results - array of
           objects of results. ts - Timestamp used in the request ns -
           Ontology namespace used in the request.) -> structure: parameter
           "stats" of unspecified object, parameter "results" of list of
           unspecified object, parameter "ts" of Long, parameter "ns" of
           String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_hierarchical_children
        validated_params=misc.validate_params(GenericParams)
        results = re_api.query("get_hierarchicalChildren", validated_params)

        returnVal={"stats": results["stats"], "ts": validated_params["ts"], "ns": validated_params["ns"]}
        if results.get('error'):
            returnVal["results"]=[]
            returnVal["error"]=results.get('error')
        else:
            returnVal["results"]=results["results"]
        #END get_hierarchical_children

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method get_hierarchical_children return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def get_hierarchical_descendants(self, ctx, GenericParams):
        """
        Retrieve hierarchical_descendants of an ontology term by ID
        :param GenericParams: instance of type "GenericParams" (Generic
           Parameters id - required - ontology term id, such as "GO:0016209"
           ts - optional - fetch documents with this active timestamp,
           defaults to now ns - optional - ontology namespace to use,
           defaults to "go" limit - optional - number of results to return
           (defaults to 20) offset - optional - number of results to skip
           (defaults to 0)) -> structure: parameter "id" of type "ID"
           (Ontology term id, such as "GO:0000002"), parameter "ts" of Long,
           parameter "ns" of String, parameter "limit" of Long, parameter
           "offset" of Long
        :returns: instance of type "GenericResults" (Generic results stats -
           Query execution information from ArangoDB. results - array of
           objects of results. ts - Timestamp used in the request ns -
           Ontology namespace used in the request.) -> structure: parameter
           "stats" of unspecified object, parameter "results" of list of
           unspecified object, parameter "ts" of Long, parameter "ns" of
           String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_hierarchical_descendants
        validated_params=misc.validate_params(GenericParams)
        results = re_api.query("get_hierarchicalDescendants", validated_params)

        returnVal={"stats": results["stats"], "ts": validated_params["ts"], "ns": validated_params["ns"]}
        if results.get('error'):
            returnVal["results"]=[]
            returnVal["error"]=results.get('error')
        else:
            returnVal["results"]=results["results"]
        #END get_hierarchical_descendants

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method get_hierarchical_descendants return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def get_hierarchical_parents(self, ctx, GenericParams):
        """
        Retrieve hierarchical_parents of an ontology term by ID
        :param GenericParams: instance of type "GenericParams" (Generic
           Parameters id - required - ontology term id, such as "GO:0016209"
           ts - optional - fetch documents with this active timestamp,
           defaults to now ns - optional - ontology namespace to use,
           defaults to "go" limit - optional - number of results to return
           (defaults to 20) offset - optional - number of results to skip
           (defaults to 0)) -> structure: parameter "id" of type "ID"
           (Ontology term id, such as "GO:0000002"), parameter "ts" of Long,
           parameter "ns" of String, parameter "limit" of Long, parameter
           "offset" of Long
        :returns: instance of type "GenericResults" (Generic results stats -
           Query execution information from ArangoDB. results - array of
           objects of results. ts - Timestamp used in the request ns -
           Ontology namespace used in the request.) -> structure: parameter
           "stats" of unspecified object, parameter "results" of list of
           unspecified object, parameter "ts" of Long, parameter "ns" of
           String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_hierarchical_parents
        validated_params=misc.validate_params(GenericParams)
        results = re_api.query("get_hierarchicalParents", validated_params)

        returnVal={"stats": results["stats"], "ts": validated_params["ts"], "ns": validated_params["ns"]}
        if results.get('error'):
            returnVal["results"]=[]
            returnVal["error"]=results.get('error')
        else:
            returnVal["results"]=results["results"]
        #END get_hierarchical_parents

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method get_hierarchical_parents return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def get_associated_ws_genomes(self, ctx, GenericParams):
        """
        Retrieve associated workspace genome objects of an ontology term by ID
        :param GenericParams: instance of type "GenericParams" (Generic
           Parameters id - required - ontology term id, such as "GO:0016209"
           ts - optional - fetch documents with this active timestamp,
           defaults to now ns - optional - ontology namespace to use,
           defaults to "go" limit - optional - number of results to return
           (defaults to 20) offset - optional - number of results to skip
           (defaults to 0)) -> structure: parameter "id" of type "ID"
           (Ontology term id, such as "GO:0000002"), parameter "ts" of Long,
           parameter "ns" of String, parameter "limit" of Long, parameter
           "offset" of Long
        :returns: instance of type "GetAssociatedWSObjectsResults" (Results
           from get_associated_ws_objects stats - Query execution information
           from ArangoDB. results - array of WSObjectsResults objects. ts -
           Timestamp used in the request ns - Ontology namespace used in the
           request. total_count - total count of associated workspace
           objects) -> structure: parameter "stats" of unspecified object,
           parameter "results" of list of type "WSObjectsWithFeatureCount"
           (Workspace obj with count of associated workspace genome features
           feature_count - count of features associated. ws_obj - WSObj
           object) -> structure: parameter "feature_count" of Long, parameter
           "ws_obj" of type "WSObj" (workspace object) -> structure:
           parameter "workspace_id" of Long, parameter "object_id" of Long,
           parameter "version" of Long, parameter "name" of String, parameter
           "ts" of Long, parameter "ns" of String, parameter "total_count" of
           Long
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_associated_ws_genomes
        validated_params=misc.validate_params(GenericParams)
        results = re_api.query("get_associated_ws_genomes", validated_params)

        returnVal={"stats": results["stats"], "ts": validated_params["ts"], "ns": validated_params["ns"]}
        if results.get('error'):
            returnVal["results"]=[]
            returnVal["total_count"]=0
            returnVal["error"]=results.get('error')
        else:
            returnVal["results"]=results["results"][0]["results"]
            returnVal["total_count"]=results["results"][0]["total_count"]
        #END get_associated_ws_genomes

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method get_associated_ws_genomes return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def get_associated_ws_features(self, ctx, GetAssociatedWSFeaturesParams):
        """
        Retrieve associated workspace genome features of an ontology term by ID and workspace obj_ref
        :param GetAssociatedWSFeaturesParams: instance of type
           "GetAssociatedWSFeaturesParams" (Parameters for
           get_terms_from_ws_feature id - required - ontology term id, such
           as "GO:0016209" obj_ref - optional - workspace object ref, such as
           "6976/926/2" ts - optional - fetch documents with this active
           timestamp, defaults to now ns - optional - ontology namespace to
           use, defaults to "go" limit - optional - number of results to
           return (defaults to 20) offset - optional - number of results to
           skip (defaults to 0)) -> structure: parameter "id" of type "ID"
           (Ontology term id, such as "GO:0000002"), parameter "obj_ref" of
           String, parameter "ns" of String, parameter "ts" of Long,
           parameter "limit" of Long, parameter "offset" of Long
        :returns: instance of type "GetAssociatedWSFeaturesResults" (Results
           from get_associated_ws_features stats - Query execution
           information from ArangoDB. results - array of WSObjectsResults
           objects. ts - Timestamp used in the request ns - Ontology
           namespace used in the request. total_count - total count of
           associated workspace features) -> structure: parameter "stats" of
           unspecified object, parameter "results" of list of type
           "WSObjWithWSFeatures" (Workspace obj with associated workspace
           genome features ws_obj - WSObj object features - a list of
           FeatureLite object) -> structure: parameter "ws_obj" of type
           "WSObj" (workspace object) -> structure: parameter "workspace_id"
           of Long, parameter "object_id" of Long, parameter "version" of
           Long, parameter "name" of String, parameter "features" of list of
           type "FeatureLite" (workspace genome feature, lite version) ->
           structure: parameter "feature_id" of String, parameter
           "updated_at" of Long, parameter "ts" of Long, parameter "ns" of
           String, parameter "total_count" of Long
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_associated_ws_features
        validated_params=misc.validate_params(GetAssociatedWSFeaturesParams, "get_associated_ws_features")
        validated_params['obj_ref']=re.sub('/', ':', validated_params['obj_ref'])
        results = re_api.query("get_associated_ws_features", validated_params)

        returnVal={"stats": results["stats"], "ts": validated_params["ts"], "ns": validated_params["ns"]}
        if results.get('error'):
            returnVal["results"]=[]
            returnVal["total_count"]=0
            returnVal["error"]=results.get('error')
        else:
            returnVal["results"]=results["results"][0]["results"]
            returnVal["total_count"]=results["results"][0]["total_count"]
        #END get_associated_ws_features

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method get_associated_ws_features return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def get_terms_from_ws_feature(self, ctx, GetTermsFromWSFeatureParams):
        """
        Retrieve ontology terms of an workspace genome feature by workspace obj_ref and feature id
        :param GetTermsFromWSFeatureParams: instance of type
           "GetTermsFromWSFeatureParams" (Parameters for
           get_terms_from_ws_feature obj_ref - required - workspace object
           ref, such as "6976/926/2" feature_id - required - workspace
           feature id, such as "b3908" ts - optional - fetch documents with
           this active timestamp, defaults to now ns - optional - ontology
           namespace to use, defaults to "go" limit - optional - number of
           results to return (defaults to 20) offset - optional - number of
           results to skip (defaults to 0)) -> structure: parameter "obj_ref"
           of String, parameter "feature_id" of String, parameter "ns" of
           String, parameter "ts" of Long, parameter "limit" of Long,
           parameter "offset" of Long
        :returns: instance of type "GetTermsFromWSFeatureResults" (Results
           from get_terms_from_ws_feature stats - Query execution information
           from ArangoDB. results - array of TermsWithWSFeature objects. ts -
           Timestamp used in the request ns - Ontology namespace used in the
           request.) -> structure: parameter "stats" of unspecified object,
           parameter "results" of list of type "TermsWithWSFeature" (Ontology
           terms with associated workspace genome feature terms - a list of
           Term object feature - Feature object) -> structure: parameter
           "terms" of list of type "Term" (Ontology term) -> structure:
           parameter "id" of type "ID" (Ontology term id, such as
           "GO:0000002"), parameter "name" of String, parameter "namespace"
           of String, parameter "alt_ids" of list of String, parameter "def"
           of unspecified object, parameter "comments" of list of String,
           parameter "synonyms" of list of unspecified object, parameter
           "xrefs" of list of unspecified object, parameter "created" of
           Long, parameter "expired" of Long, parameter "feature" of type
           "Feature" (workspace genome feature) -> structure: parameter
           "feature_id" of String, parameter "updated_at" of Long, parameter
           "workspace_id" of Long, parameter "object_id" of Long, parameter
           "version" of Long, parameter "ts" of Long, parameter "ns" of String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_terms_from_ws_feature
        validated_params=misc.validate_params(GetTermsFromWSFeatureParams, "get_terms_from_ws_feature")
        validated_params['obj_ref']=re.sub('/', ':', validated_params['obj_ref'])
        validated_params['feature_id']=validated_params['obj_ref'] + '_' + validated_params['feature_id']
        del validated_params['obj_ref']

        results = re_api.query("get_terms_from_ws_feature", validated_params)

        returnVal={"stats": results["stats"], "ts": validated_params["ts"], "ns": validated_params["ns"]}
        if results.get('error'):
            returnVal["results"]=[]
            returnVal["error"]=results.get('error')
        else:
            returnVal["results"]=results["results"]
        #END get_terms_from_ws_feature

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method get_terms_from_ws_feature return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def get_terms_from_ws_object(self, ctx, GetTermsFromWSObjParams):
        """
        Retrieve ontology terms of an workspace object by workspace obj_ref
        :param GetTermsFromWSObjParams: instance of type
           "GetTermsFromWSObjParams" (Parameters for get_terms_from_ws_object
           obj_ref - required - workspace object ref, such as "6976/926/2" ts
           - optional - fetch documents with this active timestamp, defaults
           to now ns - optional - ontology namespace to use, defaults to "go"
           limit - optional - number of results to return (defaults to 20)
           offset - optional - number of results to skip (defaults to 0)) ->
           structure: parameter "obj_ref" of String, parameter "ns" of
           String, parameter "ts" of Long, parameter "limit" of Long,
           parameter "offset" of Long
        :returns: instance of type "GetTermsFromWSObjResults" (Results from
           get_terms_from_ws_obj stats - Query execution information from
           ArangoDB. results - array of TermsWithWSFeature objects. ts -
           Timestamp used in the request ns - Ontology namespace used in the
           request.) -> structure: parameter "stats" of unspecified object,
           parameter "results" of list of type "TermsWithWSFeature" (Ontology
           terms with associated workspace genome feature terms - a list of
           Term object feature - Feature object) -> structure: parameter
           "terms" of list of type "Term" (Ontology term) -> structure:
           parameter "id" of type "ID" (Ontology term id, such as
           "GO:0000002"), parameter "name" of String, parameter "namespace"
           of String, parameter "alt_ids" of list of String, parameter "def"
           of unspecified object, parameter "comments" of list of String,
           parameter "synonyms" of list of unspecified object, parameter
           "xrefs" of list of unspecified object, parameter "created" of
           Long, parameter "expired" of Long, parameter "feature" of type
           "Feature" (workspace genome feature) -> structure: parameter
           "feature_id" of String, parameter "updated_at" of Long, parameter
           "workspace_id" of Long, parameter "object_id" of Long, parameter
           "version" of Long, parameter "ts" of Long, parameter "ns" of String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_terms_from_ws_object
        validated_params=misc.validate_params(GetTermsFromWSObjParams, "get_terms_from_ws_object")
        validated_params['obj_ref']=re.sub('/', ':', validated_params['obj_ref'])
        results = re_api.query("get_terms_from_ws_object", validated_params)

        returnVal={"stats": results["stats"], "ts": validated_params["ts"], "ns": validated_params["ns"]}
        if results.get('error'):
            returnVal["results"]=[]
            returnVal["error"]=results.get('error')
        else:
            returnVal["results"]=results["results"]
        #END get_terms_from_ws_object

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method get_terms_from_ws_object return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def get_associated_samples(self, ctx, GenericParams):
        """
        Retrieve associated samples of an ontology term by ID
        :param GenericParams: instance of type "GenericParams" (Generic
           Parameters id - required - ontology term id, such as "GO:0016209"
           ts - optional - fetch documents with this active timestamp,
           defaults to now ns - optional - ontology namespace to use,
           defaults to "go" limit - optional - number of results to return
           (defaults to 20) offset - optional - number of results to skip
           (defaults to 0)) -> structure: parameter "id" of type "ID"
           (Ontology term id, such as "GO:0000002"), parameter "ts" of Long,
           parameter "ns" of String, parameter "limit" of Long, parameter
           "offset" of Long
        :returns: instance of type "GetAssociatedSamplesResults" (Results
           from get_associated_samples stats - Query execution information
           from ArangoDB. results - array of SampleWithMetadataKey objects.
           ts - Timestamp used in the request ns - Ontology namespace used in
           the request. total_count - total count of associated samples) ->
           structure: parameter "stats" of unspecified object, parameter
           "results" of list of type "SampleWithMetadataKey" (Sample data
           with sample_metadata_key id - sample id name - sample name
           node_tree - sample metadata save_date - sample data saved date
           version - sample data version sample_metadata_key - metadata key
           referencing ontology term) -> structure: parameter "id" of String,
           parameter "name" of String, parameter "node_tree" of unspecified
           object, parameter "save_date" of Long, parameter "version" of
           Long, parameter "sample_metadata_key" of String, parameter "ts" of
           Long, parameter "ns" of String, parameter "total_count" of Long
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_associated_samples
        user_id=ctx.get('user_id')
        validated_params=misc.validate_params(GenericParams, 'get_associated_samples')
        results = re_api.query("get_associated_samples", validated_params)

        returnVal={"stats": results["stats"], "ts": validated_params["ts"], "ns": validated_params["ns"]}
        if results.get('error'):
            returnVal["results"]=[]
            returnVal["total_count"]=0
            returnVal["error"]=results.get('error')
        else:
            returnVal["total_count"]=results["results"][0]["total_count"]
            returnVal["results"]=[]
            for x in results["results"][0]["results"]:
                _sample_access=x.get("sample_access")
                _sample_metadata_key=x.get("sample_metadata_key")
                _sample=x.get("sample")
                if None in [_sample, _sample_metadata_key, _sample_access]:
                    continue
                if not _sample_access["acls"]["pubread"] \
                    and user_id != _sample_access["acls"]["owner"] \
                    and user_id not in _sample_access["acls"]["admin"] \
                    and user_id not in _sample_access["acls"]["read"]:
                    continue
                sample={"id": _sample["id"], "save_date": int(_sample["saved"] * 1000), 
                    "version": _sample["ver"], "user": _sample_access["acls"]["owner"]}
                node_tree={"id": _sample["name"], "type": _sample["type"], "parent": _sample["parent"]}
                meta_controlled={}
                for m in _sample.get("cmeta", []):
                    if m["ok"] not in meta_controlled:
                        meta_controlled[m["ok"]]={}
                    meta_controlled[m["ok"]][m["k"]]=m["v"]
                sample_name=meta_controlled.get("name")
                sample["name"]=sample_name["value"] if sample_name is not None else None
                node_tree["meta_controlled"]=meta_controlled
                meta_user={}
                for m in _sample.get("ucmeta", []):
                    if m["ok"] not in meta_user:
                        meta_user[m["ok"]]={}
                    meta_user[m["ok"]][m["k"]]=m["v"]
                node_tree["meta_user"]=meta_user
                source_meta={}
                for m in _sample.get("smeta", []):
                    source_meta["key"]=m["k"]
                    source_meta["skey"]=m["sk"]
                    source_meta["svalue"]=m["v"]
                node_tree["source_meta"]=source_meta
                sample["node_tree"]=[node_tree]
                returnVal["results"].append({"sample": sample, "sample_metadata_key": _sample_metadata_key})
        #END get_associated_samples

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method get_associated_samples return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def get_namespaces(self, ctx):
        """
        :returns: instance of type "GetNamespacesResults" -> structure:
           parameter "namespaces" of unspecified object
        """
        # ctx is the context object
        # return variables are: results
        #BEGIN get_namespaces
        # function for retrieving current iteration of namespace.yaml file
        # make sure request is made by an admin
        namespaces = namespace.load_namespaces()
        results = {'namespaces': namespaces}
        #END get_namespaces

        # At some point might do deeper type checking...
        if not isinstance(results, dict):
            raise ValueError('Method get_namespaces return value ' +
                             'results is not type dict as required.')
        # return the results
        return [results]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
