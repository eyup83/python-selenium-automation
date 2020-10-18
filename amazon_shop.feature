# Created by eyup at 10/18/2020
Feature: Add product to cart and make sure it is there

  Scenario: Verify added to cart appears
  Given Open Amazon page
  When Input watch into search field
  When click on amazon search button
  When Click on the watch
  When Click on add to cart button
  Then Verify added to cart is shown
    # Enter steps here