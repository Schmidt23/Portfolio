import { test, expect } from '@playwright/test';

const URL = 'https://demoqa.com';

test.describe('@showcase UI Elements', () => {


    test('checkboxes', async ({ page }) => {
        await page.goto(`${URL}/checkbox`);

        const homeNode = page.locator(
            '[role="treeitem"]',
            { hasText: 'Home' }
        );

        await homeNode
            .locator('.rc-tree-switcher')
            .click();

        await page.getByRole('checkbox', {name: 'Select Desktop'}).click();

        await expect(
            page.locator('#result .text-success')
        ).toContainText([
            'desktop',
            'notes',
            'commands'
        ]);
    });

    test('radio buttons', async ({ page }) => {
        await page.goto(`${URL}/radio-button`);

        await page.getByRole('radio', {name: 'Yes'}).click();
        
        await expect(
        page.locator('.text-success')
        ).toHaveText('Yes');
    });

    test('drag and drop', async ({ page }) => {

        await page.goto(`${URL}/droppable`);
        const dropTarget = page
            .getByRole('tabpanel', { name: 'Simple' })
            .locator('#droppable');

        await page
            .locator('#draggable')
            .dragTo(dropTarget);

        await expect(
            dropTarget
        ).toContainText('Dropped!');
    });
});