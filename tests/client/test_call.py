# -*- coding: utf-8 -*-
import unittest

try:
    from unittest.mock import Mock
except:
    from mock import Mock

from porthos.client import Call, TimeoutException


class TestCall(unittest.TestCase):

    def test_init(self):
        c = Call(None, "method", 200)

        self.assertEquals(c.method_name, "method")
        self.assertIsNotNone(c.corr_id)
        self.assertEquals(c.timeout, 200)
        self.assertIsNone(c.body)
        self.assertIsNone(c.response)
        self.assertEquals(c.content_type, "application/octet-stream")

    def test_with_timeout(self):
        c = Call(None, "method", 200).with_timeout(1000)

        self.assertEquals(c.timeout, 1000)

    def test_with_body(self):
        c = Call(None, "method", 200).with_body("foo")

        self.assertEquals(c.body, "foo")
        self.assertEquals(c.content_type, "application/octet-stream")

    def test_with_args(self):
        c = Call(None, "method", 200).with_args("foo", "bar")

        self.assertEquals(c.body, '["foo", "bar"]')
        self.assertEquals(c.content_type, "application/json")

    def test_with_dict(self):
        c = Call(None, "method", 200).with_dict({"foo": "bar"})

        self.assertEquals(c.body, '{"foo": "bar"}')
        self.assertEquals(c.content_type, "application/json")

    def test_sync(self):
        with self.assertRaises(TimeoutException):
            client = Mock()

            Call(client, "method", 200).sync()

        client.channel.basic_publish.assert_called_once()
        client.connection.process_data_events.assert_called_once()

