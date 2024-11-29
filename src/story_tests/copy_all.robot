*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Bibtexs
Library  Collections

*** Test Cases ***
User can copy all references
    Go To  ${HOME_URL}
    Click Link  Create article
    Input Text  title  Dummy Article
    Input Text  author  Dummy Author
    Input Text  journal  Dummy Journal
    Input Text  year  2024
    Click Button  Create
    Click Button  Copy all
    Alert Should Be Present