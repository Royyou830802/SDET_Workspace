# Day 6: Mock 完整教學

## 目錄
1. [Mock 的定義](#mock-的定義)
2. [為什麼需要 Mock?](#為什麼需要-mock)
3. [基本概念:從簡單到複雜](#基本概念從簡單到複雜)
4. [return_value 詳細解釋](#returnvalue-詳細解釋)
5. [10 種常見 Mock 用法](#10-種常見-mock-用法)
6. [常用方法總結](#常用方法總結)
7. [實戰建議](#實戰建議)

---

## Mock 的定義

**Mock** 是測試中的一種技術,用來**模擬(替代)真實的物件或函數**。當你在寫測試時,有時候不想或無法使用真實的元件(例如資料庫、API、檔案系統等),這時就可以用 Mock 來取代它們。

---

## 為什麼需要 Mock?

1. **隔離測試**: 只測試你想測試的程式碼,不受外部依賴影響
2. **加快測試速度**: 不需要真的連接資料庫或呼叫 API
3. **控制測試環境**: 可以模擬各種情況(成功、失敗、異常等)
4. **避免副作用**: 不會真的修改資料庫或發送郵件

### 生活例子比喻

想像你在拍電影:
- **真實情況**: 演員真的開車撞牆 → 危險、昂貴
- **Mock 情況**: 用特效、替身、模型車 → 安全、便宜、可重複

測試也是一樣:
- **真實情況**: 真的連資料庫、打 API → 慢、可能失敗、有副作用
- **Mock 情況**: 用假的物件 → 快、穩定、可控制

---

## 基本概念:從簡單到複雜

### 情境 1: 不需要 Mock 的簡單函數

```python
def add_numbers(a, b):
    return a + b

# 測試
def test_add_numbers():
    result = add_numbers(2, 3)
    assert result == 5  # 檢查結果是否為 5
```

這個**不需要 Mock**,因為函數很單純,沒有依賴外部的東西。

### 情境 2: 需要 Mock 的函數

假設你有一個函數會打電話給客戶:

```python
def send_notification(phone_number, message):
    # 這會真的打電話!
    phone_service.call(phone_number, message)
    return "通知已發送"
```

**問題**:
- 測試時,你不想真的打電話給客戶
- 每次測試都打電話,會花錢、花時間
- 萬一測試失敗,客戶會收到一堆騷擾電話

**解決方法:用 Mock 假裝打電話**

```python
from unittest.mock import Mock

def test_send_notification():
    # 建立一個假的 phone_service
    fake_phone_service = Mock()
    
    # 用假的服務來測試
    send_notification("0912345678", "您好")
    
    # 檢查有沒有「假裝」打電話
    fake_phone_service.call.assert_called_once()
```

---

## return_value 詳細解釋

### 關鍵概念:Mock 會自動產生屬性

Mock 物件有一個**神奇的特性**:
- 當你存取任何不存在的屬性時,它會**自動建立**一個新的 Mock
- 這叫做「自動規格」(auto-spec)

### 範例:Mock API 呼叫

#### 原始程式碼

```python
import requests

def get_user_name(user_id):
    # 步驟1: 呼叫 requests.get()
    response = requests.get(f"https://api.example.com/users/{user_id}")
    
    # 步驟2: 呼叫 response.json()
    # 步驟3: 取得 ["name"]
    return response.json()["name"]
```

#### 真實的 requests.get() 會回傳什麼?

```python
response = requests.get("https://...")
# response 是一個 Response 物件,有這些方法:
# - response.json()  → 回傳 JSON 資料
# - response.text    → 回傳文字
# - response.status_code → 回傳狀態碼
```

#### Mock 測試程式碼

```python
from unittest.mock import patch

def test_get_user_name():
    # 第1步:用 patch 把 requests.get 換成假的
    with patch('requests.get') as mock_get:
        
        # 第2步:設定假的回傳值
        # 當有人呼叫 requests.get 時,回傳這個假資料
        mock_get.return_value.json.return_value = {"name": "Alice"}
        
        # 第3步:執行要測試的函數
        result = get_user_name(123)
        
        # 第4步:檢查結果
        assert result == "Alice"
        
        # 第5步:確認有呼叫 requests.get
        mock_get.assert_called_once_with("https://api.example.com/users/123")
```

### 逐行解釋

**第1步**: `with patch('requests.get') as mock_get:`
- 把真的 `requests.get` 暫時換成假的
- 就像把真的電話換成玩具電話

**第2步**: `mock_get.return_value.json.return_value = {"name": "Alice"}`
- 設定假資料
- 意思是:當有人呼叫這個假的 API 時,就回傳 `{"name": "Alice"}`

**第3步**: `result = get_user_name(123)`
- 執行要測試的函數
- 這時函數會用到假的 `requests.get`,不會真的連網路

**第4步**: `assert result == "Alice"`
- 檢查結果是否正確

**第5步**: `mock_get.assert_called_once_with(...)`
- 確認函數有正確呼叫 API
- 檢查網址是否正確

### 為什麼是 return_value.json.return_value?

因為原始程式碼是這樣呼叫的:

```python
response = requests.get(...)  # 第1層:呼叫 get()
data = response.json()         # 第2層:呼叫 json()
name = data["name"]            # 第3層:取得資料
```

所以 Mock 也要模擬這個「層層呼叫」的結構:

```python
mock_get.return_value.json.return_value = {"name": "Alice"}
#        ↑第1層回傳    ↑第2層方法 ↑第2層回傳值
```

### 圖解說明

```
真實情況:
requests.get("url") → Response 物件 → response.json() → {"name": "Alice"}

Mock 情況:
mock_get()          → mock_get.return_value → .json() → .return_value
   ↓                        ↓                    ↓            ↓
呼叫函數            回傳的物件              呼叫方法      方法的回傳值
```

### 記憶口訣

**每次看到 `()` 呼叫,就要加一層 `.return_value`**

```python
requests.get()           → mock_get.return_value
         ↑ 有括號!         ↑ 所以要 return_value

response.json()          → mock_get.return_value.json.return_value
             ↑ 又有括號!                              ↑ 又要 return_value

response.status_code     → mock_get.return_value.status_code
                ↑ 沒括號!                            ↑ 不用 return_value
```

### 對比:有方法 vs 沒方法

```python
# 情況1:呼叫方法 (需要 .return_value)
response.json()  # json 是方法,要加 ()
mock_get.return_value.json.return_value = {...}

# 情況2:只取屬性 (不需要 .return_value)
response.status_code  # status_code 是屬性,不用加 ()
mock_get.return_value.status_code = 200
```

---

## 10 種常見 Mock 用法

### 1. 直接使用 Mock 物件(不用 patch)

**情境**: 測試一個接受參數的函數

```python
# 原始程式碼
def process_data(database):
    data = database.fetch_all()
    return len(data)

# 測試
from unittest.mock import Mock

def test_process_data():
    # 直接建立一個假的 database
    fake_db = Mock()
    fake_db.fetch_all.return_value = [1, 2, 3, 4, 5]
    
    result = process_data(fake_db)
    
    assert result == 5
    fake_db.fetch_all.assert_called_once()
```

**用途**: 當你可以直接傳入假物件時,不需要用 patch

---

### 2. patch 裝飾器(decorator)

**不用 `with`,改用 `@patch`**

```python
from unittest.mock import patch
import os

# 原始程式碼
def get_username():
    return os.getenv("USERNAME")

# 測試方法1: 用 with
def test_get_username_with():
    with patch('os.getenv') as mock_getenv:
        mock_getenv.return_value = "Alice"
        assert get_username() == "Alice"

# 測試方法2: 用 @patch (更簡潔)
@patch('os.getenv')
def test_get_username_decorator(mock_getenv):
    mock_getenv.return_value = "Alice"
    assert get_username() == "Alice"
```

**用途**: 當整個測試函數都需要 mock 時,用 `@patch` 更簡潔

#### 參數順序總結

在 pytest 中,當 `@patch` 與其他功能混合使用時,參數順序遵循以下規則:

| 參數類型 | 位置 | 順序規則 |
|---------|------|---------|
| `self` | 第1位 | 類別方法必須有 |
| Fixtures | 第2位 | 任意順序(pytest 自動匹配) |
| `@pytest.mark.parametrize` | 第3位 | 必須與裝飾器定義順序一致 |
| `@patch` Mocks | 最後 | 由下往上(裝飾器順序) |

**記憶口訣**: `self → fixtures → parametrize → mocks`

#### 最複雜的範例:全部混合

```python
import pytest
from unittest.mock import patch, Mock

# 假設的原始程式碼
class UserService:
    def get_user_info(self, user_id, db, config):
        """從資料庫取得使用者資訊"""
        timeout = config.get('timeout', 30)
        logger.info(f"Fetching user {user_id} with timeout {timeout}")
        
        response = requests.get(
            f"https://api.example.com/users/{user_id}",
            timeout=timeout
        )
        
        user_data = response.json()
        db.save_cache(user_id, user_data)
        
        return user_data

# Fixtures
@pytest.fixture
def mock_db():
    """模擬資料庫連接"""
    db = Mock()
    db.save_cache.return_value = True
    return db

@pytest.fixture
def config():
    """測試配置"""
    return {"timeout": 30, "retry": 3}

# 測試類別
class TestUserService:
    
    @pytest.mark.parametrize("user_id, expected_name, expected_status", [
        (1, "Alice", 200),
        (2, "Bob", 200),
        (999, "Unknown", 404),
    ])
    @patch('logger.info')
    @patch('requests.get')
    def test_get_user_info_complex(
        self,           # 1. self (類別方法必須)
        mock_db,        # 2. fixture (任意順序)
        config,         # 3. fixture (任意順序)
        user_id,        # 4. parametrize 第1個參數
        expected_name,  # 5. parametrize 第2個參數
        expected_status,# 6. parametrize 第3個參數
        mock_get,       # 7. mock (對應下面的 @patch)
        mock_log        # 8. mock (對應上面的 @patch)
    ):
        """
        完整測試範例:
        - 使用類別方法 (self)
        - 使用 2 個 fixtures (mock_db, config)
        - 使用 parametrize 測試多組資料
        - 使用 2 個 @patch mock 外部依賴
        """
        # 設定 mock 的回傳值
        mock_response = Mock()
        mock_response.json.return_value = {
            "id": user_id,
            "name": expected_name,
            "status": expected_status
        }
        mock_response.status_code = expected_status
        mock_get.return_value = mock_response
        
        # 執行測試
        service = UserService()
        result = service.get_user_info(user_id, mock_db, config)
        
        # 驗證結果
        assert result["name"] == expected_name
        assert result["status"] == expected_status
        
        # 驗證 mock 被正確呼叫
        mock_get.assert_called_once_with(
            f"https://api.example.com/users/{user_id}",
            timeout=30
        )
        mock_log.assert_called_once()
        mock_db.save_cache.assert_called_once_with(user_id, result)
        
        # 根據不同的測試案例做額外驗證
        if expected_status == 404:
            assert result["name"] == "Unknown"
```

**這個範例展示了**:
1. ✅ 類別測試方法 (`self`)
2. ✅ 多個 fixtures (`mock_db`, `config`)
3. ✅ `@pytest.mark.parametrize` 測試多組資料
4. ✅ 多個 `@patch` mock 外部依賴
5. ✅ 完整的測試邏輯和驗證
6. ✅ 正確的參數順序

**執行結果**: 這個測試會執行 3 次(因為 parametrize 有 3 組資料),每次使用不同的 `user_id`、`expected_name` 和 `expected_status`。

---

### 3. Mock 多個東西

```python
from unittest.mock import patch

def send_email_and_log(email, message):
    email_service.send(email, message)
    logger.info(f"Email sent to {email}")
    return "Success"

# 同時 mock 兩個東西
@patch('logger.info')
@patch('email_service.send')
def test_send_email_and_log(mock_send, mock_log):
    # 注意:參數順序是反的!(由下往上)
    result = send_email_and_log("test@example.com", "Hello")
    
    assert result == "Success"
    mock_send.assert_called_once_with("test@example.com", "Hello")
    mock_log.assert_called_once()
```

**重點**: 多個 `@patch` 時,參數順序是**由下往上**

---

### 4. Mock 會拋出例外的情況

**用途**: 模擬外部依賴拋出例外,測試程式碼的錯誤處理邏輯

> **注意**: 這與 `pytest.raises()` 不同!
> - `pytest.raises()`: 測試你的程式碼**應該拋出**例外
> - `side_effect`: 模擬外部依賴拋出例外,測試你的程式碼**如何處理**例外

```python
from unittest.mock import patch
import requests

# 原始程式碼
def fetch_user_data(user_id):
    """從 API 取得使用者資料"""
    try:
        response = requests.get(f"https://api.example.com/users/{user_id}")
        return response.json()
    except requests.ConnectionError:
        return {"error": "Network error", "user_id": user_id}
    except requests.Timeout:
        return {"error": "Request timeout", "user_id": user_id}

# 測試1: 模擬網路連線錯誤
@patch('requests.get')
def test_fetch_user_data_connection_error(mock_get):
    # 讓 mock 拋出 ConnectionError
    mock_get.side_effect = requests.ConnectionError("Network failed")
    
    result = fetch_user_data(123)
    
    # 驗證程式正確處理網路錯誤
    assert result["error"] == "Network error"
    assert result["user_id"] == 123

# 測試2: 模擬請求超時
@patch('requests.get')
def test_fetch_user_data_timeout(mock_get):
    # 讓 mock 拋出 Timeout
    mock_get.side_effect = requests.Timeout("Request timeout")
    
    result = fetch_user_data(456)
    
    # 驗證程式正確處理超時
    assert result["error"] == "Request timeout"
    assert result["user_id"] == 456

# 測試3: 對比 - 用 pytest.raises 測試應該拋出的例外
import pytest

def validate_user_id(user_id):
    """驗證使用者 ID"""
    if user_id <= 0:
        raise ValueError("User ID must be positive")
    return True

def test_validate_user_id_negative():
    # 這裡用 pytest.raises,因為我們測試「應該拋出」例外
    with pytest.raises(ValueError, match="User ID must be positive"):
        validate_user_id(-1)
```

**使用情境**:
- ✅ 測試網路錯誤處理(ConnectionError, Timeout)
- ✅ 測試資料庫連線失敗處理
- ✅ 測試外部 API 失敗的容錯機制
- ✅ 測試檔案讀取失敗的處理

---

### 5. Mock 回傳不同的值(多次呼叫)

**用途**: 模擬每次呼叫回傳不同結果,適合測試重試機制、分頁、輪詢等場景

#### 基本用法

```python
from unittest.mock import Mock

def test_multiple_calls_basic():
    mock_func = Mock()
    
    # 第1次呼叫回傳 1,第2次回傳 2,第3次回傳 3
    mock_func.side_effect = [1, 2, 3]
    
    assert mock_func() == 1
    assert mock_func() == 2
    assert mock_func() == 3
```

#### 實際應用 1: 測試重試機制

```python
from unittest.mock import patch
import requests

# 原始程式碼
def fetch_data_with_retry(url, max_retries=3):
    """帶重試機制的資料抓取"""
    for attempt in range(max_retries):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.json()
        except requests.ConnectionError:
            if attempt == max_retries - 1:
                raise
            continue
    return None

# 測試:第1次失敗,第2次成功
@patch('requests.get')
def test_fetch_data_retry_success(mock_get):
    # 第1次拋出例外,第2次成功
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"data": "success"}
    
    mock_get.side_effect = [
        requests.ConnectionError("Network error"),  # 第1次失敗
        mock_response                                # 第2次成功
    ]
    
    result = fetch_data_with_retry("https://api.example.com/data")
    
    assert result == {"data": "success"}
    assert mock_get.call_count == 2  # 確認呼叫了2次
```

#### 實際應用 2: 測試分頁 API

```python
from unittest.mock import patch

# 原始程式碼
def fetch_all_users():
    """抓取所有使用者(分頁)"""
    all_users = []
    page = 1
    
    while True:
        response = requests.get(f"https://api.example.com/users?page={page}")
        data = response.json()
        
        if not data["users"]:
            break
            
        all_users.extend(data["users"])
        page += 1
        
        if page > 10:  # 安全機制
            break
    
    return all_users

# 測試:模擬3頁資料
@patch('requests.get')
def test_fetch_all_users_pagination(mock_get):
    # 建立3頁的假資料
    page1 = Mock()
    page1.json.return_value = {"users": [{"id": 1}, {"id": 2}]}
    
    page2 = Mock()
    page2.json.return_value = {"users": [{"id": 3}, {"id": 4}]}
    
    page3 = Mock()
    page3.json.return_value = {"users": []}  # 空頁面,表示結束
    
    # 設定每次呼叫回傳不同頁面
    mock_get.side_effect = [page1, page2, page3]
    
    result = fetch_all_users()
    
    # 驗證結果
    assert len(result) == 4
    assert result[0]["id"] == 1
    assert result[3]["id"] == 4
    assert mock_get.call_count == 3
```

#### 實際應用 3: 測試輪詢機制

```python
from unittest.mock import patch
import time

# 原始程式碼
def wait_for_job_completion(job_id, timeout=10):
    """等待工作完成"""
    start_time = time.time()
    
    while time.time() - start_time < timeout:
        response = requests.get(f"https://api.example.com/jobs/{job_id}")
        status = response.json()["status"]
        
        if status == "completed":
            return True
        elif status == "failed":
            return False
            
        time.sleep(1)
    
    return False  # 超時

# 測試:模擬工作從 pending → running → completed
@patch('time.sleep')  # Mock sleep 避免真的等待
@patch('time.time')
@patch('requests.get')
def test_wait_for_job_completion(mock_get, mock_time, mock_sleep):
    # Mock time.time() 回傳遞增的時間
    mock_time.side_effect = [0, 1, 2, 3]  # 模擬時間流逝
    
    # Mock API 回傳不同狀態
    response1 = Mock()
    response1.json.return_value = {"status": "pending"}
    
    response2 = Mock()
    response2.json.return_value = {"status": "running"}
    
    response3 = Mock()
    response3.json.return_value = {"status": "completed"}
    
    mock_get.side_effect = [response1, response2, response3]
    
    result = wait_for_job_completion("job123")
    
    assert result is True
    assert mock_get.call_count == 3
```

#### 混合使用: 回傳值 + 例外

```python
from unittest.mock import Mock, patch
import requests

# 原始程式碼
def robust_api_call(url, max_retries=3):
    """強健的 API 呼叫(處理各種錯誤)"""
    for attempt in range(max_retries):
        try:
            response = requests.get(url)
            return response.json()
        except (requests.ConnectionError, requests.Timeout):
            if attempt == max_retries - 1:
                return {"error": "Max retries exceeded"}
            continue
    return None

# 測試:混合例外和成功回應
@patch('requests.get')
def test_robust_api_call_mixed(mock_get):
    success_response = Mock()
    success_response.json.return_value = {"data": "success"}
    
    # 第1次: ConnectionError
    # 第2次: Timeout
    # 第3次: 成功
    mock_get.side_effect = [
        requests.ConnectionError("Network error"),
        requests.Timeout("Request timeout"),
        success_response
    ]
    
    result = robust_api_call("https://api.example.com/data")
    
    assert result == {"data": "success"}
    assert mock_get.call_count == 3
```

#### 使用情境總結

| 情境 | 說明 | 範例 |
|------|------|------|
| **重試機制** | 第1次失敗,後續成功 | API 呼叫重試 |
| **分頁處理** | 每次回傳不同頁資料 | 抓取所有使用者 |
| **輪詢狀態** | 狀態逐漸變化 | 等待工作完成 |
| **混合情境** | 例外 + 成功回應 | 強健的錯誤處理 |
| **資料變化** | 模擬資料隨時間改變 | 庫存數量變化 |

---

### 6. 檢查 Mock 被呼叫的次數和參數

```python
from unittest.mock import Mock

def test_call_verification():
    mock_func = Mock()
    
    mock_func("hello")
    mock_func("world")
    mock_func("hello")
    
    # 檢查總共被呼叫幾次
    assert mock_func.call_count == 3
    
    # 檢查是否被呼叫過(至少一次)
    mock_func.assert_called()
    
    # 檢查最後一次呼叫的參數
    mock_func.assert_called_with("hello")
    
    # 檢查是否只被呼叫一次(會失敗,因為呼叫了3次)
    # mock_func.assert_called_once()
    
    # 檢查是否用特定參數呼叫過
    mock_func.assert_any_call("world")
```

---

### 7. patch.object - Mock 物件的方法

```python
from unittest.mock import patch

class Calculator:
    def add(self, a, b):
        return a + b
    
    def multiply(self, a, b):
        return self.add(a, 0) * b  # 用到 add 方法

def test_multiply():
    calc = Calculator()
    
    # 只 mock Calculator 的 add 方法
    with patch.object(calc, 'add', return_value=10):
        result = calc.multiply(5, 3)
        assert result == 30  # 10 * 3
```

**用途**: 只 mock 物件的某個方法,其他方法保持正常

---

### 8. Mock 檔案讀取

```python
from unittest.mock import mock_open, patch

def read_config():
    with open('config.txt', 'r') as f:
        return f.read()

def test_read_config():
    # mock_open 專門用來 mock 檔案操作
    fake_file_content = "username=admin\npassword=secret"
    
    with patch('builtins.open', mock_open(read_data=fake_file_content)):
        result = read_config()
        assert "username=admin" in result
```

**用途**: 測試檔案讀寫,不需要真的建立檔案

---

### 9. Mock 時間

```python
from unittest.mock import patch
from datetime import datetime

def get_current_year():
    return datetime.now().year

def test_get_current_year():
    # Mock datetime.now()
    fake_time = datetime(2025, 1, 1)
    
    with patch('datetime.datetime') as mock_datetime:
        mock_datetime.now.return_value = fake_time
        
        result = get_current_year()
        assert result == 2025
```

**用途**: 控制測試中的時間

---

### 10. MagicMock - 支援魔術方法

```python
from unittest.mock import MagicMock

def test_magic_methods():
    # MagicMock 支援 __len__, __iter__ 等魔術方法
    mock_list = MagicMock()
    mock_list.__len__.return_value = 3
    mock_list.__iter__.return_value = iter([1, 2, 3])
    
    assert len(mock_list) == 3
    assert list(mock_list) == [1, 2, 3]
```

---

## 常用方法總結

| 方法 | 用途 |
|------|------|
| `Mock()` | 建立基本 mock 物件 |
| `MagicMock()` | 建立支援魔術方法的 mock 物件 |
| `patch()` | 暫時替換模組/函數 |
| `patch.object()` | 替換物件的方法 |
| `mock_open()` | Mock 檔案操作 |
| `return_value` | 設定回傳值 |
| `side_effect` | 設定例外或多個回傳值 |
| `assert_called()` | 檢查是否被呼叫 |
| `assert_called_once()` | 檢查是否只被呼叫一次 |
| `assert_called_with()` | 檢查呼叫的參數 |
| `assert_called_once_with()` | 檢查是否只用特定參數呼叫一次 |
| `assert_any_call()` | 檢查是否用特定參數呼叫過 |
| `call_count` | 取得呼叫次數 |

---

## 實戰建議

1. **簡單情況**: 直接用 `Mock()`
2. **需要替換模組**: 用 `patch()`
3. **需要替換物件方法**: 用 `patch.object()`
4. **檔案操作**: 用 `mock_open()`
5. **測試例外**: 用 `side_effect`
6. **需要魔術方法**: 用 `MagicMock()`

### 選擇 Mock 的流程圖

```
需要 Mock 嗎?
├─ 否 → 直接測試
└─ 是 → 
    ├─ 可以直接傳入假物件? 
    │   └─ 是 → 用 Mock()
    └─ 需要替換模組/函數?
        ├─ 是 → 用 patch()
        └─ 只需要替換物件的某個方法?
            └─ 是 → 用 patch.object()
```

---

## 實戰踩坑筆記

以下是實際練習時常見的觀念錯誤，整理供複習。

---

### 坑 1：patch 路徑要寫「使用它的地方」，不是「定義它的地方」

```python
# exercises.py
import requests

def get_device_info(device_id):
    response = requests.get(...)  # ← 這裡用的是 exercises 模組裡的 requests
```

```python
# ❌ 錯誤：patch 了全域的 requests.get，exercises.py 不受影響
with patch("requests.get") as mock_get:
    ...

# ✅ 正確：patch exercises 模組裡的 requests.get
with patch("interview.pytest_drills.day06_mock.exercises.requests.get") as mock_get:
    ...
```

**口訣**：`patch("哪個模組用到它.那個名稱")`

---

### 坑 2：patch 路徑只能用絕對路徑，不支援相對路徑

```python
# ❌ 不支援，會報錯
@patch(".exercises.requests.get")

# ✅ 正確，完整絕對路徑
@patch("interview.pytest_drills.day06_mock.exercises.requests.get")
```

**技巧**：可以用常數縮短路徑：
```python
MODULE = "interview.pytest_drills.day06_mock.exercises"

@patch(f"{MODULE}.requests.get")
```

---

### 坑 3：`raise` vs `raise SomeException(...)`

```python
except requests.Timeout:
    if attempt == max_retries - 1:
        raise                                    # 重新拋出當前 catch 到的例外（類型不變）
        raise requests.ConnectionError("...")    # 拋出全新的例外（類型由你指定）
```

| 寫法 | 行為 |
|------|------|
| `raise` | 重新拋出當前 catch 到的例外，類型和訊息都不變 |
| `raise SomeException("msg")` | 拋出全新的例外，類型和訊息由你決定 |

---

### 坑 4：`pytest.raises` with 區塊內的 assert 不會執行

```python
# ❌ 錯誤：例外拋出後 with 區塊立刻結束，下面的 assert 永遠不會執行
with pytest.raises(Exception) as exc_info:
    some_function()
    assert exc_info.type == SomeError   # ← 不會執行！假的通過！
    assert mock.call_count == 3         # ← 不會執行！

# ✅ 正確：assert 要寫在 with 區塊外面
with pytest.raises(requests.Timeout):
    some_function()

assert mock.call_count == 3             # ← 這才會真正被驗證
```

---

### 坑 5：`Mock()` 直接建立 vs `patch()` 替換函數

```python
# Mock() → 代表「回傳值物件」本身，直接設定屬性
mock_response = Mock()
mock_response.status_code = 200
mock_response.json.return_value = {"status": "ok"}

# patch() → 代表「函數」本身，需要 .return_value 才能存取回傳值
with patch("...requests.get") as mock_get:
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"status": "ok"}
```

**口訣**：`patch()` 拿到的是函數，`.return_value` 才是函數被呼叫後回傳的物件。

```
mock_get()              → mock_get.return_value   （呼叫函數，取得回傳值）
mock_get().json()       → mock_get.return_value.json.return_value
mock_get().status_code  → mock_get.return_value.status_code   （屬性，不需要 return_value）
```

---

### 坑 6：`return_value` 和 `side_effect` 是同一層的屬性

兩者都是設定在 **Mock 物件本身**上，控制的是「這個 Mock 被呼叫時的行為」：

```python
mock_get.return_value = mock_response   # 每次呼叫都回傳同一個值
mock_get.side_effect  = [r1, r2, r3]   # 每次呼叫依序回傳不同值（覆蓋 return_value）
```

因此，你可以選擇在**不同層**控制「多次呼叫的不同結果」：

```python
# 方式 A：在 mock_get 這層控制（每次 requests.get() 回傳不同物件）
mock_get.side_effect = [mock_response1, mock_response2]

# 方式 B：在 json 這層控制（每次 requests.get() 回傳同一物件，但 json() 結果不同）
mock_get.return_value = mock_response
mock_response.json.side_effect = [{"status": "processing"}, {"status": "ready"}]
```

兩種方式結果等價，差別只在你想在哪一層模擬「變化」。

---

## 練習題

請參考 `exercises.py` 和 `test_day06_mock.py` 進行練習。

---

## 參考資源

- [Python unittest.mock 官方文件](https://docs.python.org/3/library/unittest.mock.html)
- [Real Python - Understanding the Python Mock Object Library](https://realpython.com/python-mock-library/)
