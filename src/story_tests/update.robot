*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Bibtexs
Library  Collections

*** Test Cases ***
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

User can add and delete non required fields
    Go To  ${HOME_URL}
    Click Link  Create article
    Input Text  title  Creating random articles.
    Input Text  author  Dummy, E.
    Input Text  journal  Journal about creating articles
    Input Text  year  2023
    Click Button  Create
    Click Element    bibtex-title
    Input Text  doi  1000.0
    Click Button  Save
    Page Should Contain    1000.0
    Click Element    bibtex-title
    Input Text  doi  ${EMPTY}
    Click Button  Save
    Page Should Not Contain    doi