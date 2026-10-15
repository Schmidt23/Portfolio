import { Page } from '@playwright/test';
import { BasePage } from './BasePage';
import { productDetailLocators } from '../locators/productDetail.locators';

export class ProductDetailsPage extends BasePage {

    constructor(page: Page) {
        super(page)
    }

    async isLoaded() {
        return await this.page.getByRole(productDetailLocators.backToProductsButton.role,
            {name: productDetailLocators.backToProductsButton.name} 
        ).isVisible();
    }

    async backToProducts() {
        await this.page.getByRole(productDetailLocators.backToProductsButton.role,
            {name: productDetailLocators.backToProductsButton.name}).click();
    }
    
    async addToCart() {
        await this.page.getByRole(productDetailLocators.addToCartButton.role,
            {name: productDetailLocators.addToCartButton.name}).click();
    }

    async removeFromCart() {
        await this.page.getByRole(productDetailLocators.removeFromCartButton.role,
            {name: productDetailLocators.removeFromCartButton.name}).click();
    }

    async getPrice() {
        return await this.page.locator(productDetailLocators.price).innerText();
    }
    
    async getDescription() {
        return await this.page.locator(productDetailLocators.description).innerText();
    }

    async getTitle() {
        return await this.page.locator(productDetailLocators.title).innerText();
    }
}