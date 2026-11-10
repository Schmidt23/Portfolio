import { test, expect } from '../src/fixtures/inventoryFixture';
import { ensureValidAuthState } from '../src/utils/authState';

test.beforeAll(async ({ browser }) => {
    await ensureValidAuthState(browser);
});

//use logged in state. Great time saver.
test.use({
  storageState: 'playwright/.auth/user.json',
});

test.describe('@sort Inventory Sorting', () => {

    test('sort by Price: Low to High', async ({ inventoryPage }) => {
        await inventoryPage.sortBy('Price (low to high)');

        const prices = await inventoryPage.getPrices()
        const numeric = prices.map(p => parseFloat(p.replace('$', '')));
        const sorted = [...numeric].sort((a, b) => a - b); //spread syntax [...<name>] copies original

        expect(numeric).toEqual(sorted);
    });

    test('sort by Price: High to Low', async ({ inventoryPage }) => {
        await inventoryPage.sortBy('Price (high to low)');

        const prices = await inventoryPage.getPrices()
        const numeric = prices.map(p => parseFloat(p.replace('$', '')));
        const sorted = [...numeric].sort((a, b) => b - a);

        expect(numeric).toEqual(sorted);
    });


    test('sort by Name: A to Z', async ({ inventoryPage }) => {
        await inventoryPage.sortBy('Name (A to Z)');

        const names = await inventoryPage.getNames()
        const sorted = [...names].sort();

        expect(names).toEqual(sorted);
    });


    test('sort by Name: Z to A', async ({ inventoryPage }) => {
        await inventoryPage.sortBy('Name (Z to A)');

        const names = await inventoryPage.getNames()
        const sorted = [...names].sort().reverse();

        expect(names).toEqual(sorted);
    });

});
