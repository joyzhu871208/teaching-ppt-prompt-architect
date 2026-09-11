# Teaching PPT Prompt Architect

一个面向教师的跨平台 Agent Skill：把教材、教案、课程标准或讲义转化为可审阅的教学 PPT 页面蓝图；教师确认后，再生成可直接交给 Gamma、Kimi、豆包、ChatPPT、MindShow 等 AI PPT 工具的完整 Markdown 提示词。

它解决的不是“让 AI 随机生成一套课件”，而是两个更具体的问题：

1. 生成哪些教学要素：文字、图片、问题、任务、互动、检测和素材占位；
2. 怎样组织这些要素：教学顺序、页面布局、信息层级、认知负荷和视觉规范。

## 特点

- 先生成页面蓝图，等待教师回复“通过”或“生成”，再输出完整提示词；
- 支持语文、数学、英语、物理、化学、生物、历史、地理、道法、艺术等学科；
- 默认采用“教材关键素材保留 + AI 辅助生成”的混合素材模式；
- 自动标记需要教师后期上传的教材图片；
- 输出通用 Markdown，兼顾层级型和严格列表型 AI PPT 工具；
- 不绑定模型、API、操作系统或编程语言；
- 不包含脚本，不请求网络、账号或系统权限。

## 仓库结构

```text
teaching-ppt-prompt-architect/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── discipline-adaptation.md
│   └── final-output-format.md
├── examples/
│   └── high-school-biology.md
├── tests/
│   └── validate_structure.py
├── .github/workflows/
│   └── validate.yml
├── LICENSE
└── README.md
```

`SKILL.md` 是跨平台核心；`agents/openai.yaml` 只用于支持该界面元数据的宿主，不影响其他平台；`references/` 由 Agent 在需要时按需读取。

## 快速开始

安装后，可直接提出：

```text
请使用 teaching-ppt-prompt-architect。
根据我上传的教材，为八年级英语阅读课设计一节45分钟课程的教学PPT提示词。
```

第一次输出是教学与页面蓝图。确认后回复：

```text
通过
```

Skill 随后会输出可独立复制给 AI PPT 工具的完整 Markdown 提示词。

## 下载

在 GitHub 仓库页面选择 **Code → Download ZIP**，下载后解压。安装时应保证 `SKILL.md` 位于技能文件夹根目录。

## 平台安装

### OpenAI Codex / ChatGPT desktop

项目级安装：把整个仓库文件夹复制到项目的：

```text
.agents/skills/teaching-ppt-prompt-architect/
```

用户级安装：把整个仓库文件夹复制到：

```text
~/.agents/skills/teaching-ppt-prompt-architect/
```

也可以让 Codex 的 Skill Installer 从本 GitHub 仓库安装。调用时输入：

```text
$teaching-ppt-prompt-architect
```

### OpenClaw

直接从 GitHub 安装：

```bash
openclaw skills install git:YOUR_GITHUB_NAME/teaching-ppt-prompt-architect@main
```

从本地文件夹安装：

```bash
openclaw skills install ./teaching-ppt-prompt-architect --as teaching-ppt-prompt-architect
```

如需所有本地 Agent 共用，在安装命令后添加 `--global`。

### TRAE

项目级安装：把仓库文件夹复制到项目的：

```text
.trae/skills/teaching-ppt-prompt-architect/
```

全局安装：

```text
macOS / Linux: ~/.trae/skills/teaching-ppt-prompt-architect/
Windows: %userprofile%/.trae/skills/teaching-ppt-prompt-architect/
```

安装后，可直接用自然语言提出教学 PPT 提示词任务；TRAE 会根据 `description` 自动匹配该 Skill。

### WorkBuddy

1. 在 GitHub 选择 **Code → Download ZIP**。
2. 解压并检查 `SKILL.md` 位于仓库根目录。
3. 如果 WorkBuddy 要求上传压缩包，将仓库内的全部文件重新压缩，避免 ZIP 外面多套一层目录。
4. 在 WorkBuddy 中打开 **添加技能 → 上传技能**，选择该压缩包。
5. 安装后启用 Skill，在任务中上传教材并提出课程要求。

该 Skill 不含脚本和第三方连接，导入时不需要额外账号或执行权限。

### CodeBuddy Code

项目级目录：

```text
.codebuddy/skills/teaching-ppt-prompt-architect/
```

用户级目录：

```text
~/.codebuddy/skills/teaching-ppt-prompt-architect/
```

### 其他支持 Agent Skills 的工具

把整个仓库文件夹复制到该工具规定的 Skills 目录即可。不要只复制 `SKILL.md`：两个 `references/` 文件承担最终输出格式和学科准确性检查。

## 素材模式

| 模式 | 适合场景 | 处理方式 |
|---|---|---|
| Mode A：AI全生成 | 没有现成素材、视觉准确性要求较低 | AI生成全部可生成视觉，事实性图像标注为示意图 |
| Mode B：教师素材优先 | 教材图、实验图或校本素材必须保留 | 无法嵌入的素材使用明确占位 |
| Mode C：混合素材 | 普通教学课件，默认模式 | 保留承担证据作用的真实素材，AI生成版式和辅助示意 |

统一占位格式：

```text
⚠️【教师必须替换：来源位置＋具体素材名称＋裁切或处理要求】
```

## 常见问题

### 它会直接生成 PPTX 吗？

不会。它先生成高质量、可审阅的教学 PPT 设计和完整提示词，再交给你选择的 AI PPT 工具生成幻灯片。如果需要直接制作 PPTX，应另行调用演示文稿生成能力。

### 没有上传教材可以使用吗？

可以，但必须粘贴足够的教学内容。Skill 不会只根据“第一单元”猜测教材版本和正文。

### 为什么要先确认蓝图？

因为教学顺序、页面数量和课堂活动一旦有误，后面再修改完整提示词成本更高。蓝图确认能把教师判断保留在流程中。

### 可以用于培训讲座吗？

可以。请明确受众、总时长、学习成果和已有案例，Skill 会将场景识别为讲座或培训，而非普通新授课。

## 隐私与版权

- 不要把含有学生姓名、成绩、照片或其他敏感信息的材料提交到公开仓库。
- 不要把整本教材、受版权保护的课件或图片随 Skill 一起公开。
- 示例只展示工作流与输出结构，不附教材扫描件。
- 使用第三方 AI PPT 工具前，请核对其数据与版权政策。

## Validation

本地运行：

```bash
python3 tests/validate_structure.py
```

该检查不依赖第三方 Python 包，会验证核心文件、YAML 基本字段、目录名称和引用文件。

## License

MIT License。可自由使用、修改和分发，但请保留版权与许可声明。

---

English summary: A portable Agent Skill that turns teaching materials into a reviewable slide blueprint and, after teacher approval, a complete Markdown prompt for AI presentation tools. The core skill is instruction-only, has no runtime dependencies, and follows the standard `SKILL.md` folder format.

