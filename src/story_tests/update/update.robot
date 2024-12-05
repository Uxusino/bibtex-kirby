*** Settings ***
Resource  ../resource.robot
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
    Title Should Be  Bibtex app
    Click Element    bibtex-title
    Input Text  title  Updating random articles.
    Click Button  Save
    Wait For Condition    return document.readyState=="complete"
    Page Should Contain    Updating random articles.