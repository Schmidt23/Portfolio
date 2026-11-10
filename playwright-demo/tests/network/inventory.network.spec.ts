import { test, expect } from '../../src/fixtures/inventoryFixture';
import { ensureValidAuthState } from '../../src/utils/authState';
import { Urls } from '../../src/constants/urls';
import * as Locators from '../../src/locators';

test.beforeAll(async ({ browser }) => {
    await ensureValidAuthState(browser);
});

//use logged in state. Great time saver.
test.use({
  storageState: 'playwright/.auth/user.json',
});


test.describe('@network Image loading', () => {

    test('all product images return 200', async ({ page }) => {

        await page.goto(Urls.inventory);

        const images = await page.locator(Locators.InventoryLocators.productImages);
        await expect(images.first()).toBeVisible();

        const imageUrls = await images.evaluateAll(elements =>
                elements.map(
                    element => (element as HTMLImageElement).src
                )
            );
        
        expect(imageUrls.length).toBeGreaterThan(0);
        
        for (const imageUrl of imageUrls) {

            const response = await page.request.get(imageUrl);

            expect(
                response.status(),
                `Image failed: ${imageUrl}`
            ).toBe(200);
        }

    });
});