"""LLM服务模块"""

from hello_agents import HelloAgentsLLM
from ..config import get_settings
from dotenv import load_dotenv
import os

# 加载环境变量
load_dotenv()

# 全局LLM实例
_llm_instance = None


def get_llm() -> HelloAgentsLLM:
    """
    获取LLM实例(单例模式)
    
    Returns:
        HelloAgentsLLM实例
    """
    global _llm_instance
    
    if _llm_instance is None:
        settings = get_settings()
        
        # HelloAgentsLLM会自动从环境变量读取配置
        # 包括OPENAI_API_KEY, OPENAI_BASE_URL, OPENAI_MODEL等
        _llm_instance = HelloAgentsLLM(
            provider="openai",  # 使用OpenAI兼容接口
            model=os.getenv("LLM_MODEL_ID", "LongCat-Flash-Chat"),
            api_key=os.getenv("LLM_API_KEY"),
            base_url=os.getenv("LLM_BASE_URL", "https://api.longcat.chat/openai"),
            temperature=0.7,  # 显式设置temperature，避免None值
            max_tokens=2048   # 显式设置max_tokens
        )

        
        print(f"✅ LLM服务初始化成功")
        print(f"   提供商: {_llm_instance.provider}")
        print(f"   模型: {_llm_instance.model}")
    
    return _llm_instance


def reset_llm():
    """重置LLM实例(用于测试或重新配置)"""
    global _llm_instance
    _llm_instance = None

