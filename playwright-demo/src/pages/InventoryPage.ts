import { Page } from '@playwright/test';
import { BasePage } from './BasePage';
import { InventoryLocators } from '../locators/inventory.locators';
import * as Constants from '../../src/constants'

export class InventoryPage extends BasePage {

    constructor(page: Page) {
        super(page)
    }

    async goto(){
        await this.page.goto(Constants.Urls.inventory);   
    }

    private getItem(itemName: string) {
        return this.page.locator(InventoryLocators.inventoryContainer).filter({
            has: this.page.getByRole(
                InventoryLocators.itemName.role,
                { name: itemName }
            )
        });
    }
    
    async addItemToCart(itemName: string) {
        const item = this.getItem(itemName);

        await item.getByRole(
            InventoryLocators.addToCartButton.role,
            { name: InventoryLocators.addToCartButton.name }
        ).click();
    }

    async removeItemFromCart(itemName: string) {
        const item = this.getItem(itemName);

        await item.getByRole(
            InventoryLocators.removeFromCartButton.role,
            { name: InventoryLocators.removeFromCartButton.name }
        ).click();
    }

    async openItemDetails(itemName: string) {
        await this.page.getByRole(
            InventoryLocators.itemName.role,
            { name: itemName }
        ).click();
    }

    async getItemPrice(itemName: string) {
        const item = this.getItem(itemName);
        return await item.locator(InventoryLocators.itemPrice).innerText();
    }

    async getCartCount() {
        const badge = this.page.locator(InventoryLocators.cartBadge);

        if (await badge.isVisible()) {
            return await badge.innerText();
        }

        return '0';
    }
    async isLoaded() {
        await this.page.locator(InventoryLocators.inventoryContainer).first().waitFor();
        return true;
    }
    
    async sortBy(option: string) {
        await this.page.getByRole(
            InventoryLocators.sortDropdown.role,
            { name: InventoryLocators.sortDropdown.name }
        ).selectOption(option);
    }

    async openCart() {
        await this.page.locator(InventoryLocators.cartButton).click();
    }
}