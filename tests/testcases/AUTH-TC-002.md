# Test Case: AUTH-TC-002 – Logout from authenticated user

## Section
Authentication

## Priority
Medium

## Type
Functional Test

## Automation Status
Automated (Selenium)

## Pre-conditions
- User is already authenticated in the system
- Session token is valid
- User is on Dashboard page

## Steps
1. Click on “Logout” button in the navbar/menu
2. Confirm logout request if prompt appears

## Expected Result
- User is redirected to Login page
- Session is cleared
- Login form fields are visible again

## Post-conditions
- No authenticated session remains active

## Linked Requirements
- AUTH-REQ-003

## Automation Reference
`tests/test_logout.py::test_logout_authenticated_user`
