# Created by eyup at 10/5/2020
Feature: Amazon search
  # Enter feature description here

  Scenario: Amazon product search and page opened
    Given Open Amazon page
    When Input Shoes into Amazon search field and click search
    Then Verify page contains "Shoes"