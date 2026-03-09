# Mock API Testing 面試題目 - Roku Automation QA Engineer

## 目錄
1. [基礎概念題](#基礎概念題)
2. [實作題](#實作題)
3. [系統設計題](#系統設計題)
4. [考試形式](#考試形式)
5. [Roku 特定考點](#roku-特定考點)
6. [準備建議](#準備建議)

---

## 基礎概念題

### 口頭或筆試問題

1. **什麼是 Mock?為什麼需要 Mock API?**
   - 考察對 Mock 基本概念的理解
   - 能否說明 Mock 的優缺點

2. **Mock 和 Stub 的差異是什麼?**
   - Mock: 驗證行為(是否被呼叫、呼叫次數、參數)
   - Stub: 只提供預設回應,不驗證行為

3. **什麼時候該用 Mock,什麼時候該用真實 API?**
   - Mock: 單元測試、快速反饋、隔離外部依賴
   - 真實 API: 整合測試、端到端測試、驗證實際行為

4. **`pytest.raises()` 和 `side_effect` 的差異?**
   - `pytest.raises()`: 測試程式碼**應該拋出**例外
   - `side_effect`: 模擬外部依賴拋出例外,測試程式碼**如何處理**例外

---

## 實作題

### 題目 1: Mock 外部 API 呼叫

**情境**: 給你一個呼叫 Roku API 的函數,要求你寫測試

```python
import requests

def get_device_info(device_id):
    """取得 Roku 裝置資訊"""
    response = requests.get(f"https://api.roku.com/devices/{device_id}")
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        return {"error": "Device not found"}
    else:
        raise Exception("API Error")
```

**要求**:
1. 測試成功情況(status_code = 200)
2. 測試裝置不存在(status_code = 404)
3. 測試 API 錯誤(status_code = 500)
4. 驗證 API 被正確呼叫

**考察重點**:
- ✅ 能否正確使用 `@patch` 或 `with patch`
- ✅ 能否正確設定 `return_value.json.return_value`
- ✅ 能否測試不同的 HTTP 狀態碼
- ✅ 能否驗證 API 被正確呼叫(`assert_called_once_with`)

**提示**:
- 需要 mock `requests.get`
- 需要設定不同的 `status_code`
- 記得驗證 API 被正確呼叫

---

### 題目 2: 測試重試機制

**情境**: Roku 的串流服務可能會有網路問題,需要重試機制

```python
import requests

def stream_content(content_id, max_retries=3):
    """串流內容,帶重試機制"""
    for attempt in range(max_retries):
        try:
            response = requests.get(f"https://api.roku.com/stream/{content_id}")
            if response.status_code == 200:
                return response.json()
        except requests.Timeout:
            if attempt == max_retries - 1:
                raise
            continue
    return None
```

**要求**:
1. 測試第1次失敗,第2次成功
2. 測試所有重試都失敗
3. 驗證重試次數

**考察重點**:
- ✅ 能否使用 `side_effect` 模擬多次呼叫
- ✅ 能否混合例外和成功回應
- ✅ 能否驗證重試次數(`call_count`)

**提示**:
- 使用 `side_effect` 列表模擬多次呼叫
- 第一個元素可以是例外,第二個元素是成功回應
- 記得驗證 `call_count`

---

### 題目 3: 測試非同步 API 或輪詢

**情境**: 上傳影片到 Roku,需要輪詢檢查處理狀態

```python
import requests
import time

def wait_for_video_processing(video_id, timeout=60):
    """等待影片處理完成"""
    start_time = time.time()
    
    while time.time() - start_time < timeout:
        response = requests.get(f"https://api.roku.com/videos/{video_id}/status")
        status = response.json()["status"]
        
        if status == "ready":
            return True
        elif status == "failed":
            return False
        
        time.sleep(5)
    
    return False  # 超時
```

**要求**:
1. 測試影片處理成功(processing → ready)
2. 測試影片處理失敗
3. 測試超時情況
4. 避免測試真的等待

**考察重點**:
- ✅ 能否 mock `time.time()` 和 `time.sleep()`
- ✅ 能否模擬狀態變化
- ✅ 能否測試超時邏輯

**提示**:
- 需要同時 mock `time.time()`, `time.sleep()`, 和 `requests.get()`
- 使用 `side_effect` 模擬狀態變化
- 注意 `@patch` 的順序(由下往上)

---

### 題目 4: 測試錯誤處理

**情境**: 測試各種 API 錯誤情況

```python
import requests

def get_channel_list(user_id):
    """取得使用者的頻道列表"""
    try:
        response = requests.get(
            f"https://api.roku.com/users/{user_id}/channels",
            timeout=10
        )
        return response.json()
    except requests.Timeout:
        return {"error": "Request timeout"}
    except requests.ConnectionError:
        return {"error": "Connection failed"}
    except Exception as e:
        return {"error": f"Unknown error: {str(e)}"}
```

**要求**:
1. 測試 Timeout 錯誤
2. 測試 ConnectionError
3. 測試其他例外
4. 驗證錯誤訊息

**考察重點**:
- ✅ 能否用 `side_effect` 模擬不同例外
- ✅ 能否測試所有錯誤分支
- ✅ 能否驗證錯誤訊息

**提示**:
- 使用 `side_effect` 設定不同的例外類型
- 測試每一個 except 分支
- 驗證錯誤訊息的內容

---

### 題目 5: 整合測試場景

**情境**: 測試一個完整的使用者流程

```python
import requests

class RokuService:
    def authenticate(self, username, password):
        """使用者登入"""
        response = requests.post(
            "https://api.roku.com/auth/login",
            json={"username": username, "password": password}
        )
        return response.json()
    
    def get_recommendations(self, user_id):
        """取得推薦內容"""
        response = requests.get(f"https://api.roku.com/users/{user_id}/recommendations")
        return response.json()
    
    def play_content(self, content_id):
        """播放內容"""
        response = requests.post(f"https://api.roku.com/play/{content_id}")
        return response.json()

def user_watch_flow(username, password):
    """完整的觀看流程"""
    service = RokuService()
    
    # 1. 登入
    auth_result = service.authenticate(username, password)
    if not auth_result.get("success"):
        return {"error": "Authentication failed"}
    
    user_id = auth_result["user_id"]
    
    # 2. 取得推薦
    recommendations = service.get_recommendations(user_id)
    if not recommendations:
        return {"error": "No recommendations"}
    
    # 3. 播放第一個推薦內容
    first_content = recommendations[0]["id"]
    play_result = service.play_content(first_content)
    
    return play_result
```

**要求**:
1. 測試完整的成功流程
2. 測試登入失敗
3. 測試沒有推薦內容
4. 驗證 API 呼叫順序

**考察重點**:
- ✅ 能否 mock 多個 API 呼叫
- ✅ 能否測試完整流程
- ✅ 能否處理流程中的各種錯誤情況

**提示**:
- 需要同時 mock `requests.post` 和 `requests.get`
- 使用 `side_effect` 處理多次 POST 呼叫
- 注意參數順序(由下往上)
- 驗證每個 API 的呼叫次數

---

## 系統設計題

### 資深職位可能會問的問題

#### 1. 如何設計一個可重用的 Mock API 框架?

**考察重點**:
- 程式碼組織能力
- 設計模式的理解
- 可維護性和可擴展性

**討論方向**:
- Base Mock Classes 的設計
- Factory Pattern 的應用
- Mock 資料的集中管理
- Helper Functions 的提供
- 文件和範例的重要性

**範例架構**:

```
tests/
├── mocks/
│   ├── __init__.py
│   ├── base.py              # Base Mock Classes
│   ├── roku_api_mock.py     # Roku API Mock
│   ├── factories.py         # Mock Factories
│   └── fixtures.py          # Pytest Fixtures
├── data/
│   ├── mock_responses.json  # Mock 資料
│   └── test_data.py         # 測試資料
└── helpers/
    └── mock_helpers.py      # Helper Functions
```

---

#### 2. 如何在 CI/CD 中整合 Mock 測試?

**考察重點**:
- CI/CD 流程的理解
- 測試策略的規劃
- 效能和效率的平衡

**討論方向**:
- 測試階段的劃分(PR → Merge → Deploy)
- 使用 pytest markers 區分測試類型
- 測試覆蓋率的設定
- 失敗處理和通知機制
- 測試報告的生成

**範例 CI/CD 流程**:

```yaml
# .github/workflows/test.yml
name: Tests

on: [push, pull_request]

jobs:
  unit-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run Mock Tests
        run: |
          pytest -m "mock" --cov=src --cov-report=xml
      - name: Check Coverage
        run: |
          coverage report --fail-under=80

  integration-tests:
    runs-on: ubuntu-latest
    needs: unit-tests
    steps:
      - name: Run Integration Tests
        run: |
          pytest -m "integration"
```

---

#### 3. 如何平衡 Mock 測試和整合測試?

**考察重點**:
- 測試策略的理解
- 成本效益分析
- 實務經驗

**討論方向**:
- 測試金字塔理論
- 何時該用 Mock vs 真實 API
- 測試比例的建議
- 避免過度 Mock 的陷阱
- 關鍵路徑的識別

**測試金字塔**:

```
        /\
       /  \      E2E Tests (10%)
      /____\     - 使用真實 API
     /      \    - 測試關鍵使用者流程
    /        \   
   /__________\  Integration Tests (20%)
  /            \ - 部分 Mock,部分真實
 /              \- 測試模組間互動
/________________\
Unit Tests (70%)
- 大量使用 Mock
- 快速、穩定、隔離
```

**建議原則**:
- ✅ 單元測試:大量使用 Mock(70%)
- ✅ 整合測試:部分 Mock(20%)
- ✅ E2E 測試:使用真實 API(10%)
- ✅ 關鍵路徑:必須有整合測試
- ✅ 邊界情況:可以用 Mock 測試

---

#### 4. 如何處理 API 版本變更?

**考察重點**:
- 版本管理的理解
- 向後相容性的處理
- 維護策略

**討論方向**:
- API Schema 驗證
- 版本化的 Mock 資料
- 定期執行整合測試
- 契約測試(Contract Testing)
- 文件同步機制

**範例策略**:

```python
# 版本化的 Mock 資料
mock_responses = {
    "v1": {
        "get_device": {"id": "123", "name": "Roku"}
    },
    "v2": {
        "get_device": {
            "id": "123",
            "name": "Roku",
            "model": "Ultra",  # 新增欄位
            "firmware": "10.0"
        }
    }
}

# API Schema 驗證
from jsonschema import validate

def test_api_response_schema():
    schema = {
        "type": "object",
        "properties": {
            "id": {"type": "string"},
            "name": {"type": "string"},
            "model": {"type": "string"}
        },
        "required": ["id", "name"]
    }
    
    response = get_device_info("123")
    validate(instance=response, schema=schema)
```

**建議做法**:
1. 使用 API Schema 驗證確保一致性
2. 定期執行整合測試驗證 Mock 的正確性
3. 版本化管理 Mock 資料
4. 實施契約測試(Pact, Spring Cloud Contract)
5. 建立 API 變更通知機制

---

## 考試形式

### 形式 1: Live Coding (最常見)

**時間**: 30-45 分鐘

**流程**:
1. 面試官給你一個簡單的 API 呼叫函數
2. 要求你當場寫出完整測試
3. 可能會要求你邊寫邊解釋思路
4. 可能會追問如何改進

**評分標準**:
- ✅ 程式碼正確性
- ✅ 測試覆蓋率
- ✅ 程式碼品質
- ✅ 溝通能力
- ✅ 問題解決能力

**準備建議**:
- 熟練 pytest 和 unittest.mock
- 練習在白板或線上編輯器寫程式
- 準備常見的測試模式
- 練習口頭解釋程式碼

---

### 形式 2: Take-Home Assignment

**時間**: 2-4 小時

**內容**:
- 給你一個小專案
- 要求你為所有 API 呼叫寫測試
- 可能包含 README 說明如何執行測試
- 可能要求提交 PR

**評分標準**:
- ✅ 測試完整性
- ✅ 程式碼品質
- ✅ 文件完整性
- ✅ Git commit 品質
- ✅ 額外的創意

**準備建議**:
- 建立測試專案模板
- 準備 README 模板
- 熟悉 pytest 的進階功能
- 注意程式碼風格和註解

---

### 形式 3: Code Review

**時間**: 20-30 分鐘

**內容**:
- 給你一段已經寫好的測試程式碼
- 要求你找出問題並改進
- 可能要求你口頭說明

**常見問題**:
- ❌ 沒有驗證 mock 被呼叫
- ❌ 測試覆蓋率不足
- ❌ 過度 Mock
- ❌ 測試不穩定
- ❌ 命名不清楚

**準備建議**:
- 熟悉常見的測試反模式
- 了解測試最佳實踐
- 練習 code review 技巧

---

## Roku 特定考點

### 1. 串流相關測試

**可能的考題**:
- 測試影片播放 API
- 測試緩衝機制
- 測試品質切換(HD → 4K)
- 測試播放失敗處理

**範例**:

```python
def test_video_playback_quality_switch():
    """測試影片品質切換"""
    with patch('requests.post') as mock_post:
        # Mock 品質切換回應
        response = Mock()
        response.json.return_value = {
            "quality": "4K",
            "bitrate": "25Mbps"
        }
        mock_post.return_value = response
        
        result = switch_video_quality("video123", "4K")
        
        assert result["quality"] == "4K"
```

---

### 2. 裝置管理測試

**可能的考題**:
- 測試裝置註冊
- 測試多裝置同步
- 測試裝置狀態更新

---

### 3. 內容推薦測試

**可能的考題**:
- 測試推薦演算法的 API 呼叫
- 測試個人化推薦
- 測試推薦更新機制

---

### 4. 廣告系統測試

**可能的考題**:
- 測試廣告 API 整合
- 測試廣告投放邏輯
- 測試廣告追蹤

---

### 5. 效能測試

**可能的考題**:
- 測試 API 回應時間
- 測試重試邏輯的效能影響
- 測試並發請求

---

## 準備建議

### 必須熟練的技能

1. ✅ **`@patch` 和 `with patch` 的使用**
   - 知道何時用哪一種
   - 理解 patch 的路徑規則

2. ✅ **`return_value` 和 `side_effect` 的差異**
   - `return_value`: 設定單一回傳值
   - `side_effect`: 設定多個回傳值或例外

3. ✅ **驗證 mock 被呼叫的方式**
   - `assert_called()`
   - `assert_called_once()`
   - `assert_called_with()`
   - `assert_called_once_with()`
   - `assert_any_call()`
   - `call_count`

4. ✅ **測試例外處理**
   - 使用 `pytest.raises()`
   - 使用 `side_effect` 模擬例外

5. ✅ **測試重試機制**
   - 使用 `side_effect` 列表
   - 驗證重試次數

6. ✅ **Mock 多個依賴**
   - 使用多個 `@patch`
   - 理解參數順序(由下往上)

---

### 加分項

1. 🌟 **了解 `pytest-mock` 套件**
   - 更簡潔的 mock 語法
   - 與 pytest 更好的整合

2. 🌟 **會使用 `responses` 或 `requests-mock` 套件**
   - 專門用於 mock HTTP 請求
   - 更直觀的 API

3. 🌟 **了解 fixture 的使用**
   - 建立可重用的 mock
   - 管理測試資料

4. 🌟 **會寫 parametrize 測試**
   - 測試多組資料
   - 減少重複程式碼

5. 🌟 **了解測試覆蓋率工具**
   - pytest-cov
   - coverage.py
   - 設定覆蓋率門檻

6. 🌟 **了解契約測試**
   - Pact
   - Spring Cloud Contract
   - 確保 Mock 和真實 API 一致

---

## 實戰練習建議

### 練習計畫

**第 1 週**: 基礎練習
- 練習 `@patch` 和 `return_value`
- 練習測試不同 HTTP 狀態碼
- 練習驗證 mock 被呼叫

**第 2 週**: 進階練習
- 練習 `side_effect` 的各種用法
- 練習測試重試機制
- 練習測試例外處理

**第 3 週**: 整合練習
- 練習 mock 多個 API
- 練習測試完整流程
- 練習測試輪詢機制

**第 4 週**: 模擬面試
- 限時完成練習題
- 錄影自己的解題過程
- 檢討和改進

---

## 參考資源

### 官方文件
- [Python unittest.mock](https://docs.python.org/3/library/unittest.mock.html)
- [pytest 官方文件](https://docs.pytest.org/)
- [pytest-mock](https://pytest-mock.readthedocs.io/)

### 推薦閱讀
- [Real Python - Understanding the Python Mock Object Library](https://realpython.com/python-mock-library/)
- [Martin Fowler - Mocks Aren't Stubs](https://martinfowler.com/articles/mocksArentStubs.html)
- [Google Testing Blog](https://testing.googleblog.com/)

### 練習平台
- LeetCode (雖然主要是演算法,但可以練習寫測試)
- HackerRank (有專門的測試題目)
- 自己的 GitHub 專案

---

## 總結

Mock API 測試是 Automation QA Engineer 的核心技能之一。準備面試時:

1. **紮實基礎**: 熟練掌握 `@patch`、`return_value`、`side_effect`
2. **實戰練習**: 多寫程式碼,不要只看理論
3. **理解原理**: 知道為什麼要這樣寫,不只是背語法
4. **溝通能力**: 能清楚解釋你的測試策略
5. **持續學習**: 關注最新的測試工具和最佳實踐

祝你面試順利! 🚀
