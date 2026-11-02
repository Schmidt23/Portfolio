import fs from 'fs';
import type { Browser } from '@playwright/test';
import { UserFlows } from '../flows/UserFlow';

const AUTH_FILE = 'playwright/.auth/user.json';
const REMAINING_SECONDS = 300;

export function hasValidAuthState(
): boolean {
    if (!fs.existsSync(AUTH_FILE)) {
        return false;
    }

    const state = JSON.parse(
        fs.readFileSync(AUTH_FILE, 'utf-8')
    );

    //less generic but in this case there will only ever be one expires
    const expiry = state.cookies[0]?.expires;

    if (!expiry){
        return false;
    }

    const now = Math.floor(Date.now() / 1000);

    return expiry > now + REMAINING_SECONDS;
    
}

export async function ensureValidAuthState(
    browser: Browser
): Promise<void> {
    if (hasValidAuthState()){
        return;
    }
    console.log("Creating new valid session")
    const page = await browser.newPage();
    const flows = new UserFlows(page);

    await flows.loginFlow(process.env.USER_NAME!, process.env.PASSWORD!);
    

    await page.context().storageState({
        path: AUTH_FILE
    });
    await page.close();
}