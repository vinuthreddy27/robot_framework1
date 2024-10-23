*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}        https://testautomationpractice.blogspot.com/
${browser}     chrome

*** Test Cases ***
LoginTest
   open browser   ${url}    ${browser}
   maximize browser window
   set selenium speed   1seconds
   title should be    Automation Testing Practice
   input text     id:name     vinuthreddy
   click element  xpath://input[@value='male']
   Double Click Element  xpath://button[.='Copy Text']
   select checkbox    id:sunday
   select checkbox    id:monday
   select checkbox    id:tuesday
   select checkbox    id:wednesday
   select checkbox    id:thursday
   select checkbox    id:friday
   select checkbox    id:saturday
   close browser




