*** Settings ***
Documentation  handling checkboxes
Library  SeleniumLibrary
*** Variables ***
${url}  https://the-internet.herokuapp.com/
${url1}  https://testautomationpractice.blogspot.com/
*** Test Cases ***
Handling Checkboxes
    [Documentation]  herokuapp checkboxes
    Open Browser  ${url}  chrome
    Sleep    2s
    Click Element  xpath=//a[text()="Checkboxes"]
    Page Should Contain Checkbox  xpath=(//input[@type="checkbox"])[1]
    Select Checkbox  xpath=(//input[@type="checkbox"])[1]
    Sleep    3s
    Unselect Checkbox    xpath=(//input[@type="checkbox"])[2]
    Sleep    3s
    
Handling checkboxes in automation sites
    [Documentation]  handling few checkboxes
    Open Browser  ${url1}  chrome
    Sleep    3s
    Page Should Contain Checkbox    id=sunday
    Select Checkbox    id=sunday
    Sleep    2s
    Close Browser