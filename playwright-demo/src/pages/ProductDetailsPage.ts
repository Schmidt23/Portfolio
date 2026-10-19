import { Page } from '@playwright/test';
import { BasePage } from './BasePage';
import { ProductDetailLocators } from '../locators/productDetail.locators';

export class ProductDetailsPage extends BasePage {

    constructor(page: Page) {
        super(page)
    }

    async isLoaded() {
        return await this.page.getByRole(ProductDetailLocators.backToProductsButton.role,
            {name: ProductDetailLocators.backToProductsButton.name} 
        ).isVisible();
    }

    async backToProducts() {
        await this.page.getByRole(ProductDetailLocators.backToProductsButton.role,
            {name: ProductDetailLocators.backToProductsButton.name}).click();
    }
    
    async addToCart() {
        await this.page.getByRole(ProductDetailLocators.addToCartButton.role,
            {name: ProductDetailLocators.addToCartButton.name}).click();
    }

    async removeFromCart() {
        await this.page.getByRole(ProductDetailLocators.removeFromCartButton.role,
            {name: ProductDetailLocators.removeFromCartButton.name}).click();
    }

    async getPrice() {
        return await this.page.locator(ProductDetailLocators.price).innerText();
    }
    
    async getDescription() {
        return await this.page.locator(ProductDetailLocators.description).innerText();
    }

    async getTitle() {
        return await this.page.locator(ProductDetailLocators.title).innerText();
    }
}