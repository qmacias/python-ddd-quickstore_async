Feature: API status
  As a health check endpoint
  I want to check the current api status
  In order to know the server is up and running

  Scenario: Check the API status
    When I send a GET request to "/status-check"
    Then the response status code should be 200
    And the response content type header should be "text/plain"
    And the response should be empty
    And the response location header should be "/status-check"