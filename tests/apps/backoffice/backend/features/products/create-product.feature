Feature: Create a new product
  As a user with admin permissions
  I want to create a non-existing product
  In order to have more products on the platform

  Scenario: A valid non-existing product
    When I send a PUT request to "/products/a30a0af2-79ad-498f-bafa-51e4910ebeec" with body
    """
    {
      "name": "Wireless Mouse"
    }
    """
    Then the response status code should be 201
    And the response content type header should be "text/plain"
    And the response should be empty
    And the response location header should be "/products/a30a0af2-79ad-498f-bafa-51e4910ebeec"

  Scenario: An invalid non-existing product [with bad id]
    When I send a PUT request to "/products/a30a0af2-79ad-498f-bafa-51e4910ebeec." with body
    """
    {
      "name": "Wireless Mouse"
    }
    """
    Then the response status code should be 422
    And the response content type header should be "text/plain"
    And the response content should be "Invalid id: 'a30a0af2-79ad-498f-bafa-51e4910ebeec.'"
    And the response location header should be "/products/a30a0af2-79ad-498f-bafa-51e4910ebeec."

  Scenario: An invalid non-existing product [with bad name]
    When I send a PUT request to "/products/a30a0af2-79ad-498f-bafa-51e4910ebeec" with body
    """
    {
      "name": "@Wireless Mouse"
    }
    """
    Then the response status code should be 422
    And the response content type header should be "text/plain"
    And the response content should be "Invalid name: '@Wireless Mouse'"
    And the response location header should be "/products/a30a0af2-79ad-498f-bafa-51e4910ebeec"