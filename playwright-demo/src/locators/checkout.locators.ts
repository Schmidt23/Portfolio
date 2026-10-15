export const CheckoutLocators = {
    //step 1
    firstNameInput: '[data-test="firstName"]',
    lastNameInput: '[data-test="lastName"]',
    postalCodeInput: '[data-test="postalCode"]',
    continueButton: { role: 'button', name: 'Continue' },
    cancelButton: { role: 'button', name: 'Cancel' },
    errorMessage: '[data-test="error"]',
    //step 2
    overviewItem: '.cart_item',
    finishButton: { role: 'button', name: 'Finish' },
    summaryTotal: '.summary_total_label',
    //confirmation
    confirmationMessage: '.complete-text',
    backHomeButton: { role: 'button', name: 'Back Home' }
} as const; 