import { test, expect } from '@playwright/test';
import { UserFlows } from '../../src/flows/UserFlow';
import * as Locators from '../../src/locators';

import * as Constants from '../../src/constants'

test.describe('Mock Products', () => {
    test.beforeEach(async ({ page }) => {
        const flow = new UserFlows(page);
        await flow.loginFlow(process.env.USER_NAME!, process.env.PASSWORD!)
    });

    test('mocked products are rendered', async ({ page }) => {
        await expect(page.locator(Locators.InventoryLocators.inventoryContainer)).toBeVisible();

        await page.route('**/assets/index-*.js', async route => {
        const original = await route.fetch(); //fetch instead of response for assets, else blocked
        const text = await original.text();

        const modified = text.replace('Sauce Labs Backpack', 'Mocked Backpack');

        await route.fulfill({
            status: 200,
            contentType: 'application/javascript',
            body: modified,
        });
        
    });

    await page.goto(Constants.Urls.inventory);
    await expect(
        page.locator(Locators.InventoryLocators.itemNameText, { hasText: 'Mocked Backpack' })
    ).toBeVisible();

    });
});