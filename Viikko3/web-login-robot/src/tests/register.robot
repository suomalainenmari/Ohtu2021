*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

***Test Cases***
Register With Valid Username And Password
  Set Username  testi
  Set Password  testi123
  Set Password_confirmation  testi123
  Click Button  Register
  Welcome Page Should Be Open

Register With Too Short Username And Valid Password
  Set Username  te
  Set Password  testi123
  Set Password_confirmation  testi123
  Click Button  Register
  Register Should Fail With Message  Username is too short

Register With Valid Username And Too Short Password
  Reset Application
  Set Username  testi
  Set Password  test4
  Set Password_confirmation  test4
  Click Button  Register
  Register Should Fail With Message  Password is too short

Register With Nonmatching Password And Password Confirmation
  Reset Application
  Set Username  testi
  Set Password  testi123
  Set Password_confirmation  testi111
  Click Button  Register
  Register Should Fail With Message  Password confirmation does not match password

Login After Successful Registration
  Reset Application
  Set Username  testi
  Set Password  testi123
  Set Password_confirmation  testi123
  Click Button  Register
  Welcome Page Should Be Open
  Go To Login Page
  Set Username  testi
  Set Password  testi123
  Click Button  Login
  Login Should Succeed

Login After Failed Registration
  Reset Application
  Set Username  te
  Set Password  testi123
  Set Password_confirmation  testi123
  Click Button  Register
  Register Should Fail With Message  Username is too short
  Go To Login Page
  Set Username  te
  Set Password  testi123
  Click Button  Login
  Login Should Fail With Message  Invalid username or password

***Keywords***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password_confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}