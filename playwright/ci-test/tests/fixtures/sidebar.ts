import type { Page, Locator } from "@playwright/test";

export class Sidebar {
    public readonly sidebar: Locator;
    public readonly homeLink: Locator;
    public readonly allPostsLink: Locator;
    public readonly subscribersLink: Locator;
    public readonly tagsLink: Locator;

    constructor(public readonly page: Page) {
        this.sidebar = this.page.locator("#sidebar");
        this.homeLink = this.sidebar.getByRole("link", {
            name: " Home",
        });
        this.allPostsLink = this.sidebar.getByRole("link", {
            name: " All Posts",
        });
        this.subscribersLink = this.sidebar.locator('a')
        .filter({ hasText: 'Feeds' });

        this.tagsLink = this.sidebar.getByRole("button", {
            name: " Tags",
        });
    }
}
