import json

from behave import when, then


@when('I send a GET request to "{endpoint}"')
def step_impl(context, endpoint):
    context.response = context.client.get(endpoint)


@when('I send a PUT request to "{endpoint}" with body')
def step_impl(context, endpoint):
    context.uri = endpoint
    context.request_body = json.loads(context.text)
    context.response = context.client.put(endpoint, json=context.request_body)


@then('the response status code should be {status_code:d}')
def step_impl(context, status_code):
    assert context.response.status_code == status_code


@then('the response content should be {content}')
def step_impl(context, content):
    print(context.response.content)
    print(content.encode())
    assert context.response.content == content.encode()


@then('the response content type header should be "{content_type}"')
def step_impl(context, content_type):
    headers = context.response.headers

    assert headers.get('Content-Type').split(';')[0].strip() == content_type


@then('the response should be empty')
def step_impl(context):
    assert context.response.content == b''


@then('the response location header should be "{location}"')
def step_impl(context, location):
    assert context.response.headers.get('Location') == location
