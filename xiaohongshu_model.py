#定义llm输出的内容的数据模型为：pydantic 定义的数据模型
from pydantic import BaseModel, Field
#BaseModel：pydantic 库中的基类，所有使用 pydantic 定义的数据模型类都需要继承自 BaseModel，这样才能利用 pydantic 的数据验证和序列化功能。
#Field：pydantic 提供的一个函数，用于为模型的字段添加额外的元数据，如描述信息、约束条件等。
from typing import List
#List：来自 typing 模块，用于表示列表类型，这里指定 titles 字段是一个字符串列表。

class Xiaohongshu(BaseModel):
#(BaseModel)：表示 Xiaohongshu 类继承自 BaseModel，继承后 Xiaohongshu 类就具备了 pydantic 数据模型的特性。
    titles: List[str] = Field(description="小红书的5个标题", min_items=5, max_items=5)
    #titles：字段的名称，表示小红书笔记的标题列表。
#List[str]：指定 titles 字段的类型为字符串列表，即该字段的值应该是一个由多个字符串组成的列表。
#Field(...)：使用 Field 函数为 titles 字段添加额外的元数据(补充描述)。
#description="小红书的5个标题"：为该字段添加描述信息，说明这个字段代表小红书的 5 个标题，这个描述信息在生成文档（如 JSON Schema）时会被使用。

    content: str = Field(description="小红书的正文内容")
#str：指定 content 字段的类型为字符串，即该字段的值应该是一个字符串。

