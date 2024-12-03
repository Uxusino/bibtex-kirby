*** Settings ***
Resource  ../resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Bibtexs
Library  Collections

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

Cannot add article from future
    Go To  ${HOME_URL}
    Click Link  Create article
    Input Text  title  Creating random articles.
    Input Text  author  Dummy, D.
    Input Text  journal  Journal about creating articles
    Input Text  year  2025
    Click Button  Create
    Page Should Contain    Invalid year.

User can create book
    Go To  ${HOME_URL}
    Click Link  Create book
    Input Text  title  Creating random books.
    Input Text  author  Dummy, A Book.
    Input Text  publisher  Publisher about creating books
    Input Text  year  2024
    Click Button  Create
    Page Should Contain  author: Dummy, A Book.

User can create inproceedings
    Go To  ${HOME_URL}
    Click Link  Create inproceedings
    Input Text  title  Creating random inproceedings.
    Input Text  author  Dummy, A Inproceedings.
    Input Text  booktitle  Booktitle about creating inproceedings
    Input Text  year  2024
    Click Button  Create
    Page Should Contain  author: Dummy, A Inproceedings.

User can create misc
    Go To  ${HOME_URL}
    Click Link  Create misc
    Input Text  title  Creating random misc.
    Input Text  author  Dummy, A Misc.
    Input Text  howpublished  Howpublished about creating misc
    Input Text  year  2024
    Click Button  Create
    Page Should Contain  author: Dummy, A Misc.

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

User can create and copy .bib
    Go To  ${HOME_URL}
    Click Link  Create article
    Input Text  title  moikka
    Input Text  author  moi
    Input Text  journal  1
    Input Text  year  2022
    Click Button  Create
    Click Button  Copy .bib
    Alert Should Be Present

User can create and copy all references
    Go To  ${HOME_URL}
    Click Link  Create article
    Input Text  title  Dummy Article
    Input Text  author  Dummy Author
    Input Text  journal  Dummy Journal
    Input Text  year  2024
    Click Button  Create
    Click Button  Copy all
    Alert Should Be Present