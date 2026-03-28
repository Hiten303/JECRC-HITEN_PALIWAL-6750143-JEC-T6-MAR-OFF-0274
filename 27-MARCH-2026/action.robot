*** Settings ***
Library  SeleniumLibrary
*** Variables ***
${url}  https://the-internet.herokuapp.com/drag_and_drop
${url1}  https://the-internet.herokuapp.com/
*** Test Cases ***
Handling drag and drop
     Open Browser  ${url}  chrome
     Sleep    3s
     Drag And Drop    id=column-a    id=column-b
     Sleep    2s

     Close Browser
     
Handling mouse hover
     Open Browser  ${url1}  chrome
     Sleep    3s
     Click Element    xpath=//a[text()="Hovers"]
     Sleep    3s
     Mouse Over    xpath=//h5[text()="name: user2"]/ancestor::div[@class="figure"]
     Sleep     3s
     Close Browser

Scroll to the element
     Open Browser  ${url1}  chrome
     Sleep    3s
     Scroll Element Into View    xpath=//a[text()="Typos"]
     Sleep    3s
     Close Browser