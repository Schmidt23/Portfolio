import { test as base } from '@playwright/test';
import { UserFlows } from '../flows/UserFlow';

type Fixtures = {
    userFlows: UserFlows;
}

export const test = base.extend<Fixtures>({
    userFlows: async( { page }, use ) => {
        await use(
            new UserFlows(page)
        );
    },
});

export { expect } from '@playwright/test';