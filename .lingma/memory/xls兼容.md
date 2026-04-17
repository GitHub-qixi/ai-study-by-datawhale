## 实施计划 (Implementation Plan)

- [成功] **1. 语法检测与现状分析**
   - 确认 `deepdoc/parser/excel_parser.py` 中 `_load_excel_to_workbook` 方法已包含对 `.xls` 文件头（`\xD0\xCF\x11\xE0`）的识别逻辑。
   - 检查 `api/apps/document_app.py` 的 `/get/<doc_id>` 接口，发现目前仅对 `.doc` 格式进行了转换处理，而 `.xls` 直接返回原始二进制流。
   - 验证前端预览组件是否仅支持 `.xlsx` (OpenXML) 格式，导致旧版 `.xls` (OLE2) 无法渲染。

- [成功] **2. 在 `api/utils/util_function.py` 中实现 `convert_xls_to_xlsx` 函数**
   - **文件**: `api/utils/util_function.py`
   - **符号**: `def convert_xls_to_xlsx(xls_data: bytes) -> bytes:`
   - **行为**: 
     - **增加二进制头检测**：通过检查前 4 个字节（`PK\x03\x04` 为 xlsx，`\xD0\xCF\x11\xE0` 为 xls）来精准识别文件真实格式，防止因后缀名错误导致的转换失败。
     - 使用 `pandas.read_excel` (依赖 `xlrd`) 读取 `.xls` 二进制数据。
     - 使用 `openpyxl` 将数据写入内存中的 `.xlsx` 格式字节流。
     - 增加异常处理，确保在转换失败时抛出明确的错误信息。

- [成功] **3. 修改 `api/apps/document_app.py` 的文档获取逻辑**
   - **文件**: `api/apps/document_app.py`
   - **符号**: `def get(doc_id):`
   - **行为**: 
     - 在检测到文件扩展名为 `.xls` 时，调用 `convert_xls_to_xlsx` 进行实时转换。
     - 更新响应的 `Content-Type` 为 `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`。
     - 建议同时更新文件名后缀（可选，或在响应头中提示）。

- [成功] **4. 结果校验与测试**
   - **发现的问题**: 在创建文件夹时出现 `KeyError: 'new_location'` 错误
   - **原因分析**: `document_app.py` 中 `folderCreate` 方法在调用 `DocumentService.insert` 时未包含 `new_location` 字段，但后续调用 `FileService.add_file_from_kb` 时期望该字段存在
   - **修复方案**: 在创建文件夹的字典中添加 `"new_location": None` 字段（文件夹不需要实际存储位置）
   - **修复文件**: `api/apps/document_app.py` 第 2101 行后添加 `"new_location": None,`
   - **验证结果**: 修复后文件夹创建功能恢复正常
