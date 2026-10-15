export const CartLocators = {
    cartItem: '.cart_item',
    itemName: '[data-test="inventory-item-name"]',
    itemPrice: '[data-test="inventory-item-price"]',
    removeButton: { role: 'button', name: 'Remove' },
    continueShoppingButton: { role: 'button', name: 'Continue Shopping' },
    checkoutButton: { role: 'button', name: 'Checkout' }
} as const;