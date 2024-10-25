Feature: Create a new product review
  As a user
  I want to create a non-existing product review
  In order to have more product reviews on the platform

  Scenario: A valid non-existing product review
    When I send a PUT request to "/productreviews/49f84042-349b-43a1-8d45-6222ab0987bf" with body
    """
    {
      "userId": "e780d7c6-2b0c-4977-bbb4-1bdad3fc56ec",
      "productId": "25347ff2-5b98-4903-95df-fa7a351ed806",
      "rating": 4
    }
    """
    Then the response status code should be 201
    And the response content type header should be "text/plain"
    And the response should be empty
    And the response location header should be "/productreviews/49f84042-349b-43a1-8d45-6222ab0987bf"

  Scenario: An invalid non-existing product review [with bad id]
    When I send a PUT request to "/productreviews/49f84042-349b-43a1-8d45-6222ab0987bf." with body
    """
    {
      "userId": "e780d7c6-2b0c-4977-bbb4-1bdad3fc56ec",
      "productId": "25347ff2-5b98-4903-95df-fa7a351ed806",
      "rating": 4
    }
    """
    Then the response status code should be 422
    And the response content type header should be "text/plain"
    And the response content should be "Invalid id: '49f84042-349b-43a1-8d45-6222ab0987bf.'"
    And the response location header should be "/productreviews/49f84042-349b-43a1-8d45-6222ab0987bf."

  Scenario: An invalid non-existing product review [with bad rating]
    When I send a PUT request to "/productreviews/49f84042-349b-43a1-8d45-6222ab0987bf" with body
    """
    {
      "userId": "e780d7c6-2b0c-4977-bbb4-1bdad3fc56ec",
      "productId": "25347ff2-5b98-4903-95df-fa7a351ed806",
      "rating": -1
    }
    """
    Then the response status code should be 422
    And the response content type header should be "text/plain"
    And the response content should be "Invalid number: -1"
    And the response location header should be "/productreviews/49f84042-349b-43a1-8d45-6222ab0987bf"