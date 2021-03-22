*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  mari  maris123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  testi  testi2342424
    Output Should Contain  Username is already taken

Register With Too Short Username And Valid Password
    Input Credentials  ai  testi4433
    Output Should Contain  Username has to be a minimum of 3 characters

Register With Valid Username And Too Short Password
    Input Credentials  toimiva  test3
    Output Should Contain  Password has to be a minimum of 8 characters

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  username  nonumbers
    Output Should Contain  Password must contain numbers

*** Keywords ***
Input New Command And Create User
    Create User  testi  testi123
    Input New Command
