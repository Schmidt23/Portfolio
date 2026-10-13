export const InventoryLocators = {
    inventoryContainer: '[data-test="inventory-container"]',
    itemName: { role: 'link', name: '' },
    itemPrice: '[data-test="inventory-item-price"]',
    addToCartButton: { role: 'button', name: '' },
    removeFromCartButton: { role: 'button', name: 'Remove' },
    cartBadge: '[data-test="shopping-cart-badge"]',
    sortDropdown: { role: 'combobox', name: 'product_sort_container' }
} as const;