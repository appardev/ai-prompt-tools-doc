# 🚗 Mochi AI Docs p4t5 文件

本文件由 AI 依據 `mochi-prompt-v4.txt` 及 `mochi-tools-v5.py` 整理後生成。

## 📖 使用指南

### 🎯 產品介紹
「車麻吉」是一個專注於出行服務的應用程式，提供以下核心功能：
- 停車位搜尋與支付
- 加油站搜尋與支付
- 停車場與加油站優惠資訊

### 💡 特色功能
1. **Autopass 快速通**：讓開車族與機車族在停車場、加油站及路邊停車時，不必再浪費時間繳費
2. **加油條碼付款**：透過綁定付款方式與設定交易安全碼，在支援的人工加油站向站員出示條碼即可快速完成付款
3. **麻吉付加油站**：車麻吉中的一種加油付款方式

### 🔍 搜尋原則

#### 停車場挑選原則
1. 只能選擇營業中的停車場
2. 優先順序：
   - 距離近
   - 價格便宜
   - 即時車位還有 10 個以上或總車位數 50 個以上
3. 優先推薦：
   - 車麻吉合作場
   - 銀行免費停車（若該用戶的銀行免費停車設定中，有分成「車麻吉合作」和「非車麻吉合作」，若是「車麻吉合作」則優先推薦）
4. 優先搜尋的步行範圍
5. 優先推薦有當日最高金額
6. 優先推薦室內停車場
7. 優先推薦有遮雨棚停車場（室外可）

#### 加油站挑選原則
1. 預設搜尋半徑是 10,000 公尺
2. 「距離近」為優先考量
3. 只選擇當前營業中

### 🗺️ 導航選擇原則
1. 如果是市區，距離近的請使用 `start_navigation_in_app`
2. 如果是跨縣市，預計要上快速道路或是國道的，請使用 `start_navigation_google_map`
3. 如果使用者有特別指定，再使用 `in_app`, `google_map`, 或是 `apple_map`
4. 如果無法選擇，預設是 `start_navigation_in_app`

### 📱 回覆原則
1. 回覆應簡短（約 40 個字以內）
2. 避免朗讀地址，因為使用者在開車，非常簡潔的回答才能讓使用者快速做決策
3. 回覆中不要提到網址，若有網址，請使用開啟網址的工具，直接為使用者開啟網址
4. 若使用者詢問任意一般地標，在查詢完之後，都要記得詢問使用者「是否要導航過去？」
5. 若使用者詢問租車行，在查詢完之後，都要記得詢問使用者「您是否要進一步完成行駕照驗證？」

### 🔄 工具使用流程

#### 搜尋 A 地附近的 B 地標（例如：「幫我找南港軟體園區附近的星巴克」）
1. 使用 `place_search` 找到 A 地標（南港軟體園區）的經緯度
2. 使用 `place_search` 找用 A 地標的座標，搜尋附近的 B 地標（星巴克）
3. 使用 `show_general_pois_on_map` 把 B 地標畫在地圖上給使用者

#### 協助使用者找附近停車場（例如：「幫我找大巨蛋附近的停車場」）
1. 使用 `place_search` 找到大巨蛋的經緯度
2. 使用 `get_parkinglots` 使用大巨蛋經緯度，找到附近的停車場
3. 使用 `recommend_best_poi_with_route_on_map` 標記與畫線，推薦最好的一個
4. 最後詢問是否需要導航

#### 協助使用者直接導航（例如：「幫我導航到大安森林公園」）
1. 使用 `place_search` 工具，找到最符合請求的地點的經緯度
2. 使用 `get_route_planning` 畫線在地圖上，或是使用 `start_navigation_xxx` 工具，來開啟導航模式

#### 搜尋銀行優惠停車場（例如：「幫我找台新銀行的優惠停車場」）
1. 使用 `get_discount_parkinglot_brand_by_bank` 找到優惠停車場的品牌
2. 使用 `get_parkinglots` 的 brand 參數幫使用者找停車場

### 📍 waypoints 參數使用說明

waypoints 參數用於規劃多點導航路線，常見於以下工具：
- `start_navigation_in_app`
- `recommend_best_poi_with_route_on_map`
- `get_route_planning`

#### waypoints 基本結構
每個 waypoint 包含以下必要參數：
- `lat`：緯度
- `lng`：經度
- `mark_type`：標記類型
- `arrival_method`：到達方式
- `mark_name`：標記名稱

#### 標記類型 (mark_type)
- `user_location`：使用者位置
- `parkinglot`：停車場
- `gas_station`：加油站
- `waypoint`：路徑點
- `destination`：目的地

#### 到達方式 (arrival_method)
- `drive`：開車
- `walk`：步行

#### 常見使用情境

1. **停車場到目的地**：
   ```
   waypoints: [
     {lat: 25.0330, lng: 121.5654, mark_type: "parkinglot", arrival_method: "drive", mark_name: "台北車站停車場"},
     {lat: 25.0340, lng: 121.5664, mark_type: "destination", arrival_method: "walk", mark_name: "台北101"}
   ]
   ```
   這表示：開車到停車場，然後步行到目的地

2. **多點導航**：
   ```
   waypoints: [
     {lat: 25.0330, lng: 121.5654, mark_type: "waypoint", arrival_method: "drive", mark_name: "中繼點A"},
     {lat: 25.0340, lng: 121.5664, mark_type: "waypoint", arrival_method: "drive", mark_name: "中繼點B"},
     {lat: 25.0350, lng: 121.5674, mark_type: "destination", arrival_method: "drive", mark_name: "最終目的地"}
   ]
   ```
   這表示：開車經過多個中繼點到達目的地

3. **混合交通方式**：
   ```
   waypoints: [
     {lat: 25.0330, lng: 121.5654, mark_type: "parkinglot", arrival_method: "drive", mark_name: "信義區停車場"},
     {lat: 25.0340, lng: 121.5664, mark_type: "waypoint", arrival_method: "walk", mark_name: "信義商圈"},
     {lat: 25.0350, lng: 121.5674, mark_type: "destination", arrival_method: "walk", mark_name: "台北101"}
   ]
   ```
   這表示：開車到停車場，然後步行經過商圈到達目的地

#### 注意事項
1. 使用者位置不需要放入 waypoints，系統會自動從使用者位置開始規劃路線
2. 每個 waypoint 的到達方式會影響路線規劃，例如：步行和開車的路線會不同
3. 標記類型會影響地圖上的顯示方式，例如：停車場會顯示停車場圖標
4. 路線會按照 waypoints 的順序規劃，請確保順序正確

---

## 📦 工具總覽

| 工具名稱 | 功能說明 |
|----|----|
| `get_parkinglots` | 獲取指定中心點座標附近停車場 |
| `get_gas_stations` | 獲取指定中心點座標附近的加油站 |
| `get_car_rental_stores` | 獲取指定中心點座標附近的租車行 |
| `start_navigation_in_app` | 開啟 app 內導航到地點 |
| `start_navigation_google_map` | 開啟 Google Map 導航到地點 |
| `start_navigation_apple_map` | 開啟 Apple Map 導航到地點 |
| `place_search` | 搜尋某個座標點的附近地點資訊 |
| `recommend_best_poi_with_route_on_map` | 推薦最佳 POI 並在地圖上顯示路線 |
| `recommend_more_pois_on_map` | 推薦更多 POI 並在地圖上顯示 |
| `get_route_planning` | 抓取導航規劃後的結果並在地圖上繪製路線 |
| `mark_parked_here` | 在 in-app 地圖上標記使用者目前停車的位置 |
| `get_weather_info` | 取得某個座標點的氣象資訊 |
| `parse_google_map_url` | 解析 Google Map 網址 |
| `open_store_homepage_website` | 開啟商店的網站 |
| `open_web_page` | 開啟網站 |
| `show_general_pois_on_map` | 在地圖上標記一般性地標 |
| `open_poi_street_view` | 開啟特定 POI 的街景 |
| `get_discount_parkinglot_brand_by_bank` | 取得特定銀行的停車場品牌列表 |
| `get_discount_parkinglot_brand_by_credit_card` | 取得特定信用卡的停車場品牌列表 |

---

## 🅿️ 1. `get_parkinglots`

**說明**：獲取指定中心點座標附近停車場，座標不一定是使用者的位置，例如：使用者可能會詢問某個地標附近的停車場。

**參數定義**：

| 參數名稱 | 類型 | 是否必填 | 說明 |
|----|---|----|---|
| `center_spot_lat` | `number` | ❌ 否 | 中心點緯度 |
| `center_spot_lng` | `number` | ❌ 否 | 中心點經度 |
| `min_price` | `integer` | ❌ 否 | 最低價格 |
| `center_spot_name` | `string` | ❌ 否 | 中心點名稱，例如：使用者位置、某個地標 |
| `max_price` | `integer` | ❌ 否 | 最高價格 |
| `is_cooperated` | `boolean` | ❌ 否 | 支援車麻吉付款 |
| `brand` | `string` | ❌ 否 | 停車場指定品牌（嘟嘟房、台灣聯通...） |
| `destination_lat` | `number` | ❌ 否 | 終點緯度，用來判斷方向並進行導航 |
| `destination_lng` | `number` | ❌ 否 | 終點經度，用來判斷方向並進行導航 |
| `search_radius` | `integer` | ✅ 是 | 搜尋半徑，單位為公尺, 預設是 1600 公尺，可擴大到 2500 公尺 |
| `height_limit` | `integer` | ❌ 否 | 高度限制，單位為公分 |
| `supports_charging` | `boolean` | ❌ 否 | 是否支援充電 |
| `is_mechanical` | `boolean` | ❌ 否 | 是否為機械式停車場 |
| `building_type` | `string` | ❌ 否 | 停車場室內外類型，例如：indoor, outdoor |
| `autopass_payment_type` | `string` | ❌ 否 | 車麻吉付款指定方式（還沒實作），選項有：麻吉付、快速通、條碼付、掃碼付 |

**範例**：
```json
{
  "center_spot_lat": 25.0330,
  "center_spot_lng": 121.5654,
  "search_radius": 2000,
  "brand": "嘟嘟房",
  "is_cooperated": true
}
```

---

## ⛽ 2. `get_gas_stations`

**說明**：獲取指定中心點座標附近的加油站。

**參數定義**：

| 參數名稱 | 類型 | 是否必填 | 說明 |
|----|---|----|---|
| `center_spot_lat` | `number` | ❌ 否 | 中心點緯度 |
| `center_spot_lng` | `number` | ❌ 否 | 中心點經度 |
| `center_spot_name` | `string` | ❌ 否 | 中心點名稱，例如：使用者位置、某個地標 |
| `brand` | `string` | ❌ 否 | 加油站品牌，台灣的加油站有：中油、台塑（台亞）、全國、山隆、西歐、速邁樂 Smile、北基、車容坊、台糖 |
| `supplier` | `string` | ❌ 否 | 供應商，選項有：台塑、中油 |
| `gas_types` | `string` | ❌ 否 | 支援油品類型，單選，選項有：92、95、98、柴油 |
| `is_support_self_service` | `boolean` | ❌ 否 | 是否支援自助加油 |
| `destination_lat` | `number` | ❌ 否 | 終點緯度，用來判斷方向並進行導航 |
| `destination_lng` | `number` | ❌ 否 | 終點經度，用來判斷方向並進行導航 |
| `search_radius` | `integer` | ✅ 是 | 搜尋半徑，單位為公尺, 預設是 10000 公尺 |

**範例**：
```json
{
  "center_spot_lat": 25.0330,
  "center_spot_lng": 121.5654,
  "search_radius": 5000,
  "brand": "中油",
  "gas_types": "95"
}
```

---

## 🚗 3. `get_car_rental_stores`

**說明**：獲取指定中心點座標附近的租車行。

**參數定義**：

| 參數名稱 | 類型 | 是否必填 | 說明 |
|----|---|----|---|
| `center_spot_lat` | `number` | ✅ 是 | 中心點緯度 |
| `center_spot_lng` | `number` | ✅ 是 | 中心點經度 |

**範例**：
```json
{
  "center_spot_lat": 25.0330,
  "center_spot_lng": 121.5654
}
```

---

## 🗺️ 4. `start_navigation_in_app`

**說明**：開啟 app 內導航到地點。

**參數定義**：

| 參數名稱 | 類型 | 是否必填 | 說明 |
|----|---|----|---|
| `start_lat` | `number` | ✅ 是 | 起點緯度，可以是使用者目前所在位置或是任意座標 |
| `start_lng` | `number` | ✅ 是 | 起點經度可以是使用者目前所在位置或是任意座標 |
| `waypoints` | `array` | ✅ 是 | 路徑點陣列，用於規劃多點導航路線 |

**waypoints 陣列項目**：

| 參數名稱 | 類型 | 是否必填 | 說明 |
|----|---|----|---|
| `lat` | `number` | ✅ 是 | 路徑點緯度 |
| `lng` | `number` | ✅ 是 | 路徑點經度 |
| `mark_type` | `string` | ✅ 是 | 標記類型，選項有：parkinglot、gas_station、waypoint、destination、user_location |
| `arrival_method` | `string` | ✅ 是 | 到達該地標的方式，選項有：drive、walk |
| `mark_name` | `string` | ✅ 是 | 標記名稱，例如：停車場名稱、目的地名稱 |

**使用範例**：

1. **簡單導航**：
```json
{
  "start_lat": 25.0330,
  "start_lng": 121.5654,
  "waypoints": [
    {
      "lat": 25.0340,
      "lng": 121.5664,
      "mark_type": "destination",
      "arrival_method": "drive",
      "mark_name": "台北101"
    }
  ]
}
```

2. **停車場到目的地**：
```json
{
  "start_lat": 25.0330,
  "start_lng": 121.5654,
  "waypoints": [
    {
      "lat": 25.0335,
      "lng": 121.5659,
      "mark_type": "parkinglot",
      "arrival_method": "drive",
      "mark_name": "信義區停車場"
    },
    {
      "lat": 25.0340,
      "lng": 121.5664,
      "mark_type": "destination",
      "arrival_method": "walk",
      "mark_name": "台北101"
    }
  ]
}
```

3. **多點導航**：
```json
{
  "start_lat": 25.0330,
  "start_lng": 121.5654,
  "waypoints": [
    {
      "lat": 25.0335,
      "lng": 121.5659,
      "mark_type": "waypoint",
      "arrival_method": "drive",
      "mark_name": "中繼點A"
    },
    {
      "lat": 25.0340,
      "lng": 121.5664,
      "mark_type": "waypoint",
      "arrival_method": "drive",
      "mark_name": "中繼點B"
    },
    {
      "lat": 25.0345,
      "lng": 121.5669,
      "mark_type": "destination",
      "arrival_method": "drive",
      "mark_name": "最終目的地"
    }
  ]
}
```

---

## 🗺️ 5. `start_navigation_google_map`

**說明**：開啟 Google Map 導航到地點。

**參數定義**：

| 參數名稱 | 類型 | 是否必填 | 說明 |
|----|---|----|---|
| `google_map_query` | `string` | ✅ 是 | Google Map 查詢字串，直接回傳引數部分的字串就好，也不需要任何單引號或是雙引號。saddr 是起點，daddr 是終點，waypoints 是中間點，directionsmode 是導航模式，driving 是開車，walking 是步行 |

**範例**：
```json
{
  "google_map_query": "saddr=25.0330,121.5654&daddr=25.0340,121.5664&directionsmode=driving"
}
```

**多點導航範例**：
```json
{
  "google_map_query": "saddr=25.0330,121.5654&daddr=25.0340,121.5664+to:25.0350,121.5674+to:25.0360,121.5684&directionsmode=driving"
}
```

---

## 🗺️ 6. `start_navigation_apple_map`

**說明**：開啟 Apple Map 導航到地點。

**參數定義**：

| 參數名稱 | 類型 | 是否必填 | 說明 |
|----|---|----|---|
| `lat` | `number` | ✅ 是 | 目的地緯度 |
| `lng` | `number` | ✅ 是 | 目的地經度 |

**範例**：
```json
{
  "lat": 25.0340,
  "lng": 121.5664
}
```

---

## 🔍 7. `place_search`

**說明**：搜尋某個座標點的附近地點資訊，並回傳地點資訊。

**參數定義**：

| 參數名稱 | 類型 | 是否必填 | 說明 |
|----|---|----|---|
| `query` | `string` | ✅ 是 | 搜尋關鍵字 |
| `center_spot_lat` | `number` | ✅ 是 | 中心點緯度 |
| `center_spot_lng` | `number` | ✅ 是 | 中心點經度 |

**範例**：
```json
{
  "query": "星巴克",
  "center_spot_lat": 25.0330,
  "center_spot_lng": 121.5654
}
```

---

## 🗺️ 8. `recommend_best_poi_with_route_on_map`

**說明**：依照使用者的偏好或對話裡需求，挑選出來適合的停車場或是加油站。若使用這個工具，UI 會在地圖上標記出來。也同時畫出導航路線在地圖上。在規劃路線的 waypoints 中，請依照提示詞的設定，規劃出適合的路徑。

**參數定義**：

| 參數名稱 | 類型 | 是否必填 | 說明 |
|----|---|----|---|
| `poi_id` | `string` | ✅ 是 | 停車場或加油站的 ID, 例如: d19bb199-b3bd-488c-9b76-f5a3907961fb |
| `poi_type` | `string` | ✅ 是 | POI 的類型，選項有：parkinglot、gas_station |
| `waypoints` | `array` | ✅ 是 | 依照使用者請求規劃的路徑點陣列 |

**waypoints 陣列項目**：

| 參數名稱 | 類型 | 是否必填 | 說明 |
|----|---|----|---|
| `lat` | `number` | ✅ 是 | 路徑點緯度 |
| `lng` | `number` | ✅ 是 | 路徑點經度 |
| `mark_type` | `string` | ✅ 是 | 標記類型，選項有：parkinglot、gas_station、waypoint、destination、user_location |
| `arrival_method` | `string` | ✅ 是 | 到達該地標的方式，選項有：drive、walk |
| `mark_name` | `string` | ✅ 是 | 標記名稱，例如：停車場名稱、目的地名稱 |

**使用範例**：

1. **停車場到目的地**：
```json
{
  "poi_id": "d19bb199-b3bd-488c-9b76-f5a3907961fb",
  "poi_type": "parkinglot",
  "waypoints": [
    {
      "lat": 25.0335,
      "lng": 121.5659,
      "mark_type": "parkinglot",
      "arrival_method": "drive",
      "mark_name": "信義區停車場"
    },
    {
      "lat": 25.0340,
      "lng": 121.5664,
      "mark_type": "destination",
      "arrival_method": "walk",
      "mark_name": "台北101"
    }
  ]
}
```

2. **加油站到目的地**：
```json
{
  "poi_id": "e29cc2a0-c4ce-499d-0a87-f6b5019072gc",
  "poi_type": "gas_station",
  "waypoints": [
    {
      "lat": 25.0335,
      "lng": 121.5659,
      "mark_type": "gas_station",
      "arrival_method": "drive",
      "mark_name": "中油信義站"
    },
    {
      "lat": 25.0340,
      "lng": 121.5664,
      "mark_type": "destination",
      "arrival_method": "drive",
      "mark_name": "台北101"
    }
  ]
}
```

---

## 🗺️ 9. `recommend_more_pois_on_map`

**說明**：當使用者不滿意原先的推薦的停車場或加油站的 POI 而再詢問「請幫我找更多」時，請使用已經取得的停車場或是加油站（同一種類型的 POI），當成參數使用這個工具列出來給使用者，最多三個。

**參數定義**：

| 參數名稱 | 類型 | 是否必填 | 說明 |
|----|---|----|---|
| `candidate_pois` | `array` | ✅ 是 | 候選停車場的餘位和價格資訊陣列 |

**candidate_pois 陣列項目**：

| 參數名稱 | 類型 | 是否必填 | 說明 |
|----|---|----|---|
| `poi_id` | `string` | ✅ 是 | 停車場或加油站的 ID, 例如: d19bb199-b3bd-488c-9b76-f5a3907961fb |
| `poi_type` | `string` | ✅ 是 | POI 的類型，例如：parkinglot 或 gas_station |

**範例**：
```json
{
  "candidate_pois": [
    {
      "poi_id": "d19bb199-b3bd-488c-9b76-f5a3907961fb",
      "poi_type": "parkinglot"
    },
    {
      "poi_id": "e29cc2a0-c4ce-499d-0a87-f6b5019072gc",
      "poi_type": "parkinglot"
    },
    {
      "poi_id": "f3add3b1-d5df-5aae-1b98-g7c6120183hd",
      "poi_type": "parkinglot"
    }
  ]
}
```

---

## 🗺️ 10. `get_route_planning`

**說明**：抓取導航規劃後的結果，同時在地圖上繪製導航路線，可以多點多交通方式導航。

**參數定義**：

| 參數名稱 | 類型 | 是否必填 | 說明 |
|----|---|----|---|
| `start_lat` | `number` | ✅ 是 | 起點緯度，可以是使用者目前所在位置或是任意座標 |
| `start_lng` | `number` | ✅ 是 | 起點經度，可以是使用者目前所在位置或是任意座標 |
| `waypoints` | `array` | ✅ 是 | 路徑點陣列，用於規劃多點導航路線 |

**waypoints 陣列項目**：

| 參數名稱 | 類型 | 是否必填 | 說明 |
|----|---|----|---|
| `lat` | `number` | ✅ 是 | 路徑點緯度 |
| `lng` | `number` | ✅ 是 | 路徑點經度 |
| `mark_type` | `string` | ✅ 是 | 標記類型，選項有：parkinglot、gas_station、waypoint、destination |
| `arrival_method` | `string` | ✅ 是 | 到達該地標的方式，選項有：drive、walk |
| `mark_name` | `string` | ✅ 是 | 標記名稱，例如：停車場名稱、目的地名稱 |

**使用範例**：

1. **簡單導航**：
```json
{
  "start_lat": 25.0330,
  "start_lng": 121.5654,
  "waypoints": [
    {
      "lat": 25.0340,
      "lng": 121.5664,
      "mark_type": "destination",
      "arrival_method": "drive",
      "mark_name": "台北101"
    }
  ]
}
```

2. **停車場到目的地**：
```json
{
  "start_lat": 25.0330,
  "start_lng": 121.5654,
  "waypoints": [
    {
      "lat": 25.0335,
      "lng": 121.5659,
      "mark_type": "parkinglot",
      "arrival_method": "drive",
      "mark_name": "信義區停車場"
    },
    {
      "lat": 25.0340,
      "lng": 121.5664,
      "mark_type": "destination",
      "arrival_method": "walk",
      "mark_name": "台北101"
    }
  ]
}
```

3. **多點導航**：
```json
{
  "start_lat": 25.0330,
  "start_lng": 121.5654,
  "waypoints": [
    {
      "lat": 25.0335,
      "lng": 121.5659,
      "mark_type": "waypoint",
      "arrival_method": "drive",
      "mark_name": "中繼點A"
    },
    {
      "lat": 25.0340,
      "lng": 121.5664,
      "mark_type": "waypoint",
      "arrival_method": "drive",
      "mark_name": "中繼點B"
    },
    {
      "lat": 25.0345,
      "lng": 121.5669,
      "mark_type": "destination",
      "arrival_method": "drive",
      "mark_name": "最終目的地"
    }
  ]
}
```

---

## 🅿️ 11. `mark_parked_here`

**說明**：在 in-app 地圖上標記使用者目前停車的位置。

**參數定義**：

| 參數名稱 | 類型 | 是否必填 | 說明 |
|----|---|----|---|
| `poi_id` | `string` | ✅ 是 | 停車場或加油站的 ID |

**範例**：
```json
{
  "poi_id": "d19bb199-b3bd-488c-9b76-f5a3907961fb"
}
```

---

## 🌤️ 12. `get_weather_info`

**說明**：取得某個座標點的氣象資訊。

**參數定義**：

| 參數名稱 | 類型 | 是否必填 | 說明 |
|----|---|----|---|
| `lat` | `number` | ❌ 否 | 中心點緯度 |
| `lng` | `number` | ❌ 否 | 中心點經度 |

**範例**：
```json
{
  "lat": 25.0330,
  "lng": 121.5654
}
```

---

## 🔗 13. `parse_google_map_url`

**說明**：當使用者貼給你 Google Map 網址時，先解析 Google Map 的 URL，這個工具會回傳經緯度、地標名稱。

**參數定義**：

| 參數名稱 | 類型 | 是否必填 | 說明 |
|----|---|----|---|
| `google_map_url` | `string` | ✅ 是 | Google Map 的 URL |

**範例**：
```json
{
  "google_map_url": "https://www.google.com/maps/place/Taipei+101/@25.0330,121.5654,17z/"
}
```

---

## 🌐 14. `open_store_homepage_website`

**說明**：開啟商店（例如租車行）的網站，提供商店 poi_id 即可。

**參數定義**：

| 參數名稱 | 類型 | 是否必填 | 說明 |
|----|---|----|---|
| `poi_id` | `string` | ✅ 是 | 商店 poi_id |

**範例**：
```json
{
  "poi_id": "d19bb199-b3bd-488c-9b76-f5a3907961fb"
}
```

---

## 🌐 15. `open_web_page`

**說明**：開啟網站，請務必小心使用，請勿開啟有害網站。

**參數定義**：

| 參數名稱 | 類型 | 是否必填 | 說明 |
|----|---|----|---|
| `url` | `string` | ✅ 是 | 網站 URL |

**範例**：
```json
{
  "url": "https://www.mochi.com.tw"
}
```

---

## 🗺️ 16. `show_general_pois_on_map`

**說明**：在地圖上標記出來一個或多個地標，提供地標的經緯度和名稱，通常用在使用者在尋找非停車場、加油站或是租車行時的一般性地標，例如：星巴克、牛肉麵等等。

**參數定義**：

| 參數名稱 | 類型 | 是否必填 | 說明 |
|----|---|----|---|
| `pois` | `array` | ✅ 是 | 地標陣列 |

**pois 陣列項目**：

| 參數名稱 | 類型 | 是否必填 | 說明 |
|----|---|----|---|
| `lat` | `number` | ✅ 是 | 地標緯度 |
| `lng` | `number` | ✅ 是 | 地標經度 |
| `name` | `string` | ✅ 是 | 地標名稱 |

**範例**：
```json
{
  "pois": [
    {
      "lat": 25.0330,
      "lng": 121.5654,
      "name": "星巴克台北101店"
    },
    {
      "lat": 25.0340,
      "lng": 121.5664,
      "name": "鼎泰豐信義店"
    }
  ]
}
```

---

## 🗺️ 17. `open_poi_street_view`

**說明**：開啟特定 POI（僅限停車場或加油站）的街景。

**參數定義**：

| 參數名稱 | 類型 | 是否必填 | 說明 |
|----|---|----|---|
| `poi_id` | `string` | ✅ 是 | 停車場或加油站的 ID |
| `poi_type` | `string` | ✅ 是 | POI 的類型，選項有：parkinglot、gas_station |

**範例**：
```json
{
  "poi_id": "d19bb199-b3bd-488c-9b76-f5a3907961fb",
  "poi_type": "parkinglot"
}
```

---

## 💳 18. `get_discount_parkinglot_brand_by_bank`

**說明**：取得特定銀行的停車場品牌列表，舉例：幫我找台新銀行的優惠停車場。

**參數定義**：

| 參數名稱 | 類型 | 是否必填 | 說明 |
|----|---|----|---|
| `bank_name` | `string` | ✅ 是 | 銀行名稱 |

**範例**：
```json
{
  "bank_name": "台新銀行"
}
```

---

## 💳 19. `get_discount_parkinglot_brand_by_credit_card`

**說明**：取得特定信用卡的停車場品牌列表，舉例：幫我找白金商旅卡的優惠停車場。

**參數定義**：

| 參數名稱 | 類型 | 是否必填 | 說明 |
|----|---|----|---|
| `credit_card_name` | `string` | ✅ 是 | 信用卡名稱 |

**範例**：
```json
{
  "credit_card_name": "白金商旅卡"
}
```
