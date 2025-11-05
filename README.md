#目录结构
'''
app-auto/                       # 项目根
├─ apk/                         # 待测 apk/ipa，保持 Git-LFS
├─ config/                      # 所有静态配置
│  ├─ devices.yaml              # 多设备并行参数
│  ├─ caps.yaml                 # 公共 desired_caps
│  └─ env.yml                   # 域名/账号/数据库等
├─ src/                         # 业务代码
│  ├─ base_page.py              # 所有页面对象的基类，封装滑动、等待、截图
│  ├─ pages/                    # PO 层（Page-Object）
│  │  ├─ __init__.py
│  │  ├─ login_page.py
│  │  └─ home_page.py
│  ├─ business/                 # 业务流程层（>=2 个页面组合）
│  │  └─ login_biz.py
│  └─ common/                   # 纯技术工具
│     ├─ driver_manager.py      # 单例 driver、多设备并行
│     ├─ yaml_reader.py
│     └─ logger.py
├─ test_cases/                  # 只放测试用例，不含业务逻辑
│  ├─ test_login.py
│  └─ test_mine.py
├─ test_data/                   # 数据驱动文件
│  ├─ login.csv
│  └─ login.yaml
├─ outputs/                     # 运行产物，全部 .gitignore
│  ├─ screenshots/
│  ├─ logs/
│  └─ reports/                  # allure 原始 json
├─ scripts/                     # 辅助脚本
│  ├─ run.py                    # 本地一键执行入口
│  ├─ run_parallel.py           # 多设备并行
│  └─ wda_build.sh              # iOS WebDriverAgent 编译
├─ .gitlab-ci.yml               # CI 示例
├─ pytest.ini                   # 标记、路径、addopts
├─ requirements.txt
└─ README.md                    # 写清“如何跑起来”
'''

appium 权限问题
appium --allow-insecure=*:adb_shell