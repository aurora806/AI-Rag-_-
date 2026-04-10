# 🤖 智扫通 Agent - 扫地机器人智能客服系统

本项目是一个面向消费者（ToC）的扫地机器人智能客服系统，旨在为用户提供全周期的产品服务。系统基于大语言模型（LLM），结合 **RAG（检索增强生成）** 技术与 **ReAct 智能体架构** 开发，能够自主规划、调用外部工具来解决复杂的用户需求。

## ✨ 核心功能

1. **智能问答服务 (基于 RAG)**
   - **售前咨询：** 处理关于扫地机器人功能、价格、型号对比等咨询。
   - **售后支持：** 解决操作指导、故障处理、维护建议等使用问题。
   - **精准回答：** 基于 RAG 技术从专属本地知识库中检索信息，确保回答的准确性与时效性，避免大模型幻觉。

2. **使用报告与优化建议生成**
   - **数据分析：** 自动分析用户的扫地机器人使用数据（如清洁频率、耗材状态、错误日志等）。
   - **个性化报告：** 总结使用情况，并提供优化建议（如调整清洁计划、部件更换提醒）。
   - **外部工具调用：** Agent 能够根据需求动态调用诸如获取天气、获取用户位置、时间等外部工具，辅助生成更贴近场景的报告。

## 🧠 技术架构与亮点

本项目打破了传统固定流程的链式调用（Chain），采用了**动态路由的 Agent 架构**：
- **核心大脑：** LLM 作为指挥官，根据用户输入自主思考（Think）-> 选择工具（Act）-> 获取结果（Observe）-> 生成最终回答。
- **技术栈：** - 框架：LangChain
  - 架构：ReAct Agent
  - 检索：RAG (Vector Store)
  - 前端展示：Streamlit
- **工具集 (Tools)：** 集成了包括 `rag_summarize` (知识库检索)、`get_weather` (天气查询)、`get_user_location` (位置获取) 等自定义工具。

## 📂 项目结构

```text
├── agent/                  # Agent 核心逻辑
│   ├── tools/              # Agent 可调用的外部工具集 (agent_tools.py, middleware.py)
│   └── react_agent.py      # ReAct 智能体定义与执行逻辑
├── config/                 # 配置文件目录
├── data/                   # 本地知识库文档与数据
├── model/                  # 模型工厂
│   └── factory.py          # 实例化大语言模型 (Chat Model) 和 向量模型 (Embed Model)
├── prompts/                # 提示词模板目录
├── rag/                    # RAG 检索增强生成模块
│   ├── rag_service.py      # RAG 业务逻辑处理
│   └── vector_store.py     # 向量数据库服务 (文档加载、切分、向量化)
├── utils/                  # 通用工具类 (日志、文件处理、配置解析等)
├── app.py                  # Streamlit Web 端入口文件
├── requirements.txt        # 项目依赖包
└── README.md               # 项目说明文档
```

## 🚀 快速开始

### 1. 获取项目代码
将本项目克隆到本地，并进入项目根目录：
```bash
git clone [https://github.com/你的用户名/你的仓库名.git](https://github.com/你的用户名/你的仓库名.git)
cd 你的仓库名
```
### 2. 环境配置
本项目推荐使用 Python 3.9+。为避免污染全局环境，强烈建议使用虚拟环境：

第一步：创建虚拟环境
```bash
python -m venv .venv
```
第二步：激活虚拟环境
Windows 系统:
```bash
.venv\Scripts\activate
```
macOS / Linux 系统:
```bash
source .venv/bin/activate
```
第三步：安装依赖：
```bash
pip install -r requirements.txt
```

### 3. 配置环境变量
智能体运行需要调用大模型服务。请在项目根目录下新建一个 .env 文件，并配置你的 API 密钥：
# 大语言模型 API 密钥 (请替换为你实际使用的 Key)
```
LLM_API_KEY="sk-xxxxxxxxxxxxxxxxxxxxxxxx"
```

### 4. 启动服务
确认环境与配置均已就绪后，启动 Streamlit Web 端服务：
```bash
streamlit run app.py
```










