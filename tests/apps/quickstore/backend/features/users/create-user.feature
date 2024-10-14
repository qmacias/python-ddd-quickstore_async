Feature: Create a new user
  As a user
  I want to create a non-existing user
  In order to have more users on the platform

  Scenario: A valid non-existing user
    When I send a PUT request to "/users/5cbd55ab-3e3d-4b3b-b86d-cec4fa4917b7" with body
    """
    {
      "name": "John Doe",
      "email": "example@example.com"
    }
    """
    Then the response status code should be 201
    And the response content type header should be "text/plain"
    And the response should be empty
    And the response location header should be "/users/5cbd55ab-3e3d-4b3b-b86d-cec4fa4917b7"

  Scenario: An invalid non-existing user [with bad id]
    When I send a PUT request to "/users/5cbd55ab-3e3d-4b3b-b86d-cec4fa4917b7." with body
    """
    {
      "name": "John Doe",
      "email": "example@example.com"
    }
    """
    Then the response status code should be 422
    And the response content type header should be "text/plain"
    And the response content should be "Invalid id: '5cbd55ab-3e3d-4b3b-b86d-cec4fa4917b7.'"
    And the response location header should be "/users/5cbd55ab-3e3d-4b3b-b86d-cec4fa4917b7."

  Scenario: An invalid non-existing user [with bad name]
    When I send a PUT request to "/users/5cbd55ab-3e3d-4b3b-b86d-cec4fa4917b7" with body
    """
    {
      "name": "John.Doe",
      "email": "example@example.com"
    }
    """
    Then the response status code should be 422
    And the response content type header should be "text/plain"
    And the response content should be "Invalid name: 'John.Doe'"
    And the response location header should be "/users/5cbd55ab-3e3d-4b3b-b86d-cec4fa4917b7"

  Scenario: An invalid non-existing user [with bad email]
    When I send a PUT request to "/users/5cbd55ab-3e3d-4b3b-b86d-cec4fa4917b7" with body
    """
    {
      "name": "John Doe",
      "email": "example@example"
    }
    """
    Then the response status code should be 422
    And the response content type header should be "text/plain"
    And the response content should be "Invalid email: 'example@example'"
    And the response location header should be "/users/5cbd55ab-3e3d-4b3b-b86d-cec4fa4917b7"