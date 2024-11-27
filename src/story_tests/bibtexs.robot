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
    Click Link  Create article
    Input Text  title  Creating random articles.
    Input Text  author  Dummy, A.
    Input Text  journal  Journal about creating articles
    Input Text  year  2024
    Click Button  Create
    Page Should Contain  author: Dummy, A.

All required fields must be filled
    Go To  ${HOME_URL}
    Click Link  Create article
    Input Text  author  Dummy, B.
    Input Text  journal  Journal about creating articles
    Input Text  year  2024
    Click Button  Create
    Page Should Not Contain    author: Dummy, B.

Year must be an integer
    Go To  ${HOME_URL}
    Click Link  Create article
    Input Text  title  Creating random articles.
    Input Text  author  Dummy, C.
    Input Text  journal  Journal about creating articles
    Input Text  year  gazillion
    Click Button  Create
    Page Should Contain    Year must be an integer.

Cannot add article from future
    Go To  ${HOME_URL}
    Click Link  Create article
    Input Text  title  Creating random articles.
    Input Text  author  Dummy, D.
    Input Text  journal  Journal about creating articles
    Input Text  year  2025
    Click Button  Create
    Page Should Contain    Invalid year.

Deletion success
    Go To  ${HOME_URL}
    Click Link  Create article
    Input Text  title  Creating random articles.
    Input Text  author  Dummy, D.
    Input Text  journal  Journal about creating articles
    Input Text  year  2023
    Click Button  Create
    Click Button  Delete
    Page Should Contain  You don't have references yet.

User can update references
    Go To  ${HOME_URL}
    Click Link  Create article
    Input Text  title  Creating random articles.
    Input Text  author  Dummy, E.
    Input Text  journal  Journal about creating articles
    Input Text  year  2023
    Click Button  Create
    Click Element    bibtex-title
    Input Text  title  Updating random articles.
    Click Button  Save
    Page Should Contain    Updating random articles.

User can search references
    Go To  ${HOME_URL}
    Click Link  Create article
    Input Text  title  Creating random articles.
    Input Text  author  Dummy, A.
    Input Text  journal  Journal about creating articles
    Input Text  year  2024
    Click Button  Create

    Input Text  query  å
    Click Button  Search
    Page Should Contain  No results

    Input Text  query  creating
    Click Button  Search
    Page Should Contain  Creating random articles.

    Input Text  query  y
    Click Button  Search
    Page Should Contain  Creating random articles.