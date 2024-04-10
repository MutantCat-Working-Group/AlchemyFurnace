<div align=center>
<img src="https://s2.loli.net/2024/04/10/PGYR7DdUOcZp5re.jpg" style="width:100px;"/>
<h2>炼丹炉</h2>
</div>

### 一、功能简述
- 各种编程语言的主动向外部发送信息的库。
- 直接以代码而不是包装后的各种形式提供，坚持只有一个文件。

### 二、使用方法

1. 在你的程序中添加对应的程序文件。
2. 在代码中引入功能并按说明简单调用即可。

### 二、语言支持

| 语言   | 是否实现 | 版本号     |
| ------ | -------- | ---------- |
| Python | ✅        | 1.0.240410 |
| Java   |          |            |
| Go     |          |            |
| C/C++  |          |            |
| Rust   |          |            |

### 四、详细说明

1. Python版本

   - 使用方法可参照Example.py

   - 方法列表

     | [性质]方法名（参数列表）                                  | 说明                                                         |
     | --------------------------------------------------------- | ------------------------------------------------------------ |
     | [构造]AlchemyFurnace(notice_way, token, secret0, secret1) | notice_way: 通知方式 当前支持钉钉机器人（dingbot）<br/>token: 发送的token或地址等信息<br/>secret0: 发送目标的密钥的第一部分<br/>secret1: 发送目标的密钥的第二部分<br/>关于dingbot，token是机器人的token，secret0是机器人的密钥，secret1是机器人的app_key（可选） |
     | [功能]send_message(title, message)                        |                                                              |
     | [功能]get_ding_image_mediaid(img)                         |                                                              |

### 五、开发进度

- [ ] 向钉钉机器人发送消息（1.0.240410）
- [ ] 向邮箱发送消息

### 六、相关项目

