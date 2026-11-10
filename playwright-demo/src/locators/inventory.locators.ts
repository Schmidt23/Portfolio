export const InventoryLocators = {
    inventoryContainer: '[data-test="inventory-container"]',
    productSortContainer: '[data-test="product-sort-container"]',
    itemName: { role: 'img', name: '' },
    itemNameText: '[data-test="inventory-item-name"]',
    itemPrice: '[data-test="inventory-item-price"]',
    addToCartButton: { role: 'button', name: '' },
    removeFromCartButton: { role: 'button', name: 'Remove' },
    cartButton: '.shopping_cart_link',
    cartBadge: '[data-test="shopping-cart-badge"]',
    sortDropdown: { role: 'combobox', name: 'product_sort_container' },
    productImages: '.inventory_item_img img'
} as const;