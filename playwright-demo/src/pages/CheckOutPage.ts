import { Page } from "@playwright/test";
import { BasePage } from "./BasePage";
import { CheckoutLocators } from "../locators/checkout.locators";

export class CheckoutPage extends BasePage {

    constructor(page: Page) {
        super(page)
    }

    async isLoaded() {
        return await this.page.getByRole(CheckoutLocators.continueButton.role,
            {name: CheckoutLocators.continueButton.name}
        ).isVisible();
    }

    async fillCustomerInfo(firstName: string, lastName: string, postalCode: string) {
        await this.page.locator(CheckoutLocators.firstNameInput).fill(firstName);
        await this.page.locator(CheckoutLocators.lastNameInput).fill(lastName);
        await this.page.locator(CheckoutLocators.postalCodeInput).fill(postalCode);
    }
    
    async continue() {
        await this.page.getByRole(
            CheckoutLocators.continueButton.role,
            { name: CheckoutLocators.continueButton.name }
        ).click();

    }

    async cancel() {
        await this.page.getByRole(
            CheckoutLocators.cancelButton.role,
            { name: CheckoutLocators.cancelButton.name }
        ).click();
    }

    async getErroMessage() {
        return await this.page.locator(CheckoutLocators.errorMessage).innerText();
    }
    
    async isLoadedStepTwo() {
        return await this.page.getByRole(
            CheckoutLocators.finishButton.role,
            { name: CheckoutLocators.finishButton.name }
        ).isVisible();
    }

    async getOverviewItems() {
        return await this.page.locator(CheckoutLocators.overviewItem).all();
    }

    async getTotal() {
        return await this.page.locator(CheckoutLocators.summaryTotal).innerText();
    }    

    async finish() {
        await this.page.getByRole(
            CheckoutLocators.finishButton.role,
            { name: CheckoutLocators.finishButton.name }
        ).click();
    }

    async isLoadedConfirmation() {
        return await this.page.locator(CheckoutLocators.confirmationMessage).isVisible();
    }

    async getConfirmationMessage() {
        return await this.page.locator(CheckoutLocators.confirmationMessage).innerText();
    }

    async backHome() {
        await this.page.getByRole(
            CheckoutLocators.backHomeButton.role,
            { name: CheckoutLocators.backHomeButton.name }
        ).click();
    }
}