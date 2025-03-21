# 和风天气 homeassistant插件

本分支由[zhheo](https://github.com/zhheo)开发，基于[_小愚_](https://space.bilibili.com/15856864)的和风天气进行修改，因为改动的代码太多，就不和主项目合并了。

相比[原项目](https://github.com/c1pher-cn/heweather)，我主要将配置都放在UI界面中进行，安装和使用比较方便。

## 使用说明：

1.使用和风官方apiv7版本

2.必须申请开发者账号里的免费api，请务必升级到开发者账号（免费，但要提交身份证审核，api权限会比普通用户高一些）https://console.qweather.com/#/console

3.appkey申请需要先[创建应用](https://console.qweather.com/#/apps),后选添加数据key，选wabapi即可

    国内的城市区域location关系：https://github.com/qwd/LocationList/blob/master/China-City-List-latest.csv

4.新版本整合优化了sensor以及相关中文名字，图标。将原有的24小时天天气预报从sensor中转移到weather里

## 安装方法

1. 下载代码并解压
2. 复制`custom_components/heweather`文件夹到你的Home Assistant的`custom_components`目录下
3. 重启Home Assistant

## 配置方法

### 方法一：通过用户界面配置（推荐）

1. 在Home Assistant的配置 -> 集成 页面中点击添加集成
2. 搜索"和风天气"并点击
3. 从下拉菜单中选择你所在的城市/区县，或选择"自定义输入"手动输入位置ID [点我查看对照表](https://raw.githubusercontent.com/qwd/LocationList/master/China-City-List-latest.csv)
4. 输入以下信息：
   - 名称：自定义名称（默认为"和风天气"）
   - API密钥：在和风天气开发者平台申请的key
   - 灾害预警等级：1-6之间的数字，表示关注哪个等级及以上的灾害
   - 灾害预警信息格式：选择"title"（只显示标题）或"allmsg"（显示标题+明细信息）
5. 点击提交，完成配置

后续如需修改配置，可以在集成页面找到"和风天气"，点击"选项"进行修改。你可以选择保持当前位置或更改位置。

