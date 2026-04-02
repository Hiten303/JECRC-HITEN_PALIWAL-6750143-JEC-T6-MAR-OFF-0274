*** Settings ***
Library  SeleniumLibrary
*** Variables ***
${url}  https://testautomationpractice.blogspot.com/
*** Test Cases ***
simple alerts
     Open Browser  ${url}  chrome
     Sleep    3s
     Click Button    xpath=//button[@id="alertBtn"]
     Handle Alert
     Log To Console    "You Pressed OK"
     Sleep    3s

Confirmation alert
     Open Browser  ${url}  chrome
     Sleep    3s
     Click Button    xpath=//button[@id="confirmBtn"]
     Handle Alert
     ${mainTitle}  Get Text  xpath=//p[@id="demo"]
     Sleep    3s
     Page Should Contain  ${mainTitle}
     Log To Console    ${mainTitle}
     Sleep    3s

Prompt alert
     Open Browser  ${url}  chrome
     Sleep    3s
     Click Button    xpath=//button[@id="promptBtn"]
     Input Text Into Alert    hiten paliwal
     ${mainTitle}  Get Text  xpath=//p[@id="demo"]
     Sleep    3s
     Page Should Contain  ${mainTitle}
     Log To Console    ${mainTitle}

     Sleep    3s