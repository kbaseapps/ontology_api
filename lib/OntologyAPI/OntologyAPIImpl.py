# -*- coding: utf-8 -*-
#BEGIN_HEADER
import logging
import os
import jsonschema

from OntologyAPI.utils import re_api 
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
    GIT_COMMIT_HASH = "0a3ef09a47d278c10b9a02234ec7358ad031392d"

    #BEGIN_CLASS_HEADER
    def validate_params(self, params, schema=None):
        schema = schema or {
            'type': 'object',
            'required': ['key'],
            'properties': {
                'key': {'type': 'string'},
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
           parameter "key" of type "GoID" (GoID : Unique GO term id (Source:
           external Gene Ontology database - http://www.geneontology.org/)),
           parameter "limit" of Long, parameter "offset" of Long
        :returns: instance of type "GoIDList" -> list of type "GoID" (GoID :
           Unique GO term id (Source: external Gene Ontology database -
           http://www.geneontology.org/))
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_descendants
        print('Running get_descendants() with params=')
        pprint(InputParams)
        validated_params=self.validate_params(InputParams);
        results = re_api.query("GO_get_descendants", validated_params)

        returnVal=list(map(lambda x: x["term"]["_key"] ,results["results"]))
        #END get_descendants

        # At some point might do deeper type checking...
        if not isinstance(returnVal, list):
            raise ValueError('Method get_descendants return value ' +
                             'returnVal is not type list as required.')
        # return the results
        return [returnVal]

    def get_ancestors(self, ctx, InputParams):
        """
        :param InputParams: instance of type "InputParams" -> structure:
           parameter "key" of type "GoID" (GoID : Unique GO term id (Source:
           external Gene Ontology database - http://www.geneontology.org/)),
           parameter "limit" of Long, parameter "offset" of Long
        :returns: instance of type "GoIDList" -> list of type "GoID" (GoID :
           Unique GO term id (Source: external Gene Ontology database -
           http://www.geneontology.org/))
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_ancestors
        print('Running get_ancestors() with params=')
        pprint(InputParams)
        validated_params=self.validate_params(InputParams);
        results = re_api.query("GO_get_ancestors", validated_params)

        returnVal=list(map(lambda x: x["term"]["_key"] ,results["results"]))
        #END get_ancestors

        # At some point might do deeper type checking...
        if not isinstance(returnVal, list):
            raise ValueError('Method get_ancestors return value ' +
                             'returnVal is not type list as required.')
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
