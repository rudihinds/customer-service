Feature: Create customer

  Scenario: A new customer is added
    When I create customer "Gene Kim"
    Then I should be able to fetch customer details for "Gene Kim"
