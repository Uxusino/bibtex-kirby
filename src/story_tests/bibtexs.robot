*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Bibtexs

*** Test Cases ***
At start there are no bibtexs
    Go To  ${HOME_URL}
    Title Should Be  Bibtex app
    Page Should Contain  You don't have references yet.

After adding a bibtex, there is one
    Go To  ${HOME_URL}
    Input Text  label  Dummy article
    Click Button  Create
    Page Should Contain  author: Dummy Author