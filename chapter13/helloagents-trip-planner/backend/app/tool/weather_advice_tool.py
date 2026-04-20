# 自定义的一个工具，接着注册，接着调用
def get_clothing_advice(temperature: int, weather_condition: str) -> str:
    """
    根据温度和天气状况提供穿衣建议。
    
    Args:
        temperature: 当前气温（摄氏度）。
        weather_condition: 天气状况（如：晴、雨、雪、多云）。
        
    Returns:
        具体的穿衣建议字符串。
    """
    advice = ""
    
    # 简单的逻辑判断
    if temperature < 0:
        advice = "天气非常寒冷，请穿羽绒服、戴帽子和手套。"
    elif temperature < 10:
        advice = "天气较冷，建议穿大衣或厚毛衣。"
    elif temperature < 20:
        advice = "气温适宜，可以穿夹克或长袖衬衫。"
    else:
        advice = "天气炎热，建议穿短袖、短裤并注意防晒。"
        
    if "雨" in weather_condition:
        advice += " 另外，出门请记得带伞。"
        
    return advice