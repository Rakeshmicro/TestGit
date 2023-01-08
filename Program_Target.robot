*** Settings ***
Documentation       This is to program a device with mdb.

Library             RPA.Desktop
Library             ./PythonSource/mdbsetup.py
#Library             mdbsetup.py
Library             Dialogs

*** Variables ***

${device}    ATSAML21J18B
${tool}    edbg
${tool_SN}    ATML2241040200002638
${hex_file}    C:/EDrive/VSCODE/MDB/MDB_SAML21.X.production.hex
${Prog_Tar}

*** Keywords ***
# Program Target
#     Call mdb    ${device}   ${tool}    ${tool_SN}    ${hex_file}
#     #Should Be True    ${Prog_Tar} "Programming Successful"
#     Sleep    5s    

*** Tasks ***
Open and Setup mdb
    ${Prog_Tar}=    Call mdb    ATSAML21J18B   edbg    ATML2241040200002638    C:/EDrive/VSCODE/MDB/MDB_SAML21.X.production.hex
    Should Be True    ${Prog_Tar}    "Programming Successful"
    