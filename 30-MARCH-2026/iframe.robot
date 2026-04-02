*** Settings ***
Library  SeleniumLibrary
*** Variables ***
${url}  https://demo.automationtesting.in/Frames.html
*** Test Cases ***
handling single iframe
   Open Browser  ${url}  chrome
   Sleep    3s
   
   Select Frame    id=singleframe
   Input Text    xpath=//input[@type="text"]    Hiten Paliwal
   Sleep    3s
   Unselect Frame
   
   Click Element    xpath=//a[@href="#Multiple"]
   Select Frame     xpath=//iframe[@src="MultipleFrames.html"]
   Select Frame    xpath=//iframe[@src="SingleFrame.html"]
   Input Text        xpath=//input[@type="text"]    Hiten Paliwal
   ${text}  Get Value    xpath=//input[@type="text"]
   Log To Console    ${text}
   Sleep    3s
   Unselect Frame
   Close Browser