import { test as setup } from '@playwright/test';
import { ensureValidAuthState } from '../src/utils/authState';

setup('placeholder setup', async ({ browser}) => {
  console.log('Running setup...');
  //set auth cookie. Other tests should only ensure cookie is still valid -> no parallel auth setting
  await ensureValidAuthState(browser)
});