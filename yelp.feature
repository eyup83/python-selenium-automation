# Created by eyup at 10/31/2020
Feature: Window handling

  Scenario: Company's website is opening
    Given Open Yelp page
    When Click on website link
    And Switch to a new window
    Then The kebab shop website is open
    And A user can close the new window and go to the original
