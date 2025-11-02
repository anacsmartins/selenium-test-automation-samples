# Test Case: AUTH-TC-001 – Login with Valid Credentials

## Section
Authentication

## Priority
High

## Type
Functional Test

## Automation Status
Automated (Selenium)

## Pre-conditions
- Valid user exists in the database
- User account is active
- Browser opens Login page successfully

## Steps
1. Enter a valid username in the Username field  
2. Enter the correct password in the Password field  
3. Click the "Sign In" button

## Expected Result
- User is successfully redirected to the Dashboard page  
- Dashboard header displays the text "Welcome"  
- HTTP Status code of the landing page is 200

## Post-conditions
- User is authenticated  
- Session token / JWT generated

## Linked Requirements
- AUTH-REQ-001  
- AUTH-REQ-002

## Automation Reference
`tests/test_login_valid.py::test_login_valid_credentials`
