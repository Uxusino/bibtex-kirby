*** Settings ***
Resource  ../resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Bibtexs
Library  Collections

*** Test Cases ***
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