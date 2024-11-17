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
    Input Text  label  dummy2024article
    Input Text  title  Creating random articles.
    Input Text  author  Dummy, A.
    Input Text  journal  Journal about creating articles
    Input Text  year  2024
    Click Button  Create
    Page Should Contain  author: Dummy, A.

All required fields must be filled
    Go To  ${HOME_URL}
    Input Text  label  article2001dummy
    Input Text  author  Dummy, B.
    Input Text  journal  Journal about creating articles
    Input Text  year  2024
    Click Button  Create
    Page Should Not Contain    author: Dummy, B.