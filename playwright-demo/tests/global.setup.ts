import { test as setup } from '@playwright/test';
import { ensureValidAuthState } from '../src/utils/authState';

setup('placeholder setup', async ({ browser}, testInfo) => {
  console.log('Running setup...');
  console.log(
    'SETUP PROJECT:',
    testInfo.project.name
  );
  //do not run for
  if (testInfo.project.name === 'showcase') {
        return;
    }
  //set auth cookie. Other tests should only ensure cookie is still valid -> no parallel auth setting
  await ensureValidAuthState(browser)
});