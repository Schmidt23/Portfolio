import { Page } from '@playwright/test';
import { BasePage } from './BasePage';
import {LoginLocators} from "../locators/login.locators";
import { InventoryLocators } from '../locators/inventory.locators';

export class LoginPage extends BasePage {

    constructor(page: Page) {
        super(page);
    }
    async goto(){
        await this.page.goto('https://www.saucedemo.com/');
    }

    async login(username: string, password: string ) {
        await this.page.getByRole(LoginLocators.usernameInput.role, {
            name: LoginLocators.usernameInput.name}).fill(username);
        
        await this.page.getByRole(LoginLocators.passwordInput.role, {
            name: LoginLocators.passwordInput.name}).fill(password);

        await this.page.getByRole(LoginLocators.loginButton.role, {
            name: LoginLocators.loginButton.name}).click();
    }

    async assertLoginError() {
        await this.page.locator(LoginLocators.errorMessage).isVisible();
    }

    async isLoggedIn(){
        return await this.page.locator(InventoryLocators.inventoryContainer).isVisible();
    }
}