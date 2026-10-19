import { Page } from '@playwright/test';
import { BasePage } from './BasePage';
import {LoginLocators} from "../locators/login.locators";
import { InventoryLocators } from '../locators/inventory.locators';
import * as Constants from '../../src/constants'

export class LoginPage extends BasePage {

    constructor(page: Page) {
        super(page);
    }
    async goto(){
        await this.page.goto(Constants.Urls.base);
    }

    async login(username: string, password: string ) {
        await this.page.getByRole(LoginLocators.usernameInput.role, {
            name: LoginLocators.usernameInput.name}).fill(username);
        
        await this.page.getByRole(LoginLocators.passwordInput.role, {
            name: LoginLocators.passwordInput.name}).fill(password);

        await this.page.getByRole(LoginLocators.loginButton.role, {
            name: LoginLocators.loginButton.name}).click();
    }

    async getErrorMessage() {
        return await this.page.locator(LoginLocators.errorMessage).innerText();
    }

    async isLoggedIn(){
        return await this.page.locator(InventoryLocators.inventoryContainer).isVisible();
    }
}