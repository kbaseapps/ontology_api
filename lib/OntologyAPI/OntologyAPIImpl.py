# -*- coding: utf-8 -*-
#BEGIN_HEADER
import logging
import os
import jsonschema

from OntologyAPI.utils import re_api, config 
from OntologyAPI.exceptions import InvalidParamsError, REError
from pprint import pprint
from jsonschema.exceptions import ValidationError
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
    GIT_URL = "git@github.com:zhlu9890/ontology_api.git"
    GIT_COMMIT_HASH = "15f72291f43d0ac68ad00714369d81b668c1b74d"

    #BEGIN_CLASS_HEADER
    def validate_params(self, params, schema=None):
        _CONF = config.get_config()
        if 'id' not in params:
            raise InvalidParamsError('Parameter validation error: no id')
        (name_space, key)=params['id'].split('/')
        del params['id']
        params['key']=key
        params['name_space']=name_space
        name_space_list=list(_CONF['name_space'].keys())
        schema = schema or {
            'type': 'object',
            'required': ['key', 'name_space'],
            'properties': {
                'key': {'type': 'string'},
                'name_space': {'type': 'string', 'enum': name_space_list},
                'limit': {'type': 'integer', 'maximum': 1000},
                'offset': {'type': 'integer', 'maximum': 100000},
            }
        }
        try:
            jsonschema.validate(instance=params, schema=schema)
        except ValidationError as err:
            raise InvalidParamsError('Parameter validation error: ' + err.message)
        return params
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.callback_url = os.environ['SDK_CALLBACK_URL']
        self.shared_folder = config['scratch']
        logging.basicConfig(format='%(created)s %(levelname)s: %(message)s',
                            level=logging.INFO)
        #END_CONSTRUCTOR
        pass


    def get_descendants(self, ctx, InputParams):
        """
        Retrieve descendants
        @return descendants
        :param InputParams: instance of type "InputParams" -> structure:
           parameter "id" of type "ID" (ID : name space/ontology term id),
           parameter "limit" of Long, parameter "offset" of Long
        :returns: instance of type "Results" (* Generic results * stats -
           Query execution information from ArangoDB. * results - array of
           objects of results.) -> structure: parameter "stats" of
           unspecified object, parameter "results" of list of unspecified
           object
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_descendants
        print('Running get_descendants() with params=')
        pprint(InputParams)
        validated_params=self.validate_params(InputParams);
        results = re_api.query("get_descendants", validated_params)

        returnVal={"stats": results["stats"], "results": results["results"]}
        #END get_descendants

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method get_descendants return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def get_ancestors(self, ctx, InputParams):
        """
        :param InputParams: instance of type "InputParams" -> structure:
           parameter "id" of type "ID" (ID : name space/ontology term id),
           parameter "limit" of Long, parameter "offset" of Long
        :returns: instance of type "Results" (* Generic results * stats -
           Query execution information from ArangoDB. * results - array of
           objects of results.) -> structure: parameter "stats" of
           unspecified object, parameter "results" of list of unspecified
           object
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_ancestors
        print('Running get_ancestors() with params=')
        pprint(InputParams)
        validated_params=self.validate_params(InputParams);
        results = re_api.query("get_ancestors", validated_params)

        returnVal={"stats": results["stats"], "results": results["results"]}
        #END get_ancestors

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method get_ancestors return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def get_children(self, ctx, InputParams):
        """
        :param InputParams: instance of type "InputParams" -> structure:
           parameter "id" of type "ID" (ID : name space/ontology term id),
           parameter "limit" of Long, parameter "offset" of Long
        :returns: instance of type "Results" (* Generic results * stats -
           Query execution information from ArangoDB. * results - array of
           objects of results.) -> structure: parameter "stats" of
           unspecified object, parameter "results" of list of unspecified
           object
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_children
        print('Running get_children() with params=')
        pprint(InputParams)
        validated_params=self.validate_params(InputParams);
        results = re_api.query("get_children", validated_params)

        returnVal={"stats": results["stats"], "results": results["results"]}
        #END get_children

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method get_children return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def get_parents(self, ctx, InputParams):
        """
        :param InputParams: instance of type "InputParams" -> structure:
           parameter "id" of type "ID" (ID : name space/ontology term id),
           parameter "limit" of Long, parameter "offset" of Long
        :returns: instance of type "Results" (* Generic results * stats -
           Query execution information from ArangoDB. * results - array of
           objects of results.) -> structure: parameter "stats" of
           unspecified object, parameter "results" of list of unspecified
           object
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_parents
        print('Running get_parents() with params=')
        pprint(InputParams)
        validated_params=self.validate_params(InputParams);
        results = re_api.query("get_parents", validated_params)

        returnVal={"stats": results["stats"], "results": results["results"]}
        #END get_parents

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method get_parents return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def get_related(self, ctx, InputParams):
        """
        :param InputParams: instance of type "InputParams" -> structure:
           parameter "id" of type "ID" (ID : name space/ontology term id),
           parameter "limit" of Long, parameter "offset" of Long
        :returns: instance of type "Results" (* Generic results * stats -
           Query execution information from ArangoDB. * results - array of
           objects of results.) -> structure: parameter "stats" of
           unspecified object, parameter "results" of list of unspecified
           object
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_related
        print('Running get_related() with params=')
        pprint(InputParams)
        validated_params=self.validate_params(InputParams);
        results = re_api.query("get_related", validated_params)

        returnVal={"stats": results["stats"], "results": results["results"]}
        #END get_related

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method get_related return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def get_siblings(self, ctx, InputParams):
        """
        :param InputParams: instance of type "InputParams" -> structure:
           parameter "id" of type "ID" (ID : name space/ontology term id),
           parameter "limit" of Long, parameter "offset" of Long
        :returns: instance of type "Results" (* Generic results * stats -
           Query execution information from ArangoDB. * results - array of
           objects of results.) -> structure: parameter "stats" of
           unspecified object, parameter "results" of list of unspecified
           object
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_siblings
        print('Running get_siblings() with params=')
        pprint(InputParams)
        validated_params=self.validate_params(InputParams);
        results = re_api.query("get_siblings", validated_params)

        returnVal={"stats": results["stats"], "results": results["results"]}
        #END get_siblings

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method get_siblings return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def get_metadata(self, ctx, InputParams):
        """
        :param InputParams: instance of type "InputParams" -> structure:
           parameter "id" of type "ID" (ID : name space/ontology term id),
           parameter "limit" of Long, parameter "offset" of Long
        :returns: instance of type "Results" (* Generic results * stats -
           Query execution information from ArangoDB. * results - array of
           objects of results.) -> structure: parameter "stats" of
           unspecified object, parameter "results" of list of unspecified
           object
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_metadata
        print('Running get_metadata() with params=')
        pprint(InputParams)
        validated_params=self.validate_params(InputParams);
        results = re_api.query("get_metadata", validated_params)

        returnVal={"stats": results["stats"], "results": results["results"]}
        #END get_metadata

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method get_metadata return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def get_hierarchicalAncestors(self, ctx, InputParams):
        """
        :param InputParams: instance of type "InputParams" -> structure:
           parameter "id" of type "ID" (ID : name space/ontology term id),
           parameter "limit" of Long, parameter "offset" of Long
        :returns: instance of type "Results" (* Generic results * stats -
           Query execution information from ArangoDB. * results - array of
           objects of results.) -> structure: parameter "stats" of
           unspecified object, parameter "results" of list of unspecified
           object
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_hierarchicalAncestors
        print('Running get_hierarchicalAncestors() with params=')
        pprint(InputParams)
        validated_params=self.validate_params(InputParams);
        results = re_api.query("get_hierarchicalAncestors", validated_params)

        returnVal={"stats": results["stats"], "results": results["results"]}
        #END get_hierarchicalAncestors

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method get_hierarchicalAncestors return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def get_hierarchicalChildren(self, ctx, InputParams):
        """
        :param InputParams: instance of type "InputParams" -> structure:
           parameter "id" of type "ID" (ID : name space/ontology term id),
           parameter "limit" of Long, parameter "offset" of Long
        :returns: instance of type "Results" (* Generic results * stats -
           Query execution information from ArangoDB. * results - array of
           objects of results.) -> structure: parameter "stats" of
           unspecified object, parameter "results" of list of unspecified
           object
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_hierarchicalChildren
        print('Running get_hierarchicalChildren() with params=')
        pprint(InputParams)
        validated_params=self.validate_params(InputParams);
        results = re_api.query("get_hierarchicalChildren", validated_params)

        returnVal={"stats": results["stats"], "results": results["results"]}
        #END get_hierarchicalChildren

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method get_hierarchicalChildren return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def get_hierarchicalDescendants(self, ctx, InputParams):
        """
        :param InputParams: instance of type "InputParams" -> structure:
           parameter "id" of type "ID" (ID : name space/ontology term id),
           parameter "limit" of Long, parameter "offset" of Long
        :returns: instance of type "Results" (* Generic results * stats -
           Query execution information from ArangoDB. * results - array of
           objects of results.) -> structure: parameter "stats" of
           unspecified object, parameter "results" of list of unspecified
           object
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_hierarchicalDescendants
        print('Running get_hierarchicalDescendants() with params=')
        pprint(InputParams)
        validated_params=self.validate_params(InputParams);
        results = re_api.query("get_hierarchicalDescendants", validated_params)

        returnVal={"stats": results["stats"], "results": results["results"]}
        #END get_hierarchicalDescendants

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method get_hierarchicalDescendants return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def get_hierarchicalParents(self, ctx, InputParams):
        """
        :param InputParams: instance of type "InputParams" -> structure:
           parameter "id" of type "ID" (ID : name space/ontology term id),
           parameter "limit" of Long, parameter "offset" of Long
        :returns: instance of type "Results" (* Generic results * stats -
           Query execution information from ArangoDB. * results - array of
           objects of results.) -> structure: parameter "stats" of
           unspecified object, parameter "results" of list of unspecified
           object
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_hierarchicalParents
        print('Running get_hierarchicalParents() with params=')
        pprint(InputParams)
        validated_params=self.validate_params(InputParams);
        results = re_api.query("get_hierarchicalParents", validated_params)

        returnVal={"stats": results["stats"], "results": results["results"]}
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
