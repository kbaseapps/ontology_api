# -*- coding: utf-8 -*-
#BEGIN_HEADER
import logging
import os

from installed_clients.KBaseReportClient import KBaseReport
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
    GIT_COMMIT_HASH = "58bc68de62ca71d1c6b4e52e9275d6742bd86ba7"

    #BEGIN_CLASS_HEADER
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


    def get_descendants(self, ctx, GoID):
        """
        Retrieve descendants
        @return descendants
        :param GoID: instance of type "GoID" (GoID : Unique GO term id
           (Source: external Gene Ontology database -
           http://www.geneontology.org/))
        :returns: instance of type "GoIDList" -> list of type "GoID" (GoID :
           Unique GO term id (Source: external Gene Ontology database -
           http://www.geneontology.org/))
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_descendants
        #END get_descendants

        # At some point might do deeper type checking...
        if not isinstance(returnVal, list):
            raise ValueError('Method get_descendants return value ' +
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
