*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}        https://demowebshop.tricentis.com/
${browser}    chrome
${email}      reddyvinuth27@gmail.com
${password}   selenium

*** Keywords ***
Before Scenario
      open browser    ${url}   ${browser}
      maximize browser window

After Scenario
      close browser

Navigated to the homepage
      title should be    Demo Web Shop

Click On Login Link
      click element      xpath://a[@href='/login']

[Arguments]      ${email}     ${password}
Enter credentials into Email and Password fields
      input text         Email       ${email}
      input text         Password    ${password}

Click On Login BTN
      click element      xpath://input[@value='Log in']
