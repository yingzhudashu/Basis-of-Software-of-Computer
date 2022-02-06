--使用命令创建数据库

CREATE DATABASE DataBaseEG_18373579
ON PRIMARY

(
Name=DataBaseEG_data,
Filename='D:\SQLserver\test\DBEG_data.mdf',
Size=8MB,
Maxsize=unlimited,
Filegrowth=10%
)

LOG ON
(
Name=DataBaseEG_log,
Filename='D:\SQLserver\test\DBEG_log.ldf',
Size=3MB,
Maxsize=50MB,
FileGrowth=2MB
)
