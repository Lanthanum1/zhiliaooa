# zhiliaooa

映射`ORM`模型：
1. `flask db init` 只需执行一次
2. `flask db migrate` 识别ORM模型的改变，生成迁移脚本
3. `flask db upgrade` 运行迁移脚本，同步到数据库中