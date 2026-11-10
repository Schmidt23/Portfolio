import { test, expect } from "@playwright/test";
import { UserFlows } from "../src/flows/UserFlow";

test('@flow Full purchase flow', async ({ page }) => {
    const flows = new UserFlows(page);

    await flows.fullPurchaseFlow('Sauce Labs Backpack', {
        firstName: process.env.FIRST_NAME!,
        lastName: process.env.LAST_NAME!,
        postalCode: process.env.POSTAL_CODE!
    });

    expect(await page.locator('.inventory_list').isVisible()).toBeTruthy();
});