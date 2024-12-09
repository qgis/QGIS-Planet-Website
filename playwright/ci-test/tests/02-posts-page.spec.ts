import { test as base, expect } from "@playwright/test";
import { Sidebar } from "./fixtures/sidebar";
// import { PostsPage } from "./fixtures/posts-page";
import { HomePage } from "./fixtures/home-page";

type PostsPageFixtures = {
    homePage: HomePage;
    sidebar: Sidebar;
    // postsPage: PostsPage;
};

const test = base.extend<PostsPageFixtures>({
    homePage: async ({ page }, use) => {
        const homePage = new HomePage(page);
        await use(homePage);
    },
    sidebar: async ({ page }, use) => {
        const sidebar = new Sidebar(page);
        await use(sidebar);
    },
    // postsPage: async ({ page }, use) => {
    //     const postsPage = new PostsPage(page);
    //     await use(postsPage);
    // },
});

test("Posts page", async ({ homePage, sidebar }) => {
    await homePage.goto();
    await homePage.startReadingLink.click();
    await expect(sidebar.homeLink).toBeVisible();
    await expect(sidebar.allPostsLink).toBeVisible();
    await expect(sidebar.subscribersLink).toBeVisible();
    await expect(sidebar.tagsLink).toBeVisible();
});
