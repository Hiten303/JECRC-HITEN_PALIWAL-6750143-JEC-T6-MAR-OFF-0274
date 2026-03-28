*** Settings ***
Documentation  Opening of browsers
Library  SeleniumLibrary
*** Variables ***
# scalar variables
${url}  https://www.cricbuzz.com/
# list variables
@{bikes}  ktm  splendor  ct100  bullet
# dict variable
&{cars}  nissan=gtr  honda=civic
*** Test Cases ***
Opening Chrome Browser
   [Documentation]  Chrome browser navigating to https://crickbuzz
   Open Browser   ${url}  chrome
   Maximize Browser Window
   Log  navigated to cricbuzz
   Log To Console    ${bikes}[1]
   Sleep    3s

Open cricbuzz in edge
    Opening Edge Browser

*** Keywords ***
Opening Edge Browser
    [Documentation]  Edge browser navigating to https://google
    Open Browser  ${url}  edge
    Log  navigate to google
    Log To Console    ${bikes}[1]
    Sleep    3s

    Close Browser