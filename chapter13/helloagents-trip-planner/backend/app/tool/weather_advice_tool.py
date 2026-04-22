from hello_agents.tools import Tool, ToolParameter
from typing import Dict, Any, List


class ClothingAdviceTool(Tool):
    """穿衣建议工具 - 根据温度和天气状况提供穿衣建议"""

    def __init__(self):
        super().__init__(
            name="get_clothing_advice",
            description="根据温度和天气状况提供穿衣建议。参数：temperature(温度，整数), weather_condition(天气状况，如'晴'、'雨'、'雪'、'多云')"
        )

    def run(self, parameters: Dict[str, Any]) -> str:
        """
        执行穿衣建议逻辑
        
        Args:
            parameters: 包含 temperature (int) 和 weather_condition (str) 的字典
            
        Returns:
            具体的穿衣建议字符串
        """
        temperature = parameters.get("temperature", 20)
        weather_condition = parameters.get("weather_condition", "晴")
        
        advice = ""
        
        # 简单的逻辑判断
        if temperature < 0:
            advice = "天气非常寒冷,请穿羽绒服、戴帽子和手套。"
        elif temperature < 10:
            advice = "天气较冷,建议穿大衣或厚毛衣。"
        elif temperature < 20:
            advice = "气温适宜,可以穿夹克或长袖衬衫。"
        else:
            advice = "天气炎热,建议穿短袖、短裤并注意防晒。"
            
        if "雨" in weather_condition:
            advice += " 另外,出门请记得带伞。"
            
        return advice

    def get_parameters(self) -> List[ToolParameter]:
        """获取工具参数定义"""
        return [
            ToolParameter(
                name="temperature",
                type="integer",
                description="当前气温(摄氏度)",
                required=True
            ),
            ToolParameter(
                name="weather_condition",
                type="string",
                description="天气状况(如:晴、雨、雪、多云)",
                required=True
            )
        ]
