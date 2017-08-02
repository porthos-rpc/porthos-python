# Porthos

A RPC over AMQP library for Python.

## Goal

Provide a language-agnostic RPC library to write distributed systems.

## Client

```python
with porthos.Client("amqp://guest:guest@broker:5672/myVHost", "SampleService") as c:
    # call with a dict body
    response = c.call("method").with_dict({"foo": "bar"}).sync()

    if response.status_code == porthos.Status.OK:
        # extract a dict from the response (if response status code is application/json).
        print(response.as_dict())

    # call with *args body.
    response = c.call("method").with_args("foo", "bar").sync()

    if response.status_code == porthos.Status.OK:
        print(response.content)

    # call with a str body.
    response = c.call("method").with_body("foo").sync()

    if response.status_code == porthos.Status.OK:
        print(response.content)
```

## Server

Not implemented yet.

## Contributing

Pull requests are very much welcomed. Make sure a test or example is included that covers your change.

Docker is being used for the local environment. To build/run/test your code you can bash into the server container:

```sh
$ docker-compose run client bash
root@porthos:/usr/src/app# pytest
```

