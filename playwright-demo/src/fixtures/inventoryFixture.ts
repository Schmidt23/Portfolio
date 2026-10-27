import { test as base } from '@playwright/test';
import type { Page } from '@playwright/test';
import { InventoryPage } from '../../src/pages/InventoryPage';
import { UserFlows } from "../../src/flows/UserFlow";
import { Urls } from '../../src/constants/urls';


type Fixtures = {
  inventoryPage: InventoryPage; 
};

export const test = base.extend<Fixtures>({
  inventoryPage: async ({ page }, use) => {
    const flow = new UserFlows(page);
    await flow.loginFlow(process.env.USER_NAME!, process.env.PASSWORD!);
    await page.goto(Urls.inventory);
    const inventoryPage = new InventoryPage(page);
    await inventoryPage.waitUntilReady();
    await use(inventoryPage);
  },
});

export { expect } from '@playwright/test';
