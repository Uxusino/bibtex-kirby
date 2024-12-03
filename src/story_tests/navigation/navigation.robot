*** Settings ***
Resource  ../resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Bibtexs
Library  Collections

*** Test Cases ***
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

User can sort references by order of creation first
    Go To  ${HOME_URL}
    Click Link  Create article
    Input Text  title  A
    Input Text  author  Ensimmäinen, 1.
    Input Text  journal  Journal about creating articles
    Input Text  year  2023
    Click Button  Create
    Go To  ${HOME_URL}
    Click Link  Create article
    Input Text  title  B
    Input Text  author  Toinen, 2.
    Input Text  journal  Journal about creating articles
    Input Text  year  2023
    Click Button  Create
    Go To  ${HOME_URL}
    Click Link  Create article
    Input Text  title  C
    Input Text  author  Kolmas, 3.
    Input Text  journal  Journal about creating articles
    Input Text  year  2023
    Click Button  Create
    Go To  ${HOME_URL}
    Select From List By Label    id=sort-options    Created first
    ${elements}=  Get WebElements  xpath=//li[contains(@class, 'bibtex-item')]//span[contains(@class, 'bibtex-title')]
    ${titles}=  Create List
    FOR  ${element}  IN  @{elements}
        ${text}=  Get Text  ${element}
        Append To List  ${titles}  ${text}
    END
    Log Many  ${titles}
    Should Be Equal  ${titles[0]}  A
    Should Be Equal  ${titles[1]}  B
    Should Be Equal  ${titles[2]}  C
User can sort references by order of creation last
    Go To  ${HOME_URL}
    Click Link  Create article
    Input Text  title  A1
    Input Text  author  Ensimmäinen, 1.
    Input Text  journal  Journal about creating articles
    Input Text  year  2023
    Click Button  Create
    Go To  ${HOME_URL}
    Click Link  Create article
    Input Text  title  B2
    Input Text  author  Toinen, 2.
    Input Text  journal  Journal about creating articles
    Input Text  year  2023
    Click Button  Create
    Go To  ${HOME_URL}
    Click Link  Create article
    Input Text  title  C3
    Input Text  author  Kolmas, 3.
    Input Text  journal  Journal about creating articles
    Input Text  year  2023
    Click Button  Create
    Go To  ${HOME_URL}
    Select From List By Label    id=sort-options    Created last
    ${elements}=  Get WebElements  xpath=//li[contains(@class, 'bibtex-item')]//span[contains(@class, 'bibtex-title')]
    ${titles}=  Create List
    FOR  ${element}  IN  @{elements}
        ${text}=  Get Text  ${element}
        Append To List  ${titles}  ${text}
    END
    Log Many  ${titles}
    Should Be Equal  ${titles[0]}  C3
    Should Be Equal  ${titles[1]}  B2
    Should Be Equal  ${titles[2]}  A1
User can sort references alphabetically a-z
    Go To  ${HOME_URL}
    Click Link  Create article
    Input Text  title  CC
    Input Text  author  Ensimmäinen, 1.
    Input Text  journal  Journal about creating articles
    Input Text  year  2023
    Click Button  Create
    Go To  ${HOME_URL}
    Click Link  Create article
    Input Text  title  AA
    Input Text  author  Toinen, 2.
    Input Text  journal  Journal about creating articles
    Input Text  year  2023
    Click Button  Create
    Go To  ${HOME_URL}
    Click Link  Create article
    Input Text  title  DD
    Input Text  author  Kolmas, 3.
    Input Text  journal  Journal about creating articles
    Input Text  year  2023
    Click Button  Create
    Go To  ${HOME_URL}
    Select From List By Label    id=sort-options    A-Z
    ${elements}=  Get WebElements  xpath=//li[contains(@class, 'bibtex-item')]//span[contains(@class, 'bibtex-title')]
    ${titles}=  Create List
    FOR  ${element}  IN  @{elements}
        ${text}=  Get Text  ${element}
        Append To List  ${titles}  ${text}
    END
    Log Many  ${titles}
    Should Be Equal  ${titles[0]}  AA
    Should Be Equal  ${titles[1]}  CC
    Should Be Equal  ${titles[2]}  DD

User can sort references alphabetically z-a
    Go To  ${HOME_URL}
    Click Link  Create article
    Input Text  title  CC
    Input Text  author  Ensimmäinen, 1.
    Input Text  journal  Journal about creating articles
    Input Text  year  2023
    Click Button  Create
    Go To  ${HOME_URL}
    Click Link  Create article
    Input Text  title  AA
    Input Text  author  Toinen, 2.
    Input Text  journal  Journal about creating articles
    Input Text  year  2023
    Click Button  Create
    Go To  ${HOME_URL}
    Click Link  Create article
    Input Text  title  DD
    Input Text  author  Kolmas, 3.
    Input Text  journal  Journal about creating articles
    Input Text  year  2023
    Click Button  Create
    Go To  ${HOME_URL}
    Select From List By Label    id=sort-options    Z-A
    ${elements}=  Get WebElements  xpath=//li[contains(@class, 'bibtex-item')]//span[contains(@class, 'bibtex-title')]
    ${titles}=  Create List
    FOR  ${element}  IN  @{elements}
        ${text}=  Get Text  ${element}
        Append To List  ${titles}  ${text}
    END
    Log Many  ${titles}
    Should Be Equal  ${titles[0]}  DD
    Should Be Equal  ${titles[1]}  CC
    Should Be Equal  ${titles[2]}  AA


User can sort references by modification latest
    Go To  ${HOME_URL}
    Click Link  Create article
    Input Text  title  First reference
    Input Text  author  First Author
    Input Text  journal  Journal 1
    Input Text  year  2023
    Click Button  Create
    Go To  ${HOME_URL}
    Click Link  Create article
    Input Text  title  Second reference
    Input Text  author  Second Author
    Input Text  journal  Journal 2
    Input Text  year  2023
    Click Button  Create
    Go To  ${HOME_URL}
    Click Link  Create article
    Input Text  title  Third reference
    Input Text  author  Third Author
    Input Text  journal  Journal 3
    Input Text  year  2023
    Click Button  Create

    # Edit the first reference
    Click Element  xpath=//span[@class='bibtex-title' and contains(text(), 'First reference')]
    Input Text  title  First reference edited
    Click Button  Save
    Sleep  1s

    # Edit the second reference
    Click Element  xpath=//span[@class='bibtex-title' and contains(text(), 'Second reference')]
    Input Text  title  Second reference edited
    Click Button  Save
    Sleep  1s

    # Edit the third reference
    Click Element  xpath=//span[@class='bibtex-title' and contains(text(), 'Third reference')]
    Input Text  title  Third reference edited
    Click Button  Save
    Sleep  1s

    # Sort by earliest modified
    Go To  ${HOME_URL}
    Select From List By Label    id=sort-options    Earliest modified
    Sleep  1s

    # Verify the order
    ${elements}=  Get WebElements  xpath=//li[contains(@class, 'bibtex-item')]//span[contains(@class, 'bibtex-title')]
    ${titles}=  Create List
    FOR  ${element}  IN  @{elements}
        ${text}=  Get Text  ${element}
        Append To List  ${titles}  ${text}
    END
    Log Many  ${titles}
    Should Be Equal  ${titles[0]}  First reference edited
    Should Be Equal  ${titles[1]}  Second reference edited
    Should Be Equal  ${titles[2]}  Third reference edited

User can sort references by modification earliest 
    Go To  ${HOME_URL}
    Click Link  Create article
    Input Text  title  First reference
    Input Text  author  First Author
    Input Text  journal  Journal 1
    Input Text  year  2023
    Click Button  Create
    Go To  ${HOME_URL}
    Click Link  Create article
    Input Text  title  Second reference
    Input Text  author  Second Author
    Input Text  journal  Journal 2
    Input Text  year  2023
    Click Button  Create
    Go To  ${HOME_URL}
    Click Link  Create article
    Input Text  title  Third reference
    Input Text  author  Third Author
    Input Text  journal  Journal 3
    Input Text  year  2023
    Click Button  Create

    # Edit the second reference
    Click Element  xpath=//span[@class='bibtex-title' and contains(text(), 'Second reference')]
    Input Text  title  Second reference edited again
    Click Button  Save
    Sleep  1s

    # Edit the first reference
    Click Element  xpath=//span[@class='bibtex-title' and contains(text(), 'First reference')]
    Input Text  title  First reference edited again
    Click Button  Save
    Sleep  1s

    # Edit the third reference
    Click Element  xpath=//span[@class='bibtex-title' and contains(text(), 'Third reference')]
    Input Text  title  Third reference edited again
    Click Button  Save
    Sleep  1s

    # Sort by earliest modified
    Go To  ${HOME_URL}
    Select From List By Label    id=sort-options    Earliest modified
    Sleep  5s

    # Verify the order
    ${elements}=  Get WebElements  xpath=//li[contains(@class, 'bibtex-item')]//span[contains(@class, 'bibtex-title')]
    ${titles}=  Create List
    FOR  ${element}  IN  @{elements}
        ${text}=  Get Text  ${element}
        Append To List  ${titles}  ${text}
    END
    Log Many  ${titles}
    Should Be Equal  ${titles[0]}  Second reference edited again
    Should Be Equal  ${titles[1]}  First reference edited again
    Should Be Equal  ${titles[2]}  Third reference edited again

User can sort references by year
    Go To  ${HOME_URL}
    Click Link  Create article
    Input Text  title  b
    Input Text  author  First Author
    Input Text  journal  Journal 1
    Input Text  year  2023
    Click Button  Create
    Go To  ${HOME_URL}
    Click Link  Create article
    Input Text  title  a
    Input Text  author  Second Author
    Input Text  journal  Journal 2
    Input Text  year  2023
    Click Button  Create
    Go To  ${HOME_URL}
    Click Link  Create article
    Input Text  title  c
    Input Text  author  Third Author
    Input Text  journal  Journal 3
    Input Text  year  2010
    Click Button  Create

    # Sort by earliest modified
    Go To  ${HOME_URL}
    Select From List By Label    id=sort-options    Year (oldest first)
    Sleep  1s

    # Verify the order
    ${elements}=  Get WebElements  xpath=//li[contains(@class, 'bibtex-item')]//span[contains(@class, 'bibtex-title')]
    ${titles}=  Create List
    FOR  ${element}  IN  @{elements}
        ${text}=  Get Text  ${element}
        Append To List  ${titles}  ${text}
    END
    Log Many  ${titles}
    Should Be Equal  ${titles[0]}  c
    Should Be Equal  ${titles[1]}  a
    Should Be Equal  ${titles[2]}  b

User can sort references by year in reversed order
    Go To  ${HOME_URL}
    Click Link  Create article
    Input Text  title  b
    Input Text  author  First Author
    Input Text  journal  Journal 1
    Input Text  year  2023
    Click Button  Create
    Go To  ${HOME_URL}
    Click Link  Create article
    Input Text  title  a
    Input Text  author  Second Author
    Input Text  journal  Journal 2
    Input Text  year  2023
    Click Button  Create
    Go To  ${HOME_URL}
    Click Link  Create article
    Input Text  title  c
    Input Text  author  Third Author
    Input Text  journal  Journal 3
    Input Text  year  2010
    Click Button  Create

    # Sort by earliest modified
    Go To  ${HOME_URL}
    Select From List By Label    id=sort-options    Year (newest first)
    Sleep  1s

    # Verify the order
    ${elements}=  Get WebElements  xpath=//li[contains(@class, 'bibtex-item')]//span[contains(@class, 'bibtex-title')]
    ${titles}=  Create List
    FOR  ${element}  IN  @{elements}
        ${text}=  Get Text  ${element}
        Append To List  ${titles}  ${text}
    END
    Log Many  ${titles}
    Should Be Equal  ${titles[0]}  a
    Should Be Equal  ${titles[1]}  b
    Should Be Equal  ${titles[2]}  c