# Created by eyup at 10/31/2020
Feature: Make sure user can open and close Amazon Applications

  Scenario: User can open and close Amazon Applications
    Given Open Amazon T&C page
    When Store original windows
    Then Click on Amazon applications link
    Then Switch to the newly opened window
    Then Amazon app page is opened
    Then User can close new window and switch back to original
