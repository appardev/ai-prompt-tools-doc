# 🚗 Mochi Tools v5 工具文件

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
| `start_lng` | `number` | ✅ 是 | 起點經度，可以是使用者目前所在位置或是任意座標 |
| `waypoints` | `array` | ✅ 是 | 路徑點陣列 |

**waypoints 陣列項目**：

| 參數名稱 | 類型 | 是否必填 | 說明 |
|----|---|----|---|
| `lat` | `number` | ✅ 是 | 路徑點緯度 |
| `lng` | `number` | ✅ 是 | 路徑點經度 |
| `mark_type` | `string` | ✅ 是 | 標記類型，選項有：parkinglot、gas_station、waypoint、destination |
| `arrival_method` | `string` | ✅ 是 | 到達該地標的方式，選項有：drive、walk |
| `mark_name` | `string` | ✅ 是 | 標記名稱，例如：停車場名稱、目的地名稱 |

**範例**：
```json
{
  "start_lat": 25.0330,
  "start_lng": 121.5654,
  "waypoints": [
    {
      "lat": 25.0330,
      "lng": 121.5654,
      "mark_type": "user_location",
      "arrival_method": "drive",
      "mark_name": "我的位置"
    },
    {
      "lat": 25.0340,
      "lng": 121.5664,
      "mark_type": "parkinglot",
      "arrival_method": "drive",
      "mark_name": "台北車站停車場"
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

**範例**：
```json
{
  "poi_id": "d19bb199-b3bd-488c-9b76-f5a3907961fb",
  "poi_type": "parkinglot",
  "waypoints": [
    {
      "lat": 25.0330,
      "lng": 121.5654,
      "mark_type": "user_location",
      "arrival_method": "drive",
      "mark_name": "我的位置"
    },
    {
      "lat": 25.0340,
      "lng": 121.5664,
      "mark_type": "parkinglot",
      "arrival_method": "drive",
      "mark_name": "台北車站停車場"
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
| `waypoints` | `array` | ✅ 是 | 路徑點陣列 |

**waypoints 陣列項目**：

| 參數名稱 | 類型 | 是否必填 | 說明 |
|----|---|----|---|
| `lat` | `number` | ✅ 是 | 路徑點緯度 |
| `lng` | `number` | ✅ 是 | 路徑點經度 |
| `mark_type` | `string` | ✅ 是 | 標記類型，選項有：parkinglot、gas_station、waypoint、destination |
| `arrival_method` | `string` | ✅ 是 | 到達該地標的方式，選項有：drive、walk |
| `mark_name` | `string` | ✅ 是 | 標記名稱，例如：停車場名稱、目的地名稱 |

**範例**：
```json
{
  "start_lat": 25.0330,
  "start_lng": 121.5654,
  "waypoints": [
    {
      "lat": 25.0330,
      "lng": 121.5654,
      "mark_type": "user_location",
      "arrival_method": "drive",
      "mark_name": "我的位置"
    },
    {
      "lat": 25.0340,
      "lng": 121.5664,
      "mark_type": "parkinglot",
      "arrival_method": "drive",
      "mark_name": "台北車站停車場"
    },
    {
      "lat": 25.0350,
      "lng": 121.5674,
      "mark_type": "destination",
      "arrival_method": "walk",
      "mark_name": "台北101"
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
