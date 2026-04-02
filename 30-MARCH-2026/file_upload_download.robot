*** Settings ***
Library  SeleniumLibrary
Library  OperatingSystem
*** Variables ***
${url}   https://the-internet.herokuapp.com/
${check_downloads}  C:\\Users\\user\\OneDrive\\Downloads\\file.txt
*** Test Cases ***
Upload
     Open Browser  ${url}  chrome
     Click Element    xpath=//a[@href="/upload"]

     ${path}  Normalize Path   ${CURDIR}/reports/selenium-screenshot-7.png
     Choose File    id=file-upload    ${path}
     Sleep    2s
     Click Button    id=file-submit
     Sleep    2s
     Close Browser

Download
    Open Browser  ${url}  chrome
    Click Element    xpath=//a[@href="/download"]
    Sleep    3s
    Click Element    xpath=//a[@href="download/file.txt"]
    Wait Until Created    ${check_downloads}  timeout=10s
    File Should Exist    ${check_downloads}
    Log To Console    downloaded successfully
    Close Browser