import { test as base } from '@playwright/test';
import { InventoryPage } from '../../src/pages/InventoryPage';



type Fixtures = {
  inventoryPage: InventoryPage; 
};

export const test = base.extend<Fixtures>({
  inventoryPage: async ({ page }, use) => {

    //
    const inventoryPage = new InventoryPage(page);
    await inventoryPage.goto();
    await inventoryPage.waitUntilReady();
    await use(inventoryPage);
  },
});

export { expect } from '@playwright/test';
