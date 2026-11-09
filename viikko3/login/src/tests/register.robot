*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  pekka
    Set Password  pekka123
    Set Password Confirmation  pekka123
    Click  button >> text=Register
    Register Should Succeed

Register With Matching Password Confirmation
    Set Username  pekka
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click  button >> text=Register
    Register Should Succeed

Register With Different Password Confirmation
    Set Username  pekka
    Set Password  kalle123
    Set Password Confirmation  kalle124
    Click  button >> text=Register
    Register Should Fail With Message  Password and password confirmation do not match

Register With Password Containing A Digit
    Set Username  pekka
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click  button >> text=Register
    Register Should Succeed

Register With Password Containing A Symbol
    Set Username  pekka
    Set Password  kalle#abc
    Set Password Confirmation  kalle#abc
    Click  button >> text=Register
    Register Should Succeed

Register With Password Consisting Only Of Lowercase Letters
    Set Username  pekka
    Set Password  kallekalle
    Set Password Confirmation  kallekalle
    Click  button >> text=Register
    Register Should Fail With Message  Password must contain a character that is not a letter

Register With Password Consisting Only Of Mixed Case Letters
    Set Username  pekka
    Set Password  KalleKalle
    Set Password Confirmation  KalleKalle
    Click  button >> text=Register
    Register Should Fail With Message  Password must contain a character that is not a letter

Register With Too Short Username And Valid Password
    Set Username  pe
    Set Password  pekka123
    Set Password Confirmation  pekka123
    Click  button >> text=Register
    Register Should Fail With Message  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username  pekka
    Set Password  pekka12
    Set Password Confirmation  pekka12
    Click  button >> text=Register
    Register Should Fail With Message  Password must be at least 8 characters long

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click  button >> text=Register
    Register Should Fail With Message  User with username kalle already exists

*** Keywords ***
Register Should Succeed
    Get Title  ==  Welcome to Ohtu Application!

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Get Text  body  *=  ${message}

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page
