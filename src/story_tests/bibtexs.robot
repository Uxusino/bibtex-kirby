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
    Input Text  title  Creating random articles.
    Input Text  author  Dummy, A.
    Input Text  journal  Journal about creating articles
    Input Text  year  2024
    Click Button  Create
    Page Should Contain  author: Dummy, A.

All required fields must be filled
    Go To  ${HOME_URL}
    Input Text  author  Dummy, B.
    Input Text  journal  Journal about creating articles
    Input Text  year  2024
    Click Button  Create
    Page Should Not Contain    author: Dummy, B.

Year must be an integer
    Go To  ${HOME_URL}
    Input Text  title  Creating random articles.
    Input Text  author  Dummy, C.
    Input Text  journal  Journal about creating articles
    Input Text  year  gazillion
    Click Button  Create
    Page Should Contain    Year must be an integer.

Cannot add article from future
    Go To  ${HOME_URL}
    Input Text  title  Creating random articles.
    Input Text  author  Dummy, D.
    Input Text  journal  Journal about creating articles
    Input Text  year  2025
    Click Button  Create
    Page Should Contain    Invalid year.