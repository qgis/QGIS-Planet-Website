import type { Page, Locator } from "@playwright/test";

export class Footer {
    public readonly banner: Locator;
    private readonly liElement: Locator;
    public readonly projectList: Locator;
    public readonly communityList: Locator;
    public readonly resourcesList: Locator;
    public readonly downloadLink: Locator;
    public readonly logoImage: Locator;
    public readonly facebookLink: Locator;
    public readonly youtubeLink: Locator;
    public readonly mastodonLink: Locator;
    public readonly ghLink: Locator;
    public readonly mailLink: Locator;

    constructor(public readonly page: Page) {
        this.banner = this.page.getByRole("contentinfo");
        this.liElement = this.page.locator("li");
        this.projectList = this.liElement.filter({ hasText: "QGIS Planet"}).first();
        this.communityList = this.liElement.filter({ hasText: "All Posts" });
        this.resourcesList = this.liElement.filter({ hasText: "Tags" });
        this.downloadLink = this.banner
            .locator("div")
            .filter({ hasText: "Download" })
            .nth(2);
        this.logoImage = this.page.getByRole("img", { name: "Logo" }).last();
        this.facebookLink = this.page.getByRole("link", { name: "" });
        this.youtubeLink = this.page.getByRole("link", { name: "" });
        this.mastodonLink = this.page
            .locator("div:nth-child(2) > div:nth-child(2) > a:nth-child(4)")
            .first();
        this.ghLink = this.page.getByRole("link", { name: "" });
        this.mailLink = this.page.getByRole("link", { name: "" });
    }
}
