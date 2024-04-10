<div align=center>
<img src="https://s2.loli.net/2024/04/10/PGYR7DdUOcZp5re.jpg" style="width:100px;"/>
<h2>炼丹炉</h2>
</div>

### 一、功能简述
- 各种编程语言的主动向外部发送信息的库，支持发送图片。
- 直接以代码而不是包装后的各种形式提供，大多只有一个文件。
- 如果运行设备支持联网，训练模式的时候的控制台日志，服务运行异常报错等均可使用本库发送提醒消息。

### 二、使用方法

1. 在你的程序中添加对应的程序文件。
2. 在代码中引入功能并按说明简单调用即可。

### 三、语言支持

| 语言   | 是否实现 | 版本号     | 说明                   |
| ------ | -------- | ---------- | ---------------------- |
| Python | ✅        | 1.0.240410 | 支持钉钉机器人通知方式 |
| Java   |          |            |                        |
| Go     |          |            |                        |
| C/C++  |          |            |                        |
| Rust   |          |            |                        |

### 四、详细说明

1. Python版本

   - 使用方法可参照Example.py

   - 功能列表

     | 性质 | 方法名                 | 参数列表                            | 说明                                                         |
     | ---- | ---------------------- | ----------------------------------- | ------------------------------------------------------------ |
     | 构造 | AlchemyFurnac          | notice_way, token, secret0, secret1 | notice_way: 通知方式 （dingbot...）<br/>token: 发送的token或地址等信息<br/>secret0: 发送目标的密钥的第一部分<br/>secret1: 发送目标的密钥的第二部分<br/>关于dingbot模式的参数中，token代表Webhook地址后面的token，secret0代表加签的密钥或AppSecret，secret1代表机器人的AppKey |
     | 功能 | send_message           | title, message                      | 发送消息（必填token、secret0）                               |
     | 功能 | get_ding_image_mediaid | img                                 | 通过图片获得钉钉开放平台的mediaid（钉钉模式下生效，必填app_key、secret0），用于在markdown中插入图片信息 |
     | 功能 | send_message_at        | title, message,one                  | 发送消息并且@某人<br/>关于dingbot模式中，会在群众艾特所有人  |

### 五、开发进度

- [x] 向钉钉机器人发送消息（1.0.240410）
- [ ] 向邮箱发送消息

### 六、相关项目

- [MutantCat-Working-Group/Echoes: 回声 (github.com)](https://github.com/MutantCat-Working-Group/Echoes)
