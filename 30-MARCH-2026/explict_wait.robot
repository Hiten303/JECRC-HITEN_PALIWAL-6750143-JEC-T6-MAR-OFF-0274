*** Settings ***
Library  SeleniumLibrary
*** Variables ***
${url}  https://practicetestautomation.com/practice-test-login/
*** Test Cases ***
explicit wait example
    Open Browser  ${url}  chrome

    Wait Until Element Is Visible    id=username
    Input Text     id=username    text