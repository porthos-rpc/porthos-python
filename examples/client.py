# -*- coding: utf-8 -*-
import os

import porthos


def run_example():
    with porthos.Client(os.environ["AMQP_URL"], "SampleService") as c:
        try:
            response = c.call("method").with_timeout(300000).with_dict({"foo": "bar"}).sync()

            if response.status_code == porthos.Status.OK:
                print("Got content type: %s" % response.content_type)
                print(response.content)
            else:
                print("Got status code: %d" % response.status_code)
        except porthos.TimeoutException:
            print("TimeoutException")


if __name__ == "__main__":
    run_example()

