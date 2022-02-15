*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
  Input Credentials  kalle  kalle123
  Output Should Contain  New user registered

Register With Already Taken Username And Password
  Input Credentials  pentti  salasana1
  Output Should Contain  Username is already in use

Register With Too Short Username And Valid Password
  Input Credentials  pe  testisalasana
  Output Should Contain  Username is too short

Register With Valid Username And Too Short Password
  Input Credentials  mikko  salasan
  Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
  Input Credentials  marko  salasana
  Output Should Contain  Password should not be only letters

*** Keywords ***
Create User And Input New Command
  Create User  pentti  salasana1
  Input New Command