*** Settings ***
Library  SeleniumLibrary
*** Variables ***
${url}=  https://inc.in/
*** Test Cases ***
handling js 
    Open Browser  ${url}  chrome
    Sleep    3s
    Execute Javascript  window.scrollTo(0,document.body.scrollHeight)
    Sleep    3s
    Close Browser