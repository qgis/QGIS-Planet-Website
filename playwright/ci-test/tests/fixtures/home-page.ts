import type { Page, Locator, expect } from "@playwright/test";

export class HomePage {
    private readonly url: string = "/";
    public readonly pageBody: Locator;
    public readonly freeOpenSourceSpatialDiv: Locator;
    public readonly startReadingLink: Locator;
    public readonly qgisSupportersHeading: Locator;
    public readonly supportersGridDiv: Locator;
    public readonly addYourLogoHereText: Locator;
    public readonly silverPartnerText: Locator;
    public readonly otherSupporters: Locator;

    public readonly textList: string[] = [
        "Free and Open Source",
        "QGIS Planet",
        "Your go-to source for the latest posts and updates related to QGIS",
    ];

    constructor(public readonly page: Page) {
        this.pageBody = this.page.locator("body");
        this.freeOpenSourceSpatialDiv = this.page
            .locator("div")
            .filter({ hasText: "Free and open source" })
            .first();
        this.startReadingLink = this.page
            .locator("section")
            .filter({ hasText: "Free and open source" })
            .getByRole("link");
        this.qgisSupportersHeading = this.page.getByRole("heading", {
            name: "QGIS sustaining members",
        });
        this.addYourLogoHereText = this.page
            .locator("div")
            .filter({ hasText: "Add your logo here?" })
            .nth(2);
        this.silverPartnerText = this.page
            .locator("div")
            .filter({ hasText: "Large membership" })
            .nth(2);
        this.supportersGridDiv = this.page
            .locator(".supporters-grid > div:nth-child(3)")
            .first();
        this.otherSupporters = this.page
            .locator(".container > div:nth-child(3)")
            .first();
    }

    async goto() {
        await this.page.goto(this.url);
    }
}
