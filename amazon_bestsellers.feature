# Created by eyup at 10/18/2020
Feature: Amazon bestseller links test
  # Enter feature description here

  Scenario: Amazon bestsellers page displays 5 links
    Given Amazon bestsellers page
    Then Verify 5 links are displayed


    # Enter steps here