import { test, expect } from '@playwright/test';
import { Urls } from '../../src/constants/urls';
import { UserFlows } from '../../src/flows/UserFlow';


test.describe('Performance Metrics', () => {

    test('Inventory page baseline performance', async ({ page }) => {
        const flow = new UserFlows(page);
        await flow.loginFlow(process.env.USER_NAME!, process.env.PASSWORD!)

        await page.goto(Urls.inventory);


        // Browser metrics
        const prfrmnc = await page.evaluate(() => {
            const navigation = performance.getEntriesByType('navigation')[0] as PerformanceNavigationTiming;

            const resources = performance.getEntriesByType('resource') 
                .map(res => {
                    const r = res as PerformanceResourceTiming;
                    return {
                    name: r.name.substring(0,100),
                    fetchStart: r.fetchStart,
                    responseEnd: r.responseEnd,
                    duration: r.responseEnd - r.fetchStart,
                    size: r.transferSize,
                    };
                });
            
            return {
                Navigation: {
                    startTime: navigation.startTime,
                    duration: navigation.duration - navigation.startTime,
                    domComplete: navigation.domComplete - navigation.startTime,
                    loadEventEnd: navigation.loadEventEnd - navigation.startTime,
                },

                Resources: resources
            };
        })
        console.log("Navigation");
        console.log(prfrmnc["Navigation"]);
        console.log("Resources");
        console.log(prfrmnc["Resources"]);
    });
});
