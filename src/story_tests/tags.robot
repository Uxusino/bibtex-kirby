*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Bibtexs
Library  Collections

*** Test Cases ***
User can add tags
    Go To  ${HOME_URL}
    Click Link  Create article
    Input Text  title  Creating random articles.
    Input Text  author  Dummy, F.
    Input Text  journal  Journal about creating articles
    Input Text  year  2024
    Input Text    tags    random, robot
    Click Button    Create
    Page Should Contain    robot
    Page Should Contain    random

User can select and view references by a tag
    Go To  ${HOME_URL}
    Click Link  Create article
    Input Text  title  Creating random articles.
    Input Text  author  Dummy, F.
    Input Text  journal  Journal about creating articles
    Input Text  year  2024
    Input Text    tags    random, robot
    Click Button    Create
    Click Link    Create book
    Input Text    title    Not creating non-random books.
    Input Text    author    Dummy, G.
    Input Text    publisher    Dummy Publisher
    Input Text    year    2023
    Input Text    tags    not random, robot
    Click Button    Create
    Click Element    xpath=//div[@class='tag' and @data-tag='random'][1]
    Element Should Not Be Visible    xpath=//span[@class='bibtex-title' and @data-type='book']
