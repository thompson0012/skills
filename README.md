# Skills

個人 skill 與筆記的集中地。每個目錄一件事，不互相混合。

## 內容

| 路徑 | 類型 | 說明 |
|---|---|---|
| [prompt-translator/](prompt-translator/) | skill | 從模糊或口語需求產出可直接使用的全新 Prompt、System Prompt、Agent 指令模板與 Sub-agent 委派簡報（含 `Light` 快速通道、靜態快取前綴／動態 `{{變數槽}}` 分離與 `Fresh／Forked` 簡報）。 |
| [prompt-auditor/](prompt-auditor/) | skill | 審核、診斷、改寫與換代瘦身既有的 Prompt、Skill 或 SOP（依 `SPEC 契約／COMP 補償／STALE／DEBT／DUP／CONFLICT` 逐項歸屬，預設存疑保留，附改寫稿與前後差異）。 |


## Skill 結構

```
<skill-name>/
├── SKILL.md              # 入口：frontmatter（name、description）+ 工作流程
├── references/           # 需要時才讀的詳細資料，按需漸進載入
└── evals/                # 選配：L1 回歸測試集（evals.json）
```

`SKILL.md` 的 `description` 決定何時觸發，所以要寫出使用者會講的話，而不是功能列表。細節放 `references/`，避免主檔膨脹。

## 慣例

- 一個目錄一個職責。有兩種不相容的輸入介面（例如「從需求產出」與「審核既有成品」）就分成兩個，不要用「模式」硬塞。
- 文件夾需要 3 處以上「這種情況除外」，表示抽屜錯了，應該拆。
- 低頻、一次性的事寫成可複製的短指令，不要固化成 skill。
- 筆記與 skill 分開放，不混。

## 版控

```
git log --oneline
```

`.DS_Store` 已由 `.gitignore` 排除。
