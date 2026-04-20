## 📚 DRY 原则详解

**DRY** 是 **Don't Repeat Yourself**（不要重复自己）的缩写，这是软件开发中最核心的设计原则之一。

---

## 🎯 核心思想

> **"每一段知识在系统中都应该有单一、明确、权威的表示"**

换句话说：**相同的代码逻辑不应该在多处重复出现**。

---

## 🔍 在 `map.py` 中违反 DRY 的表现

让我用实际代码说明：

### ❌ 当前写法（违反 DRY）

```python
# 接口1: 搜索POI
@router.get("/poi")
async def search_poi(...):
    try:
        service = get_amap_service()           # ← 重复1
        pois = service.search_poi(...)          # ← 业务逻辑
        return POISearchResponse(               # ← 重复2
            success=True,
            message="POI搜索成功",
            data=pois
        )
    except Exception as e:                      # ← 重复3
        print(f"❌ POI搜索失败: {str(e)}")
        raise HTTPException(status_code=500, detail=f"POI搜索失败: {str(e)}")


# 接口2: 查询天气
@router.get("/weather")
async def get_weather(...):
    try:
        service = get_amap_service()           # ← 重复1（完全一样）
        weather_info = service.get_weather(...) # ← 业务逻辑
        return WeatherResponse(                # ← 重复2（结构一样）
            success=True,
            message="天气查询成功",
            data=weather_info
        )
    except Exception as e:                      # ← 重复3（完全一样）
        print(f"❌ 天气查询失败: {str(e)}")
        raise HTTPException(status_code=500, detail=f"天气查询失败: {str(e)}")


# 接口3: 规划路线
@router.post("/route")
async def plan_route(request: RouteRequest):
    try:
        service = get_amap_service()           # ← 重复1（完全一样）
        route_info = service.plan_route(...)    # ← 业务逻辑
        return RouteResponse(                  # ← 重复2（结构一样）
            success=True,
            message="路线规划成功",
            data=route_info
        )
    except Exception as e:                      # ← 重复3（完全一样）
        print(f"❌ 路线规划失败: {str(e)}")
        raise HTTPException(status_code=500, detail=f"路线规划失败: {str(e)}")
```

**重复的部分：**
1. `service = get_amap_service()` - 每个接口都获取服务实例
2. `return XxxResponse(success=True, message="...", data=...)` - 响应格式完全一致
3. `except Exception as e: ... raise HTTPException(...)` - 异常处理逻辑相同

---

## ✅ 遵循 DRY 的改进方案

### 方案1：提取通用装饰器

```python
from functools import wraps
from typing import Callable, Any
import logging

logger = logging.getLogger(__name__)


def handle_api_response(response_model_class: type, success_message: str):
    """
    通用API响应处理装饰器
    
    Args:
        response_model_class: 响应模型类（如 POISearchResponse）
        success_message: 成功消息
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        async def wrapper(*args, **kwargs) -> Any:
            try:
                # 统一获取服务实例
                service = get_amap_service()
                
                # 执行业务逻辑（注入 service）
                result = await func(service, *args, **kwargs)
                
                # 统一响应格式
                return response_model_class(
                    success=True,
                    message=success_message,
                    data=result
                )
                
            except ValueError as e:
                logger.warning(f"参数错误: {e}")
                raise HTTPException(status_code=400, detail=str(e))
                
            except ConnectionError as e:
                logger.error(f"外部服务连接失败: {e}")
                raise HTTPException(status_code=503, detail="服务暂时不可用")
                
            except Exception as e:
                logger.exception(f"未预期错误: {e}")
                raise HTTPException(status_code=500, detail=f"服务器内部错误: {str(e)}")
        
        return wrapper
    return decorator


# ✅ 使用装饰器后（消除重复）
@router.get("/poi", response_model=POISearchResponse)
@handle_api_response(POISearchResponse, "POI搜索成功")
async def search_poi(
    service,  # ← 由装饰器注入
    keywords: str = Query(...),
    city: str = Query(...),
    citylimit: bool = Query(True)
):
    """只关注业务逻辑"""
    return service.search_poi(keywords, city, citylimit)


@router.get("/weather", response_model=WeatherResponse)
@handle_api_response(WeatherResponse, "天气查询成功")
async def get_weather(
    service,  # ← 由装饰器注入
    city: str = Query(...)
):
    """只关注业务逻辑"""
    return service.get_weather(city)


@router.post("/route", response_model=RouteResponse)
@handle_api_response(RouteResponse, "路线规划成功")
async def plan_route(
    service,  # ← 由装饰器注入
    request: RouteRequest
):
    """只关注业务逻辑"""
    return service.plan_route(
        origin_address=request.origin_address,
        destination_address=request.destination_address,
        origin_city=request.origin_city,
        destination_city=request.destination_city,
        route_type=request.route_type
    )
```

**改进效果：**
- ✅ 消除了 3 处 `get_amap_service()` 重复
- ✅ 消除了 3 处响应格式化重复
- ✅ 消除了 3 处异常处理重复
- ✅ 每个接口只关注核心业务逻辑

---

### 方案2：依赖注入（FastAPI 推荐）

```python
from fastapi import Depends


def get_map_service():
    """依赖注入：获取地图服务"""
    return get_amap_service()


@router.get("/poi", response_model=POISearchResponse)
async def search_poi(
    keywords: str = Query(...),
    city: str = Query(...),
    citylimit: bool = Query(True),
    service = Depends(get_map_service)  # ← FastAPI 自动注入
):
    try:
        pois = service.search_poi(keywords, city, citylimit)
        return POISearchResponse(success=True, message="POI搜索成功", data=pois)
    except Exception as e:
        logger.exception(f"POI搜索失败: {e}")
        raise HTTPException(status_code=500, detail=str(e))
```

---

## 📊 DRY 原则的对比总结

| 维度 | 违反 DRY | 遵循 DRY |
|------|---------|---------|
| **代码量** | 140行（大量重复） | 80行（精简50%） |
| **修改成本** | 改异常处理需改3处 | 改装饰器只需1处 |
| **出错概率** | 可能漏改某处 | 统一处理，不易遗漏 |
| **可读性** | 噪音多，核心逻辑不突出 | 业务逻辑清晰可见 |
| **测试难度** | 需测试3个接口的异常分支 | 测试装饰器即可 |

---

## 💡 DRY 原则的其他应用场景

### 1. **常量提取**
```python
# ❌ 违反 DRY
if status == "active": ...
if status == "active": ...

# ✅ 遵循 DRY
USER_STATUS_ACTIVE = "active"
if status == USER_STATUS_ACTIVE: ...
```

### 2. **工具函数封装**
```python
# ❌ 违反 DRY
date1 = datetime.strptime("2024-01-01", "%Y-%m-%d")
date2 = datetime.strptime("2024-02-01", "%Y-%m-%d")

# ✅ 遵循 DRY
def parse_date(date_str: str) -> datetime:
    return datetime.strptime(date_str, "%Y-%m-%d")

date1 = parse_date("2024-01-01")
date2 = parse_date("2024-02-01")
```

### 3. **配置集中管理**
```python
# ❌ 违反 DRY（到处硬编码）
timeout = 30
timeout = 30

# ✅ 遵循 DRY
class Config:
    REQUEST_TIMEOUT = 30

timeout = Config.REQUEST_TIMEOUT
```

---

## ⚖️ DRY 的边界（不要过度）

**什么时候可以不遵守 DRY？**

1. **偶然相似** - 两段代码现在看起来一样，但未来可能朝不同方向演化
2. **抽象成本高** - 提取公共代码会导致复杂度剧增
3. **性能敏感** - 额外的函数调用开销不可接受

**判断标准：**
> 如果两段代码**语义相同**且**变化原因相同**，就应该合并；如果只是**表面相似**但**职责不同**，应该保持独立。

---

## 🎓 总结

**DRY 原则的本质是：**
- 📦 **封装重复** - 把相同的逻辑提取成函数/类/装饰器
- 🔧 **单一来源** - 每段知识只有一个地方定义
- 🛠️ **易于维护** - 修改一处，全局生效

在你的 `map.py` 中，通过提取装饰器或依赖注入，可以显著减少重复代码，提高可维护性。这正是 DRY 原则的实际应用价值！