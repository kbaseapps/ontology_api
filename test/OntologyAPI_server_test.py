# -*- coding: utf-8 -*-
import os
import time
import unittest
from configparser import ConfigParser

from OntologyAPI.OntologyAPIImpl import OntologyAPI
from OntologyAPI.OntologyAPIServer import MethodContext
from OntologyAPI.authclient import KBaseAuth as _KBaseAuth
from OntologyAPI.exceptions import InvalidParamsError, REError

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
        ret = self.serviceImpl.get_descendants(self.ctx, {"key": "GO:0000002"})
        self.assertEqual(ret[0], ["GO:0033955"])
        with self.assertRaises(InvalidParamsError):
            self.serviceImpl.get_descendants(self.ctx, {"id": "GO:0000002"})

    def test_get_ancestors(self):
        ret = self.serviceImpl.get_ancestors(self.ctx, {"key": "GO:0000002"})
        self.assertEqual(ret[0], ['GO:0006996', 'GO:0007005', 'GO:0008150','GO:0008150','GO:0009987', 'GO:0016043', 'GO:0071840'])
