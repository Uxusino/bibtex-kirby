*** Settings ***
Resource  ../resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Bibtexs
Library  Collections

*** Test Cases ***
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