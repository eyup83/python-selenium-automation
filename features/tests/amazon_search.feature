# Created by eyup at 10/2/2020
Feature: Test for Amazon search
  # Enter feature description here

  Scenario: Amazon search returns correct result
  Given Open Amazon page
    When Input Dress into Amazon search field
    And Click on Amazon search icon
    Then Search result Dress is shown
