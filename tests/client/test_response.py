# -*- coding: utf-8 -*-
import unittest

from porthos.client import Response

class TestResponse(unittest.TestCase):

    def test_as_dict(self):
        d = Response(content_type='application/json', content='{"foo": "bar"}').as_dict()

        self.assertEquals(d, {"foo": "bar"})

    def test_as_dict_wrong_content_type(self):
        with self.assertRaises(ValueError) as context:
            Response(content_type='application/octet-stream', content='foo').as_dict()

        self.assertTrue('Content-Type is not application/json: application/octet-stream' in context.exception)
