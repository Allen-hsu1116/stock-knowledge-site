import { PageLayout, SharedLayout } from "./quartz/cfg"
import * as Component from "./quartz/components"
import { FileTrieNode } from "./quartz/util/fileTrie"

// 自定義 Explorer 排序：按照指定順序排列資料夾
const FOLDER_ORDER = [
  "技術分析",
  "基本面分析",
  "籌碼面分析",
  "操作策略",
  "風險管理",
  "YouTube頻道",
  "每日分析",
]

function customSortFn(a: FileTrieNode, b: FileTrieNode): number {
  // 如果兩邊都是資料夾或都是檔案，按自定義順序/字母排序
  if ((!a.isFolder && !b.isFolder) || (a.isFolder && b.isFolder)) {
    const aOrder = FOLDER_ORDER.indexOf(a.displayName)
    const bOrder = FOLDER_ORDER.indexOf(b.displayName)
    // 如果兩邊都在自定義順序中，按自定義順序排
    if (aOrder !== -1 && bOrder !== -1) return aOrder - bOrder
    // 如果只有一邊在自定義順序中，它在前面
    if (aOrder !== -1) return -1
    if (bOrder !== -1) return 1
    // 都不在自定義順序中，按字母排
    return a.displayName.localeCompare(b.displayName, undefined, { numeric: true, sensitivity: "base" })
  }
  // 資料夾排在前面
  if (!a.isFolder && b.isFolder) return 1
  return -1
}

// components shared across all pages
export const sharedPageComponents: SharedLayout = {
  head: Component.Head(),
  header: [],
  afterBody: [],
  footer: Component.Footer({
    links: {
      GitHub: "https://github.com/jackyzha0/quartz",
    },
  }),
}

// components for pages that display a single page (e.g. a single note)
export const defaultContentPageLayout: PageLayout = {
  beforeBody: [
    Component.ConditionalRender({
      component: Component.Breadcrumbs(),
      condition: (page) => page.fileData.slug !== "index",
    }),
    Component.ArticleTitle(),
    Component.ContentMeta(),
    Component.TagList(),
  ],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Flex({
      components: [
        {
          Component: Component.Search(),
          grow: true,
        },
        { Component: Component.Darkmode() },
        { Component: Component.ReaderMode() },
      ],
    }),
    Component.Explorer({ sortFn: customSortFn }),
  ],
  right: [
    Component.Graph(),
    Component.DesktopOnly(Component.TableOfContents()),
    Component.Backlinks(),
  ],
}

// components for pages that display lists of pages  (e.g. tags or folders)
export const defaultListPageLayout: PageLayout = {
  beforeBody: [Component.Breadcrumbs(), Component.ArticleTitle(), Component.ContentMeta()],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Flex({
      components: [
        {
          Component: Component.Search(),
          grow: true,
        },
        { Component: Component.Darkmode() },
      ],
    }),
    Component.Explorer({ sortFn: customSortFn }),
  ],
  right: [],
}