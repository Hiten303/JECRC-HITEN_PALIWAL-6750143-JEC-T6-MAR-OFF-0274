*** Settings ***
Documentation  handling dropdowns
Library  SeleniumLibrary
*** Variables ***
${url1}  https://testautomationpractice.blogspot.com/
*** Test Cases ***
handling multiselect
    Open Browser  ${url1}  chrome
    Page Should Contain Element    id=colors
    ${options}=  Get List Items    id=colors
    Select From List By Label    id=colors  Red  Blue
    ${select_options}=  Get Selected List Labels    id=colors
    Log To Console    ${select_options}
    Sleep    3s
    Close Browser