export const LoginLocators = {
    usernameInput: { role: 'textbox', name: 'Username' },
    passwordInput: { role: 'textbox', name: 'Password' },
    loginButton: { role: 'button', name: 'Login' },
    errorMessage: '[data-test="error"]'
} as const;