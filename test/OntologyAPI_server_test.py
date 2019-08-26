# -*- coding: utf-8 -*-
import os
import time
import unittest
from configparser import ConfigParser

from OntologyAPI.OntologyAPIImpl import OntologyAPI
from OntologyAPI.OntologyAPIServer import MethodContext
from OntologyAPI.authclient import KBaseAuth as _KBaseAuth
from OntologyAPI.exceptions import InvalidParamsError, REError
from pprint import pprint

from installed_clients.WorkspaceClient import Workspace


class OntologyAPITest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        token = os.environ.get('KB_AUTH_TOKEN', None)
        config_file = os.environ.get('KB_DEPLOYMENT_CONFIG', None)
        cls.cfg = {}
        config = ConfigParser()
        config.read(config_file)
        for nameval in config.items('OntologyAPI'):
            cls.cfg[nameval[0]] = nameval[1]
        # Getting username from Auth profile for token
        authServiceUrl = cls.cfg['auth-service-url']
        auth_client = _KBaseAuth(authServiceUrl)
        user_id = auth_client.get_user(token)
        # WARNING: don't call any logging methods on the context object,
        # it'll result in a NoneType error
        cls.ctx = MethodContext(None)
        cls.ctx.update({'token': token,
                        'user_id': user_id,
                        'provenance': [
                            {'service': 'OntologyAPI',
                             'method': 'please_never_use_it_in_production',
                             'method_params': []
                             }],
                        'authenticated': 1})
        cls.wsURL = cls.cfg['workspace-url']
        cls.wsClient = Workspace(cls.wsURL)
        cls.serviceImpl = OntologyAPI(cls.cfg)
        cls.scratch = cls.cfg['scratch']
        cls.callback_url = os.environ['SDK_CALLBACK_URL']
        suffix = int(time.time() * 1000)
        cls.wsName = "test_ContigFilter_" + str(suffix)
        ret = cls.wsClient.create_workspace({'workspace': cls.wsName})  # noqa

    @classmethod
    def tearDownClass(cls):
        if hasattr(cls, 'wsName'):
            cls.wsClient.delete_workspace({'workspace': cls.wsName})
            print('Test workspace was deleted')

    # NOTE: According to Python unittest naming rules test method names should start from 'test'. # noqa
    def test_get_descendants(self):
        ret = self.serviceImpl.get_descendants(self.ctx, {"id": "go_ontology/GO:0000002"})
        returnVal=list(map(lambda x: x["term"]["_key"], ret[0]["results"]))
        self.assertEqual(returnVal, ["GO:0033955"])
        with self.assertRaises(InvalidParamsError):
            self.serviceImpl.get_descendants(self.ctx, {"key": "go_ontology/GO:0000002"})
        with self.assertRaises(InvalidParamsError):
            self.serviceImpl.get_descendants(self.ctx, {"id": "go_ontology\GO:0000002"})

    def test_get_ancestors(self):
        ret = self.serviceImpl.get_ancestors(self.ctx, {"id": "go_ontology/GO:0000002"})
        returnVal=list(map(lambda x: x["term"]["_key"], ret[0]["results"]))
        self.assertEqual(returnVal, ['GO:0006996', 'GO:0007005', 'GO:0008150','GO:0008150','GO:0009987', 'GO:0016043', 'GO:0071840'])

    def test_get_children(self):
        ret = self.serviceImpl.get_children(self.ctx, {"id": "go_ontology/GO:0000002"})
        returnVal=list(map(lambda x: x["term"]["_key"], ret[0]["results"]))
        self.assertEqual(returnVal, ['GO:0033955'])

    def test_get_parents(self):
        ret = self.serviceImpl.get_parents(self.ctx, {"id": "go_ontology/GO:0000002"})
        returnVal=list(map(lambda x: x["term"]["_key"], ret[0]["results"]))
        self.assertEqual(returnVal, ['GO:0007005'])

    def test_get_related(self):
        ret = self.serviceImpl.get_related(self.ctx, {"id": "go_ontology/GO:0000002"})
        returnVal=list(map(lambda x: x["term"]["_key"], ret[0]["results"]))
        self.assertEqual(returnVal, ['GO:0007005', 'GO:0032042', 'GO:0033955'])

    def test_get_siblings(self):
        ret = self.serviceImpl.get_siblings(self.ctx, {"id": "go_ontology/GO:0000002"})
        returnVal=list(map(lambda x: x, ret[0]["results"]))
        self.assertEqual(returnVal, ["GO:0000266", "GO:0007006", "GO:0007287", "GO:0008053", "GO:0008637", "GO:0030382", "GO:0048311", "GO:0061726", "GO:0070584", "GO:0097250"])

    def test_get_metadata(self):
        ret = self.serviceImpl.get_metadata(self.ctx, {"id": "go_ontology/GO:0000002"})
        returnVal=list(map(lambda x: x["_key"], ret[0]["results"]))
        self.assertEqual(returnVal, ['GO:0000002'])

    def test_get_hierarchicalAncestors(self):
        ret = self.serviceImpl.get_hierarchicalAncestors(self.ctx, {"id": "go_ontology/GO:0000002"})
        returnVal=list(map(lambda x: x["term"]["_key"], ret[0]["results"]))
        self.assertEqual(returnVal, ['GO:0007005', 'GO:0006996', 'GO:0016043', 'GO:0009987', 'GO:0008150', 'GO:0071840', 'GO:0008150'])

    def test_get_hierarchicalChildren(self):
        ret = self.serviceImpl.get_hierarchicalChildren(self.ctx, {"id": "go_ontology/GO:0000002"})
        returnVal=list(map(lambda x: x["term"]["_key"], ret[0]["results"]))
        self.assertEqual(returnVal, ['GO:0032042', 'GO:0033955'])

    def test_get_hierarchicalDescendants(self):
        ret = self.serviceImpl.get_hierarchicalDescendants(self.ctx, {"id": "go_ontology/GO:0000002"})
        returnVal=list(map(lambda x: x["term"]["_key"], ret[0]["results"]))
        self.assertEqual(returnVal, ['GO:0032042', 'GO:0033955'])

    def test_get_hierarchicalParents(self):
        ret = self.serviceImpl.get_hierarchicalParents(self.ctx, {"id": "go_ontology/GO:0000002"})
        returnVal=list(map(lambda x: x["term"]["_key"], ret[0]["results"]))
        self.assertEqual(returnVal, ['GO:0007005'])
