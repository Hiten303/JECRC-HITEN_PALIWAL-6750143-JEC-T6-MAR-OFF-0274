*** Settings ***
Library  SeleniumLibrary
*** Variables ***
${url}  https://www.amazon.in/
*** Test Cases ***
amazon
    Open Browser  ${url}  chrome
    Sleep    2s
    Click Element    xpath=//a[@href="/electronics/b/?ie=UTF8&node=976419031&ref_=nav_cs_electronics"]
    Sleep    2s
    Click Element    xpath=//label[@for="apb-browse-refinements-checkbox_6"]/i
    Sleep    2s

    ${product_name}=    Get Text    xpath=(//h2[contains(@class,"a-size-base-plus")]/span)[2]
    Log To Console    ${product_name}
    Sleep    2s
    Click Element    xpath=(//span[@data-component-type="s-product-image"])[2]/a
    Sleep    2s
    @{windows}  Get Window Handles
    Sleep    3s
    Switch Window  new
    Sleep    3s
    Page Should contain  ${product_name}
    Sleep    3s
    ${actual_price}  Get Text    xpath=//span[@class="a-price-whole"]
    Log To Console    ${actual_price}

    Sleep    3s

    ${discount}   Get Text    xpath=//span[@class="apex-savings-container"]/span
    Log To Console    ${discount}
    Sleep    3s
    Scroll Element Into View    id=add-to-cart-button
    Sleep    3s
    Click Element    id=add-to-cart-button
    Sleep    3s
    Click Element    id=nav-cart-count
    Sleep    3s
    Page Should Contain  ${product_name}
    Sleep    3s
    Switch Window
    Close Browser