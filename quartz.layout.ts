import { PageLayout, SharedLayout } from "./quartz/cfg"
import * as Component from "./quartz/components"
import { FileTrieNode } from "./quartz/util/fileTrie"

// 自定義 Explorer 排序：按照指定順序排列資料夾
// 注意：sortFn 會被序列化成字串傳到前端，所以必須是自包含函式（不能引用外部變數）
function customSortFn(a: FileTrieNode, b: FileTrieNode): number {
  // 定義排序順序（必須內嵌，不能引用外部常數）
  const folderOrder: Record<string, number> = {
    "技術分析": 1,
    "基本面分析": 2,
    "籌碼面分析": 3,
    "操作策略": 4,
    "風險管理": 5,
    "YouTube頻道": 6,
    "每日分析": 7,
  }
  // 如果兩邊都是資料夾或都是檔案，按自定義順序/字母排序
  if ((!a.isFolder && !b.isFolder) || (a.isFolder && b.isFolder)) {
    const aOrder = folderOrder[a.displayName] ?? 999
    const bOrder = folderOrder[b.displayName] ?? 999
    if (aOrder !== bOrder) return aOrder - bOrder
    // 不在自定義順序中，按字母排
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
      "📊 產業地圖": "https://allen-hsu1116.github.io/industry-map-site/",
      "📈 每日報告": "https://allen-hsu1116.github.io/industry-map-site/daily-report",
      "🧠 AI 選股": "https://allen-hsu1116.github.io/knowledge-base/專案/應用/ZhuLinsen-daily_stock_analysis",
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