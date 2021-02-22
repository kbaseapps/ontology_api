# -*- coding: utf-8 -*-
import os
import time
import unittest
from configparser import ConfigParser

from OntologyAPI.OntologyAPIImpl import OntologyAPI
from OntologyAPI.OntologyAPIServer import MethodContext
from OntologyAPI.authclient import KBaseAuth as _KBaseAuth
from OntologyAPI.exceptions import InvalidParamsError, REError
from OntologyAPI.utils import namespace
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
        #cls.callback_url = os.environ['SDK_CALLBACK_URL']
        suffix = int(time.time() * 1000)
        cls.wsName = "test_OntologyAPI_" + str(suffix)
        ret = cls.wsClient.create_workspace({'workspace': cls.wsName})  # noqa

    @classmethod
    def tearDownClass(cls):
        if hasattr(cls, 'wsName'):
            cls.wsClient.delete_workspace({'workspace': cls.wsName})
            print('Test workspace was deleted')

    # NOTE: According to Python unittest naming rules test method names should start from 'test'. # noqa

    def test_get_namespaces(self):
        ret = self.serviceImpl.get_namespaces(self.ctx)
        fn_namespaces = ret[0]['namespaces']
        loaded_namespaces = namespace.load_namespaces()
        self.assertEqual(fn_namespaces, loaded_namespaces)

    def test_go_status(self):
      ret = self.serviceImpl.status(self.ctx)
      returnVal=ret[0]["state"]
      self.assertEqual(returnVal, "OK")

    def test_go_get_descendants(self):
        ret = self.serviceImpl.get_descendants(self.ctx, {"id": "GO:0000002"})
        returnVal=list(map(lambda x: x["term"]["id"], ret[0]["results"]))
        self.assertTrue(set(["GO:0033955"]).issubset(set(returnVal)))
        with self.assertRaises(InvalidParamsError):
            self.serviceImpl.get_descendants(self.ctx, {"key": "GO:0000002"})
        with self.assertRaises(InvalidParamsError):
          self.serviceImpl.get_descendants(self.ctx, {"id": "GO:0000002", "ns": "test"})

    def test_go_get_ancestors(self):
        ret = self.serviceImpl.get_ancestors(self.ctx, {"id": "GO:0000002"})
        returnVal=list(map(lambda x: x["term"]["id"], ret[0]["results"]))
        self.assertTrue(set(['GO:0006996', 'GO:0007005', 'GO:0008150','GO:0008150','GO:0009987', 'GO:0016043', 'GO:0071840']).issubset(set(returnVal)))

    def test_go_get_children(self):
        ret = self.serviceImpl.get_children(self.ctx, {"id": "GO:0000002"})
        returnVal=list(map(lambda x: x["term"]["id"], ret[0]["results"]))
        self.assertTrue(set(['GO:0033955']).issubset(set(returnVal)))

    def test_go_get_parents(self):
        ret = self.serviceImpl.get_parents(self.ctx, {"id": "GO:0000002"})
        returnVal=list(map(lambda x: x["term"]["id"], ret[0]["results"]))
        self.assertTrue(set(['GO:0007005']).issubset(set(returnVal)))

    def test_go_get_related(self):
        ret = self.serviceImpl.get_related(self.ctx, {"id": "GO:0000002"})
        returnVal=list(map(lambda x: x["term"]["id"], ret[0]["results"]))
        self.assertTrue(set(['GO:0007005', 'GO:0032042', 'GO:0033955']).issubset(set(returnVal)))

    def test_go_get_siblings(self):
        ret = self.serviceImpl.get_siblings(self.ctx, {"id": "GO:0000002"})
        returnVal=list(map(lambda x: x["id"], ret[0]["results"]))
        self.assertTrue(set(["GO:0000266", "GO:0007006", "GO:0007287", "GO:0008053", "GO:0008637", "GO:0030382", "GO:0048311", "GO:0061726", "GO:0070584", "GO:0097250"]).issubset(set(returnVal)))

    def test_go_get_terms(self):
        ret = self.serviceImpl.get_terms(self.ctx, {"ids": ["GO:0000002", "GO:0000266"]})
        returnVal=list(map(lambda x: x["id"], ret[0]["results"]))
        self.assertTrue(set(['GO:0000002', 'GO:0000266']).issubset(set(returnVal)))

    def test_go_get_hierarchical_ancestors(self):
        ret = self.serviceImpl.get_hierarchical_ancestors(self.ctx, {"id": "GO:0000002"})
        returnVal=list(map(lambda x: x["term"]["id"], ret[0]["results"]))
        self.assertTrue(set([ "GO:0006996", "GO:0007005", "GO:0008150", "GO:0008150", "GO:0009987", "GO:0016043", "GO:0071840"]).issubset(set(returnVal)))

    def test_go_get_hierarchical_children(self):
        ret = self.serviceImpl.get_hierarchical_children(self.ctx, {"id": "GO:0000002"})
        returnVal=list(map(lambda x: x["term"]["id"], ret[0]["results"]))
        self.assertTrue(set(['GO:0032042', 'GO:0033955']).issubset(set(returnVal)))

    def test_go_get_hierarchical_descendants(self):
        ret = self.serviceImpl.get_hierarchical_descendants(self.ctx, {"id": "GO:0000002"})
        returnVal=list(map(lambda x: x["term"]["id"], ret[0]["results"]))
        self.assertTrue(set(['GO:0032042', 'GO:0032043', 'GO:0033955', 'GO:0043504', 'GO:1901858', 'GO:1901859', 'GO:1901859', 'GO:1901860', 'GO:1901860', 'GO:1905951']).issubset(set(returnVal)))

    def test_go_get_hierarchical_parents(self):
        ret = self.serviceImpl.get_hierarchical_parents(self.ctx, {"id": "GO:0000002"})
        returnVal=list(map(lambda x: x["term"]["id"], ret[0]["results"]))
        self.assertTrue(set(['GO:0007005']).issubset(set(returnVal)))

    def test_go_get_associated_ws_genomes(self):
        ret = self.serviceImpl.get_associated_ws_genomes(self.ctx, {"id": "GO:0016209"})
        returnVal=list(map(lambda x: (x["ws_obj"]["workspace_id"], x["feature_count"]), ret[0]["results"]))
        self.assertTrue(ret[0]["total_count"] == 43)
        self.assertTrue((4258, 17) in returnVal)

    def test_go_get_associated_ws_features(self):
        ret = self.serviceImpl.get_associated_ws_features(self.ctx, {"id": "GO:0016209", "obj_ref": "4258/36981/3"})
        returnVal=list(map(lambda x: x["feature_id"], ret[0]["results"][0]["features"]))
        self.assertTrue(ret[0]["total_count"] == 7)
        self.assertTrue(set(["Thecc1EG022426"]).issubset(set(returnVal)))
        self.assertTrue(ret[0]["results"][0]["ws_obj"]["workspace_id"] == 4258)

    def test_go_get_terms_from_ws_feature(self):
        ret = self.serviceImpl.get_terms_from_ws_feature(self.ctx, {"obj_ref": "4258/36981/3", "feature_id": "Thecc1EG022426"})
        returnVal=list(map(lambda x: x["terms"][0]["id"], ret[0]["results"]))
        self.assertTrue(set(["GO:0016209"]).issubset(set(returnVal)))

    def test_go_get_terms_from_ws_object(self):
        ret = self.serviceImpl.get_terms_from_ws_object(self.ctx, {"obj_ref": "4258/36981/3"})
        returnVal=list(map(lambda x: x["terms"][0]["id"], ret[0]["results"]))
        self.assertTrue(set(["GO:0016747"]).issubset(set(returnVal)))

    def test_envo_get_ancestors(self):
        ret = self.serviceImpl.get_ancestors(self.ctx, {"id": "ENVO:00002041", "ns": "envo_ontology"})
        returnVal=list(map(lambda x: x["term"]["id"], ret[0]["results"]))
        self.assertTrue(set(['ENVO:00002006']).issubset(set(returnVal)))

    def test_envo_get_children(self):
        ret = self.serviceImpl.get_children(self.ctx, {"id": "ENVO:00002006",  "ns": "envo_ontology"})
        returnVal=list(map(lambda x: x["term"]["id"], ret[0]["results"]))
        self.assertTrue(set(['ENVO:00002041']).issubset(set(returnVal)))

    def test_envo_get_descendants(self):
        ret = self.serviceImpl.get_descendants(self.ctx, {"id": "ENVO:00002006",  "ns": "envo_ontology"})
        returnVal=list(map(lambda x: x["term"]["id"], ret[0]["results"]))
        self.assertTrue(set(["ENVO:00002041"]).issubset(set(returnVal)))

    def test_envo_get_parents(self):
        ret = self.serviceImpl.get_parents(self.ctx, {"id": "ENVO:00002041", "ns": "envo_ontology"})
        returnVal=list(map(lambda x: x["term"]["id"], ret[0]["results"]))
        self.assertTrue(set(['ENVO:00002006']).issubset(set(returnVal)))

    def test_envo_get_siblings(self):
        ret = self.serviceImpl.get_siblings(self.ctx, {"id": "ENVO:00002006",  "ns": "envo_ontology"})
        returnVal=list(map(lambda x: x["id"], ret[0]["results"]))
        self.assertTrue(set(["ENVO:00002985", "ENVO:01000558"]).issubset(set(returnVal)))

    def test_envo_get_terms(self):
        ret = self.serviceImpl.get_terms(self.ctx, {"ids": ["ENVO:00002041", "ENVO:00002006"], "ns": "envo_ontology"})
        returnVal=list(map(lambda x: x["id"], ret[0]["results"]))
        self.assertTrue(set(["ENVO:00002041", "ENVO:00002006"]).issubset(set(returnVal)))

    def test_envo_get_associated_samples(self):
        ret = self.serviceImpl.get_associated_samples(self.ctx, {"id": "ENVO:01000221", "ns": "envo_ontology"})
        returnVal=list(map(lambda x: x["sample"]["id"], ret[0]["results"]))
        self.assertTrue(ret[0]["total_count"] == 2)
        #self.assertTrue(set(["0795d792-54e1-430c-b280-da0849d7474c", "465b1476-3699-4e6c-a06b-8d384fcc41f3"]).issubset(set(returnVal)))

    def test_methods_not_implemented(self):
        ret = self.serviceImpl.get_associated_ws_genomes(self.ctx, {"id": "ENVO:00002006", "ns": "envo_ontology"})
        self.assertEqual(len(ret[0]["results"]), 0)
        self.assertTrue("Not found" in ret[0]["error"].get("message"))
