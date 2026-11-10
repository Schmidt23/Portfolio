import { test, expect } from '../../src/fixtures/flowFixture';
import { Urls } from '../../src/constants/urls';
import * as Locators from '../../src/locators';

import * as Constants from '../../src/constants'


test.describe('@mock Mock Products', () => {
    test.beforeEach(async ({ userFlows }) => {
        await userFlows.loginFlow(
            process.env.USER_NAME!,
            process.env.PASSWORD!
        );
    });

    test('create baseline screen-shot', async({page}) =>{
        await page.goto(Urls.inventory);
        await expect(page).toHaveScreenshot(
        'inventory-baseline.png'
        );
    });

    test('mocked products are rendered', async ({ page }) => {
        await page.goto(Urls.inventory);

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

    test('mocked page differs from baseline', async ({ page }) => {
        test.fail();
        await page.goto(Urls.inventory);

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
        
        await expect(page).toHaveScreenshot(
            'inventory-baseline.png'
        );

    });
});