import { test, expect } from '@playwright/test';
import { LoginPage } from '../src/pages/LoginPage';
import { InventoryPage } from '../src/pages/InventoryPage';
import { UserFlows } from '../src/flows/UserFlow';
import * as Locators from '../src/locators';

//basic version
test('basic @login works', async ({ page }) => {
    const loginPage = new LoginPage(page);
    const inventoryPage = new InventoryPage(page);

    await loginPage.goto();
    await loginPage.login('standard_user', 'secret_sauce');

    // simple check: inventory page loaded
    const loaded = await inventoryPage.isLoaded();
    expect(loaded).toBeTruthy();
});

//UserFlow
test('@login works (UserFlow)', async ({ page }) => {
    const flows = new UserFlows(page);

    await flows.loginFlow(process.env.USER_NAME!, process.env.PASSWORD!);

    await expect(page.locator(Locators.InventoryLocators.inventoryContainer)).toBeVisible();
});


//DDT
const loginData = [
    {
        username: process.env.USER_NAME!,
        password: process.env.PASSWORD!,
        expected: 'success',
        description: 'valid user'
    },
    {
        username: '',
        password: 'secret_sauce',
        expected: 'Epic sadface: Username is required',
        description: 'no username'
    },
    {
        username: 'standard_user',
        password: '',
        expected: 'Epic sadface: Password is required',
        description: 'no password'
    },
    {
        username: 'locked_out_user',
        password: 'secret_sauce',
        expected: 'Epic sadface: Sorry, this user has been locked out.',
        description: 'locked out user'
    },
    {
        username: 'invalid',
        password: 'invalid',
        expected: 'Epic sadface: Username and password do not match any user in this service',
        description: 'invalid credentials'
    }
];

test.describe('@login Login DDT', () =>{

    for (const data of loginData){

        test(`(${data.description})`, async ( {page}) => {
            const loginPage = new LoginPage(page);
            const inventoryPage = new InventoryPage(page);

            await loginPage.goto();
            await loginPage.login(data.username, data.password);

            if (data.expected === "success"){
                expect(await inventoryPage.isLoaded()).toBeTruthy();
            } else {
                const error = await loginPage.getErrorMessage();
                expect(error.toLowerCase()).toContain(data.expected.toLowerCase());
            }
        })
    }

});
