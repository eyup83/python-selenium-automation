# Created by eyup at 10/8/2020
Feature: Open amazon, click cart, verify your cart is empty
  # Enter feature description here

  Scenario: Verify your shopping cart is empty appear
    Given Open Amazon home page
    When Click on Cart
    Then Your shopping cart is empty is shown
