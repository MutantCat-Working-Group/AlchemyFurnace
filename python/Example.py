# 引入炼丹炉库
from AlchemyFurnace import AlchemyFurnace

# 创建炼丹炉实例
alchemy_furnace = AlchemyFurnace(notice_way='dingbot',
                                 token='9b0e99c69d7d659ae0c8a67e3ccefd15bd0c7b496775830d1e54c5f8ed09145e',
                                 secret0='JOSLGXrxc1OpN9lMh74ZRjz2jY9MbXrrCs1Amf5tCCYtnMY3EKcR8hPSn1tA0keq',
                                 secret1='dingevhxwsvon4rbhpbd')

# 发送消息
alchemy_furnace.send_message("title", "message")

# 发送消息并@所有人
alchemy_furnace.send_message_at("title", "message")

# 上传一张图片之后发过去
alchemy_furnace.send_message("title", "![image]("+alchemy_furnace.get_ding_image_mediaid('image.jpg') +")")


