*** Settings ***
Library  SeleniumLibrary
*** Variables ***
${url}  https://the-internet.herokuapp.com/javascript_alerts
*** Test Cases ***
simple alerts
     Open Browser  ${url}  chrome
     Sleep    3s
     Click Button    xpath=//button[@onclick="jsAlert()"]
     Handle Alert
     Sleep    3s

Confirmation alert
     Open Browser  ${url}  chrome
     Sleep    3s
     Click Button    xpath=//button[@onclick="jsConfirm()"]
     Handle Alert   action=DISMISS
     Sleep    3s
Prompt alert
     Open Browser  ${url}  chrome
     Sleep    3s
     Click Button    xpath=//button[@onclick="jsPrompt()"]
     Input Text Into Alert    hiten paliwal   action=DISMISS

     Sleep    3s