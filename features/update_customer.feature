Feature: Update the customer based on id
  As a service I want to update the customer name.

  Scenario: Update existing customer
    Given customer "Nicole Forsgren" with ID "12345" exists
    When I update customer "12345" with surname "Woods"
    And I fetch customer "12345"
    Then I should see customer "Nicole Woods"
    