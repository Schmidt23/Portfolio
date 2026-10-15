import { Page } from '@playwright/test';
import { LoginPage } from '../pages/LoginPage';
import { InventoryPage } from '../pages/InventoryPage';
import { ProductDetailsPage } from '../pages/ProductDetailsPage';
import { CartPage } from '../pages/CartPage';
import { CheckoutPage } from '../pages/CheckoutPage';

export class UserFlows {
    private loginPage: LoginPage;
    private inventoryPage: InventoryPage;
    private detailsPage: ProductDetailsPage;
    private cartPage: CartPage;
    private checkoutPage: CheckoutPage;

    constructor(page: Page) {
        this.loginPage = new LoginPage(page);
        this.inventoryPage = new InventoryPage(page);
        this.detailsPage = new ProductDetailsPage(page);
        this.cartPage = new CartPage(page);
        this.checkoutPage = new CheckoutPage(page);
    }

    async loginFlow(username: string, password: string) {
        await this.loginPage.goto();
        await this.loginPage.login(username, password);
        await this.inventoryPage.isLoaded();
    }

    async addItemToCartFlow(itemName: string) {
        await this.inventoryPage.openItemDetails(itemName)
        await this.detailsPage.isLoaded()
        await this.detailsPage.addToCart();
        await this.detailsPage.backToProducts();
        await this.inventoryPage.openCart();
    }

    async checkoutFlow(customerData: { firstName: string; lastName: string; postalCode: string }) {
        await this.cartPage.checkout();

        await this.checkoutPage.fillCustomerInfo(
            customerData.firstName,
            customerData.lastName,
            customerData.postalCode
        );

        await this.checkoutPage.continue();
        await this.checkoutPage.finish();
        await this.checkoutPage.backHome();
        await this.inventoryPage.isLoaded();
    }

    async fullPurchaseFlow(itemName: string, customerData: { firstName: string; lastName: string; postalCode: string }) {
        await this.loginFlow(process.env.USER_NAME!, process.env.PASSWORD!);
        await this.addItemToCartFlow(itemName);
        await this.checkoutFlow(customerData);
    }
}