import { Page } from '@playwright/test';
import { BasePage } from './BasePage';
import { CartLocators } from '../locators/cart.locators'

export class CartPage extends BasePage {

    constructor(page: Page) {
        super(page)
    }

    private getItem(itemName: string) {
       return this.page.locator(CartLocators.cartItem).filter({
        has: this.page.locator(CartLocators.itemName, { hasText: itemName })
    });
}
    async goto(){
        await this.page.goto('https://www.saucedemo.com/cart.html');
    }

    async isLoaded(){
        return await this.page.getByRole(CartLocators.checkoutButton.role,
            {name: CartLocators.checkoutButton.name}).isVisible();
    }

    async continueShopping() {
        await this.page.getByRole(CartLocators.continueShoppingButton.role,
            {name: CartLocators.continueShoppingButton.name}).click();
    }
    
    async checkout() {
        await this.page.getByRole(CartLocators.checkoutButton.role,
        {name: CartLocators.checkoutButton.name}).click();
    }

    async removeItem(itemName: string) {
        const item = this.getItem(itemName);
        await item.getByRole(CartLocators.removeButton.role, 
        {name: CartLocators.removeButton.name}).click();
    }

    async getItems() {
        return await this.page.locator(CartLocators.cartItem).all();
    }

    async getItemNames() {
        return await this.page.locator(CartLocators.cartItem)
        .locator(CartLocators.itemName)
        .allInnerTexts();
    }

    async getItemPrices() {
        return await this.page.locator(CartLocators.cartItem)
        .locator(CartLocators.itemPrice)
        .allInnerTexts();
    }
}