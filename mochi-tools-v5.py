# Tool key: mochi-tools, version: 5

[
    {
        "type": "function",
        "function": {
            "name": "get_parkinglots",
            "description": "獲取指定中心點座標附近停車場，座標不一定是使用者的位置，例如：使用者可能會詢問某個地標附近的停車場",
            "parameters": {
                "type": "object",
                "properties": {
                    "center_spot_lat": {
                        "type": "number",
                        "description": "中心點緯度"
                    },
                    "center_spot_lng": {
                        "type": "number", 
                        "description": "中心點經度"
                    },
                    "min_price": {
                        "type": "integer",
                        "description": "最低價格"
                    },
                    "center_spot_name": {
                        "type": "string",
                        "description": "中心點名稱，例如：使用者位置、某個地標"
                    },
                    "max_price": {
                        "type": "integer", 
                        "description": "最高價格"
                    },
                    "is_cooperated": {
                        "type": "boolean",
                        "description": "支援車麻吉付款"
                    },
                    "brand": {
                        "type": "string",
                        "description": "停車場指定品牌（嘟嘟房、台灣聯通...）"
                    },
                    "destination_lat": {
                        "type": "number",
                        "description": "終點緯度，用來判斷方向並進行導航"
                    },
                    "destination_lng": {
                        "type": "number",
                        "description": "終點經度，用來判斷方向並進行導航"
                    },
                    "search_radius": {
                        "type": "integer",
                        "description": "搜尋半徑，單位為公尺, 預設是 1600 公尺，可擴大到 2500 公尺"
                    },
                    "height_limit": {
                        "type": "integer",
                        "description": "高度限制，單位為公分"
                    },
                    "supports_charging": {
                        "type": "boolean",
                        "description": "是否支援充電"
                    },
                    "is_mechanical": {
                        "type": "boolean",
                        "description": "是否為機械式停車場"
                    },
                    "building_type": {
                        "type": "string",
                        "description": "停車場室內外類型，例如：indoor, outdoor"
                    },
                    "autopass_payment_type": {
                        "type": "string",
                        "description": "車麻吉付款指定方式（還沒實作），選項有：麻吉付、快速通、條碼付、掃碼付",
                        "enum": ["麻吉付", "快速通", "條碼付", "掃碼付"]
                    }
                },
                "required": ["search_radius"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_gas_stations",
            "description": "獲取指定中心點座標附近的加油站",
            "parameters": {
                "type": "object",
                "properties": {
                    "center_spot_lat": {
                        "type": "number",
                        "description": "中心點緯度"
                    },
                    "center_spot_lng": {
                        "type": "number",
                        "description": "中心點經度"
                    },
                    "center_spot_name": {
                        "type": "string",
                        "description": "中心點名稱，例如：使用者位置、某個地標"
                    },
                    "brand": {
                        "type": "string",
                        "description": "加油站品牌，台灣的加油站有：中油、台塑（台亞）、全國、山隆、西歐、速邁樂 Smile、北基、車容坊、台糖"
                    },
                    "supplier": {
                        "type": "string",
                        "enum": ["台塑", "中油"],
                        "description": "供應商"
                    },
                    "gas_types": {
                        "type": "string",
                        "enum": ["92", "95", "98", "柴油"],
                        "description": "支援油品類型，單選",
                    },
                    "is_support_self_service": {
                        "type": "boolean",
                        "description": "是否支援自助加油"
                    },
                    "destination_lat": {
                        "type": "number",
                        "description": "終點緯度，用來判斷方向並進行導航"
                    },
                    "destination_lng": {
                        "type": "number",
                        "description": "終點經度，用來判斷方向並進行導航"
                    },
                    "search_radius": {
                        "type": "integer",
                        "description": "搜尋半徑，單位為公尺, 預設是 10000 公尺"
                    }
                },
                "required": ["search_radius"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_car_rental_stores",
            "description": "獲取指定中心點座標附近的租車行",
            "parameters": {
                "type": "object",
                "properties": {
                    "center_spot_lat": {
                        "type": "number",
                        "description": "中心點緯度"
                    },
                    "center_spot_lng": {
                        "type": "number",
                        "description": "中心點經度"
                    }
                },
                "required": ["center_spot_lat", "center_spot_lng"]
            }
        }
    },
    {
        "type": "function", 
        "function": {
            "name": "start_navigation_in_app",
            "description": "開啟 app 內導航到地點",
            "parameters": {
                "type": "object",
                "properties": {
                    "start_lat": {
                        "type": "number",
                        "description": "起點緯度，可以是使用者目前所在位置或是任意座標"
                    },
                    "start_lng": {
                        "type": "number",
                        "description": "起點經度，可以是使用者目前所在位置或是任意座標"
                    },
                    "waypoints": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "lat": {
                                    "type": "number",
                                    "description": "路徑點緯度"
                                },
                                "lng": {
                                    "type": "number",
                                    "description": "路徑點經度"
                                },
                                "mark_type": {
                                    "type": "string", 
                                    "enum": [
                                        "parkinglot", 
                                        "gas_station", 
                                        "waypoint", 
                                        "destination"
                                    ],
                                    "description": "標記類型，若該地標是停車場或加油站，則 mark_type 應為 parkinglot 或 gas_station。若該地標不是停車場或是加油站, 而是中間行經的路徑點, 則 mark_type 應為 waypoint, 若為所有路徑點的最後一站，且不是停車場或加油站, 則 mark_type 應為 destination。"
                                },
                                "arrival_method": {
                                    "type": "string",
                                    "enum": ["drive", "walk"],
                                    "description": "到達該地標的方式，drive 表示開車，walk 表示步行"
                                },
                                "mark_name": {
                                    "type": "string",
                                    "description": "標記名稱，例如：停車場名稱、目的地名稱"
                                }
                            }
                        },
                        "description": "路徑點陣列"
                    }
                },
                "required": ["start_lat", "start_lng", "waypoints"]
            }
        }
    },
    {
        "type": "function", 
        "function": {
            "name": "start_navigation_google_map",
            "description": "開啟 google map 導航到地點",
            "parameters": {
                "type": "object",
                "properties": {
                    "google_map_query": {
                        "type": "string",
                        "description": "google map 查詢字串, 直接回傳引數部分的字串就好, 也不需要任何單引號或是雙引號。saddr 是起點, daddr 是終點, waypoints 是中間點, directionsmode 是導航模式, driving 是開車, walking 是步行。例如, 多點導航: saddr=55.852866,-4.323120&daddr=56.019015,-3.372803+to:55.972934,-3.279419+to:55.932952,-3.284912+to:56.022085,-3.565063&directionsmode=driving。例如, 單點導航: saddr=37.4419,-122.143&daddr=37.7749,-122.4194&directionsmode=walking"
                    }
                },
                "required": ["google_map_query"]
            }
        }
        # comgooglemapsurl://?saddr=37.4419,-122.143&daddr=37.7749,-122.4194&directionsmode=walking
        # comgooglemapsurl://?saddr=55.852866,-4.323120&daddr=56.019015,-3.372803+to:55.972934,-3.279419+to:55.932952,-3.284912+to:56.022085,-3.565063&directionsmode=driving
    },
    {
        "type": "function", 
        "function": {
            "name": "start_navigation_apple_map",
            "description": "開啟 apple map 導航到地點",
            "parameters": {
                "type": "object",
                "properties": {
                    "lat": {
                        "type": "number",
                        "description": "目的地緯度"
                    },
                    "lng": {
                        "type": "number", 
                        "description": "目的地經度"
                    }
                },
                "required": ["lat", "lng"]
            }
        }
        # comgooglemapsurl://?saddr=37.4419,-122.143&daddr=37.7749,-122.4194&directionsmode=walking
        # comgooglemapsurl://?saddr=55.852866,-4.323120&daddr=56.019015,-3.372803+to:55.972934,-3.279419+to:55.932952,-3.284912+to:56.022085,-3.565063&directionsmode=driving
    },
    {
        "type": "function",
        "function": {
            "name": "place_search",
            "description": "搜尋某個座標點的附近地點資訊，並回傳地點資訊",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "搜尋關鍵字"
                    },
                    "center_spot_lat": {
                        "type": "number",
                        "description": "中心點緯度"
                    },
                    "center_spot_lng": {
                        "type": "number", 
                        "description": "中心點經度"
                    },
                },
                "required": ["query", "center_spot_lat", "center_spot_lng"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "recommend_best_poi_with_route_on_map",
            "description": "依照使用者的偏好或對話裡需求，挑選出來適合的停車場或是加油站。若使用這個工具，UI，會在地圖上標記出來。也同時畫出導航路線在地圖上。在規劃路線的 waypoints 中，請依照提示詞的設定，規劃出適合的路徑。",
            "parameters": {
                "type": "object",
                "properties": {
                    "poi_id": {
                        "type": "string",
                        "description": "停車場或加油站的 ID, 例如: d19bb199-b3bd-488c-9b76-f5a3907961fb"
                    },
                    "poi_type": {
                        "type": "string",
                        "description": "poi 的類型，例如：parkinglot 或 gas_station",
                        "enum": ["parkinglot", "gas_station"]
                    },
                    "waypoints": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "lat": {
                                    "type": "number",
                                    "description": "路徑點緯度"
                                },
                                "lng": {
                                    "type": "number",
                                    "description": "路徑點經度"
                                },
                                "mark_type": {
                                    "type": "string", 
                                    "enum": [
                                        "parkinglot", 
                                        "gas_station", 
                                        "waypoint", 
                                        "destination",
                                        "user_location"
                                    ],
                                    "description": "標記類型，若該地標是停車場或加油站，則 mark_type 必須為 parkinglot 或 gas_station。若為使用者座標，則 mark_type 必須為 user_location。若是除上述外的行經的路徑點, 則 mark_type 必須為 waypoint, 若為所有路徑點的最後一站，且不是停車場或加油站, 則 mark_type 必須為 destination。"
                                },
                                "arrival_method": {
                                    "type": "string",
                                    "enum": ["drive", "walk"],
                                    "description": "到達該地標的方式，drive 表示開車，walk 表示步行"
                                },
                                "mark_name": {
                                    "type": "string",
                                    "description": "標記名稱，例如：停車場名稱、目的地名稱"
                                }
                            }
                        },
                        "description": "依照使用者請求規劃的路徑點陣列"
                    }
                },
                "required": ["poi_id", "poi_type", "waypoints"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "recommend_more_pois_on_map",
            "description": "當使用者不滿意原先的推薦的停車場或加油站的 poi 而再詢問「請幫我找更多」時，請使用已經取得的停車場或是加油站（同一種類型的 poi），當成參數使用這個工具列出來給使用者，最多三個。",
            "parameters": {
                "type": "object",
                "properties": {
                    "candidate_pois": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "poi_id": {
                                    "type": "string",
                                    "description": "停車場或加油站的 ID, 例如: d19bb199-b3bd-488c-9b76-f5a3907961fb"
                                },
                                "poi_type": {
                                    "type": "string",
                                    "description": "poi 的類型，例如：parkinglot 或 gas_station"
                                }
                            },
                            "required": ["poi_id", "poi_type"]
                        },
                        "description": "候選停車場的餘位和價格資訊陣列，順序同 candidate_poi_ids"
                    }
                },
                "required": ["candidate_pois"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_route_planning",
            "description": "抓取導航規劃後的結果，同時在地圖上繪製導航路線，可以多點多交通方式導航",
            "parameters": {
                "type": "object",
                "properties": {
                    "start_lat": {
                        "type": "number",
                        "description": "起點緯度，可以是使用者目前所在位置或是任意座標"
                    },
                    "start_lng": {
                        "type": "number",
                        "description": "起點經度，可以是使用者目前所在位置或是任意座標"
                    },
                    "waypoints": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "lat": {
                                    "type": "number",
                                    "description": "路徑點緯度"
                                },
                                "lng": {
                                    "type": "number",
                                    "description": "路徑點經度"
                                },
                                "mark_type": {
                                    "type": "string", 
                                    "enum": [
                                        "parkinglot", 
                                        "gas_station", 
                                        "waypoint", 
                                        "destination"
                                    ],
                                    "description": "標記類型，若該地標是停車場或加油站，則 mark_type 應為 parkinglot 或 gas_station。若該地標不是停車場或是加油站, 而是中間行經的路徑點, 則 mark_type 應為 waypoint, 若為所有路徑點的最後一站，且不是停車場或加油站, 則 mark_type 應為 destination。"
                                },
                                "arrival_method": {
                                    "type": "string",
                                    "enum": ["drive", "walk"],
                                    "description": "到達該地標的方式，drive 表示開車，walk 表示步行"
                                },
                                "mark_name": {
                                    "type": "string",
                                    "description": "標記名稱，例如：停車場名稱、目的地名稱"
                                }
                            }
                        },
                        "description": "路徑點陣列"
                    }
                },
                "required": ["start_lat", "start_lng", "waypoints"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "mark_parked_here",
            "description": "在 in-app 地圖上標記使用者目前停車的位置",
            "parameters": {
                "type": "object",
                "properties": {
                    "poi_id": {
                        "type": "string",
                        "description": "停車場或加油站的 ID"
                    }
                },
                "required": ["poi_id"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_weather_info",
            "description": "取得某個座標點的氣象資訊",
            "parameters": {
                "type": "object",
                "properties": {
                    "lat": {
                        "type": "number",
                        "description": "中心點緯度"
                    },
                    "lng": {
                        "type": "number",
                        "description": "中心點經度"
                    }
                }
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "parse_google_map_url",
            "description": "當使用者貼給你 google map 網址時，先解析 google map 的 url, 這個工具會回傳經緯度、地標名稱",
            "parameters": {
                "type": "object",
                "properties": {
                    "google_map_url": {
                        "type": "string",
                        "description": "google map 的 url"
                    }
                },
                "required": ["google_map_url"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "open_store_homepage_website",
            "description": "開啟商店（例如租車行）的網站，提供商店 poi_id 即可",
            "parameters": {
                "type": "object",
                "properties": {
                    "poi_id": {
                        "type": "string",
                        "description": "商店 poi_id"
                    }
                },
                "required": ["poi_id"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "open_web_page",
            "description": "開啟網站，請務必小心使用，請勿開啟有害網站。",
            "parameters": {
                "type": "object",
                "properties": {
                    "url": {
                        "type": "string",
                        "description": "網站 url"
                    }
                },
                "required": ["url"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "show_general_pois_on_map",
            "description": "在地圖上標記出來一個或多個地標，提供地標的經緯度和名稱，通常用在使用者在尋找非停車場、加油站或是租車行時的一般性地標，例如：星巴克、牛肉麵等等",
            "parameters": {
                "type": "object",
                "properties": {
                    "pois": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "lat": {
                                    "type": "number",
                                    "description": "地標緯度"
                                },
                                "lng": {
                                    "type": "number",
                                    "description": "地標經度"
                                },
                                "name": {
                                    "type": "string",
                                    "description": "地標名稱"
                                }
                            }
                        }
                    }
                },
                "required": ["pois"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "open_poi_street_view",
            "description": "開啟特定 poi （僅限停車場或加油站）的街景",
            "parameters": {
                "type": "object",
                "properties": {
                    "poi_id": {
                        "type": "string",
                        "description": "停車場或加油站的 ID"
                    },
                    "poi_type": {
                        "type": "string",
                        "description": "poi 的類型，例如：parkinglot 或 gas_station",
                        "enum": ["parkinglot", "gas_station"]
                    },
                },
                "required": ["poi_id", "poi_type"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_discount_parkinglot_brand_by_bank",
            "description": "取得特定銀行的停車場品牌列表，舉例：幫我找台新銀行的優惠停車場",
            "parameters": {
                "type": "object",
                "properties": {
                    "bank_name": {
                        "type": "string",
                        "description": "銀行名稱"
                    },
                },
                "required": ["bank_name"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_discount_parkinglot_brand_by_credit_card",
            "description": "取得特定信用卡的停車場品牌列表，舉例：幫我找白金商旅卡的優惠停車場",
            "parameters": {
                "type": "object",
                "properties": {
                    "credit_card_name": {
                        "type": "string",
                        "description": "信用卡名稱"
                    },
                },
                "required": ["credit_card_name"]
            }
        }
    }
]