export const productDetailLocators = {
    title: '[data-test="inventory-item-name"]',
    description: '[data-test="inventory-item-desc"]',
    price: '[data-test="inventory-item-price"]',
    addToCartButton: { role: 'button', name: 'Add to cart' },
    removeFromCartButton: { role: 'button', name: 'Remove' },
    backToProductsButton: { role: 'button', name: 'Back to products' }
} as const;