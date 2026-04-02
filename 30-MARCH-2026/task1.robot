*** Settings ***
Library  SeleniumLibrary
*** Variables ***
${url}  https://testautomationpractice.blogspot.com/
*** Test Cases ***
task
   Open Browser  ${url}  chrome
   Sleep    3s
   Click Element    xpath=//button[@id="PopUp"]
   Sleep    3s

   @{windows}  Get Window Handles
   @{titles}  Get Window Titles
   Log To Console    ${titles}


   Switch Window  NEW

   Switch Window  ${windows}[0]
   ${mainTitle}  Get Text  class=title
   Sleep    3s
   Page Should Contain  ${mainTitle}

   Close Browser