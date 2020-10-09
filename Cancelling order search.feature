# Created by eyup at 10/7/2020
Feature: Search for cancelling an order on Amazon
  # Enter feature description here

  Scenario: Amazon search for cancelling order returns correct result
    Given Open Amazon help page
    When Input cancel order into help search field, hit enter
    Then Search result Cancel items or orders is shown

