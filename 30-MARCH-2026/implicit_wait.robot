*** Settings ***
Library  SeleniumLibrary
Library    Collections
*** Variables ***
${url}  https://the-internet.herokuapp.com/windows

*** Test Cases ***
implicit wait
    Open Browser  ${url}  chrome
    ${before}  Get Selenium Implicit Wait
    Log To Console    ${before}
    Set Selenium Implicit Wait    3s
    ${after}  Get Selenium Implicit Wait
    Log To Console    ${after}
    Close Browser